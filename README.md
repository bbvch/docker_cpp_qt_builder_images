[![Build Status](https://travis-ci.org/bbvch/docker_cpp_qt_builder_images.svg?branch=master)](https://travis-ci.org/bbvch/docker_cpp_qt_builder_images)

# docker C++ build images

## Usage

Dockerfiles to create container images for building C++ projects with
cmake (version 3.17.1), Qt (5.14.2), doxygen, conan and different gcc and clang compiler versions.
The compiler images depend on the pre-built bbvch/qt image (in `qt/`) to have a feasible build times on CI.

The images are uploaded to Dockerhub:

### Workflow

Images are built using github actions to build on any push. Any push to `master` will be published on [dockerhub](https://hub.docker.com/u/bbvch). 

## Available images 

#### GCC
- [bbvch/conan_qt-5.14.2_builder_gcc7 : gcc 7.5.0](https://hub.docker.com/r/bbvch/conan_qt-5.14.2_builder_gcc7)
- [bbvch/conan_qt-5.14.2_builder_gcc8 : gcc 8.4.0](https://hub.docker.com/r/bbvch/conan_qt-5.14.2_builder_gcc8)
- [bbvch/conan_qt-5.14.2_builder_gcc9 : gcc 9.3.0](https://hub.docker.com/r/bbvch/conan_qt-5.14.2_builder_gcc9)

#### Clang
- [bbvch/conan_qt-5.14.2_builder_clang50: clang 5.0.1](https://hub.docker.com/r/bbvch/conan_qt-5.14.2_builder_clang50)
- [bbvch/conan_qt-5.14.2_builder_clang60: clang 6.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.14.2_builder_clang60)
- [bbvch/conan_qt-5.14.2_builder_clang7: clang 7.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.14.2_builder_clang7)
- [bbvch/conan_qt-5.14.2_builder_clang8: clang 8.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.14.2_builder_clang8)
- [bbvch/conan_qt-5.14.2_builder_clang9: clang 9.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.14.2_builder_clang9)

# Use the images to build your c++ project in CI serviecs

These Docker images can be used to build your project using the travis-ci, github actions or azure devops.
