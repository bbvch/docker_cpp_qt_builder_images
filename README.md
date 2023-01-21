[![Github Actions Build Status](https://github.com/bbvch/docker_cpp_qt_builder_images/workflows/CI/badge.svg?branch=master)](https://github.com/bbvch/docker_cpp_qt_builder_images/actions)

# docker C++ build images

## Usage

_Ubuntu focal_ based dockerfiles to create container images for building C++ projects with
cmake, Qt, doxygen, conan, openssl and different gcc and clang compiler versions.
The compiler images depend on the pre-built bbvch/qt image (in `qt/`) to have feasible build times on CI.

The images are uploaded to Dockerhub:

### Workflow

Images are built using github actions to build on any push. Any push to `master` will be published on [dockerhub](https://hub.docker.com/u/bbvch). 

## Available images 

### Qt 5.15.8-lts-lgpl & CMake 3.25.2 (jammy)

#### GCC

- [bbvch/conan_qt-5.15.8_builder_gcc11_jammy : gcc 11.3.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_gcc11_jammy)
- [bbvch/conan_qt-5.15.8_builder_gcc121_jammy : gcc 12.1.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_gcc12_jammy)

#### Clang
- [bbvch/conan_qt-5.15.8_builder_clang15_jammy: clang 14.0.6](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_clang14_jammy)
- [bbvch/conan_qt-5.15.8_builder_clang15_jammy: clang 15.0.7](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_clang15_jammy)


### Qt 5.15.8-lts-lgpl & CMake 3.25.2 (focal)

#### GCC

- [bbvch/conan_qt-5.15.8_builder_gcc7_focal : gcc 7.5.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_gcc7_focal)
- [bbvch/conan_qt-5.15.8_builder_gcc8_focal : gcc 8.4.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_gcc8_focal)
- [bbvch/conan_qt-5.15.8_builder_gcc9_focal : gcc 9.4.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_gcc9_focal)
- [bbvch/conan_qt-5.15.8_builder_gcc10_focal : gcc 10.3.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_gcc10_focal)
- [bbvch/conan_qt-5.15.8_builder_gcc11_focal : gcc 11.1.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_gcc11_focal)

#### Clang
- [bbvch/conan_qt-5.15.8_builder_clang7_focal: clang 7.0.1](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_clang7_focal)
- [bbvch/conan_qt-5.15.8_builder_clang8_focal: clang 8.0.1](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_clang8_focal)
- [bbvch/conan_qt-5.15.8_builder_clang9_focal: clang 9.0.1](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_clang9_focal)
- [bbvch/conan_qt-5.15.8_builder_clang10_focal: clang 10.0.1](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_clang10_focal)
- [bbvch/conan_qt-5.15.8_builder_clang11_focal: clang 11.1.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_clang11_focal)
- [bbvch/conan_qt-5.15.8_builder_clang12_focal: clang 12.0.1](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_clang12_focal)
- [bbvch/conan_qt-5.15.8_builder_clang13_focal: clang 13.0.1](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_clang13_focal)
- [bbvch/conan_qt-5.15.8_builder_clang14_focal: clang 14.0.6](https://hub.docker.com/r/bbvch/conan_qt-5.15.8_builder_clang14_focal)


### Qt 5.15.2 & CMake 3.22.1 (bionic)

#### GCC

- [bbvch/conan_qt-5.15.2_builder_gcc7 : gcc 7.5.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_gcc7)
- [bbvch/conan_qt-5.15.2_builder_gcc8 : gcc 8.4.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_gcc8)
- [bbvch/conan_qt-5.15.2_builder_gcc9 : gcc 9.3.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_gcc9)
- [bbvch/conan_qt-5.15.2_builder_gcc10 : gcc 10](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_gcc10)
- [bbvch/conan_qt-5.15.2_builder_gcc11 : gcc 11](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_gcc11)

#### Clang
- [bbvch/conan_qt-5.15.2_builder_clang50: clang 5.0.1](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_clang50)
- [bbvch/conan_qt-5.15.2_builder_clang60: clang 6.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_clang60)
- [bbvch/conan_qt-5.15.2_builder_clang7: clang 7.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_clang7)
- [bbvch/conan_qt-5.15.2_builder_clang8: clang 8.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_clang8)
- [bbvch/conan_qt-5.15.2_builder_clang9: clang 9.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_clang9)
- [bbvch/conan_qt-5.15.2_builder_clang10: clang 10.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_clang10)
- [bbvch/conan_qt-5.15.2_builder_clang11: clang 11.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_clang11)
- [bbvch/conan_qt-5.15.2_builder_clang12: clang 12.0.0](https://hub.docker.com/r/bbvch/conan_qt-5.15.2_builder_clang12)


### Qt 5.14.2 & CMake 3.17.1 (bionic)

Qt 5.14.2 images are missing openssl and bluetooth support for qt

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
