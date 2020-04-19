#!/bin/bash

set -e

CMAKE_FULL_VERSION=3.17.1
GCC_VERSION=7
QT_VERSION=5.14.2
IMAGE_NAME=""

POSITIONAL=()
while [[ $# -gt 0 ]] ; do
  key="$1"

  case $key in
      -n|--name)
      IMAGE_NAME="$2"
      shift # past argument
      shift # past value
      ;;
      -v|--version)
      GCC_VERSION="$2"
      shift # past argument
      shift # past value
      ;;
      --cmake_version)
      CMAKE_FULL_VERSION="$2"
      shift # past argument
      shift # past value
      ;;
      -h|--help)
        echo "usage: build.sh [--version gcc-version] [--cmake_version cmake-version] [-n image_name]"
      exit 1
      ;;
      *)    # unknown option
      POSITIONAL+=("$1") # save it in an array for later
      shift # past argument
      ;;
  esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

if [ -z "$IMAGE_NAME"] ; then
  IMAGE_NAME=bbvch/conan_qt-${QT_VERSION}_builder:gcc-${GCC_VERSION}
fi
CMAKE_VERSION="${CMAKE_FULL_VERSION%.*}"
CMAKE_BUILD="${CMAKE_FULL_VERSION##*.}"

docker build --build-arg CMAKE_VERSION=${CMAKE_VERSION} --build-arg CMAKE_BUILD=${CMAKE_BUILD} --build-arg GCC_VERSION=${GCC_VERSION} -t ${IMAGE_NAME} .
