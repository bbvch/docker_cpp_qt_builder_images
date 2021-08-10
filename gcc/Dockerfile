FROM ubuntu:bionic as cmake_builder

ARG CMAKE_VERSION=3.17
ARG CMAKE_BUILD=1

RUN apt-get update
RUN apt-get install -y wget
RUN wget https://cmake.org/files/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.${CMAKE_BUILD}-Linux-x86_64.sh 
RUN mkdir /opt/cmake
RUN sh cmake-${CMAKE_VERSION}.${CMAKE_BUILD}-Linux-x86_64.sh --skip-license --prefix=/opt/cmake

FROM ubuntu:bionic

ARG GCC_VERSION=8

ENV CC=gcc CXX=g++
ENV CMAKE_C_COMPILER=gcc CMAKE_CXX_COMPILER=g++

LABEL maintainer="Michel Estermann <michel.estermann@bbv.ch>"

#install qt - unfortunately COPY --from does not support build args
#A possible workaround can be found here
COPY --from=bbvch/qt:5.15.2 /usr/local/Qt /usr/local/Qt
ENV Qt5_DIR=/usr/local/Qt

#install cmake
COPY --from=cmake_builder /opt/cmake /opt/cmake

RUN ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake
RUN ln -s /opt/cmake/bin/ctest /usr/local/bin/ctest

RUN apt-get update
RUN apt-get -qq install -y software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
RUN apt-get update
RUN apt-get -qq  install -y build-essential
RUN apt-get -qq  install -y lcov
RUN apt-get -qq  install -y ninja-build
RUN apt-get -qq  install -y git
RUN apt-get -qq  install -y doxygen graphviz

#install qt dependencies
RUN apt-get -qq install -y mesa-common-dev libglu1-mesa-dev libfontconfig1-dev libfreetype6-dev libx11-dev libxext-dev libxfixes-dev libxi-dev libxrender-dev libxcb1-dev libx11-xcb-dev libxcb-glx0-dev libxkbcommon-x11-dev

# Install Clang and dependencies
RUN apt-get -qq install -y g++-${GCC_VERSION} gcc-${GCC_VERSION}
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-${GCC_VERSION} 100
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-${GCC_VERSION} 100
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-${GCC_VERSION} 100
RUN update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-${GCC_VERSION} 100

#install conan
RUN apt-get -qq install -y python3 python3-pip
RUN pip3 install conan

RUN conan profile new default --detect
RUN conan profile update settings.compiler.libcxx=libstdc++11 default

#Cleanup
RUN apt-get -qq autoremove
RUN apt-get -qq clean
