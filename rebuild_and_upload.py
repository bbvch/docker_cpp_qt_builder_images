#!/usr/bin/env python3

"""Build docker images and upload to hub.docker
"""
import os
import sys
import argparse


cmake_version = "3.17.1"
qt_version = "5.15.2"

class Arguments(object):
    """Collect user arguments from CLI
    """
    def __init__(self):
        self.__parser = argparse.ArgumentParser(
            description="Build and Upload Docker images")
        self.__parser.add_argument(
            "--upload",
            help="Upload image to hub docker after build",
            action="store_true")
        self.__parser.add_argument(
            "--all",
            help="Build all images (gcc and clang).",
            action="store_true")
        self.__parser.add_argument(
            "--tag",
            help="Tag to use for the image.")
        self.__parser.add_argument(
            "--build_number",
            help="Build number to use for upload.")
        self.__parser.add_argument(
            "--cmake_version",
            help="CMake version to install.",
            default=cmake_version)
        self.__parser.add_argument(
            "--qt_version",
            help="Qt version to install.",
            default=qt_version)
        self.__parser.add_argument('--gcc',
                            nargs='*',
                            dest='gcc_versions',
                            help='gcc versions to build images from. Use "*" for all versions.',
                            default=[])

        self.__parser.add_argument('--clang',
                            nargs='*',
                            dest='clang_versions',
                            help='clang versions to build images from. Use "*" for all versions.',
                            default=[])
        if len(sys.argv) == 1:
            self.__parser.print_help()
            sys.exit(1)
        self.__args = self.__parser.parse_args()

    @property
    def upload(self):
        """If image should be uploaded to hub.docker
        """
        return self.__args.upload

    @property
    def tag(self):
        """Tag to use for image
        """
        if self.__args.tag:
            return self.__args.tag
        return ""

    @property
    def build_number(self):
        """Build number to use for upload.
        """
        if self.__args.build_number:
            return self.__args.build_number
        return ""
    @property
    def cmake_version(self):
        """ help="CMake version to install.
        """
        if self.__args.cmake_version:
            return self.__args.cmake_version
        return ""

    @property
    def qt_version(self):
        """Qt version to install.
        """
        if self.__args.qt_version:
            return self.__args.qt_version
        return ""    


    def versions(self, compiler):
        """Compiler versions to be used on build
        """
        if compiler == "gcc":
            if (len(self.__args.gcc_versions) == 1) and (self.__args.gcc_versions[0] == '*'):
                return []
            return self.__args.gcc_versions
        elif compiler == "clang":
            if (len(self.__args.clang_versions) == 1) and (self.__args.clang_versions[0] == '*'):
                return []
            return self.__args.clang_versions
        return []

    @property
    def compilers(self):
        """Compiler names to be used on build
        """
        compilers = []
        if self.__args.all:
            compilers.append('gcc')
            compilers.append('clang')
            return compilers
        if len(self.__args.gcc_versions) > 0:
            compilers.append('gcc')
        if len(self.__args.clang_versions) > 0:
            compilers.append('clang')
        return compilers


class Builder(object):
    """Base builder for docker image
    """
    def __init__(self, compiler_name, compiler_versions):
        self.__compiler_name = compiler_name
        self.__compiler_versions = compiler_versions

    def build_and_upload(self, upload_after_build, versions, tag, build_number, cmake_version, qt_version):
        """Build docker image and upload to server
        """
        compiler_versions = versions or self.__compiler_versions
        for compiler_version in compiler_versions:
            folder_name = "{}".format(self.__compiler_name)
            image_name = "bbvch/conan_qt-{}_builder_{}{}".format(qt_version, self.__compiler_name, compiler_version.replace(".", ""))
            tagged_image_name = "{}:{}".format(image_name,tag) if len(tag) > 0 else image_name
            build_image_name = "{}:{}".format(image_name,build_number) if len(build_number) > 0 else tagged_image_name
            return_value = os.system("cd {} && ./build.sh -n {} -v {} --cmake_version {} --qt_version {}".format(folder_name, tagged_image_name, compiler_version, cmake_version, qt_version))
            if upload_after_build:
                if build_image_name != tagged_image_name:
                    return_value += os.system("docker tag {} {}".format(tagged_image_name, build_image_name))
                    return_value += os.system("sudo docker push {}".format(build_image_name))
                return_value += os.system("sudo docker push {}".format(tagged_image_name))
            if return_value != 0:
                return return_value

    @property
    def name(self):
        """Retrieve compiler name used by builder
        """
        return self.__compiler_name


class GccBuilder(Builder):
    """Specilized builder for GCC
    """
    def __init__(self):
        Builder.__init__(
            self, "gcc",
            ["7", "8", "9"])


class ClangBuilder(Builder):
    """Specialized builder for Clang
    """
    def __init__(self):
        Builder.__init__(
            self, "clang", 
            ["5.0", "6.0", "7", "8", "9"])


if __name__ == "__main__":
    args = Arguments()
    for builder in [GccBuilder(), ClangBuilder()]:
        if builder.name in args.compilers:
            return_value = builder.build_and_upload(args.upload, args.versions(builder.name), args.tag, args.build_number, args.cmake_version, args.qt_version)
            sys.exit(return_value)
