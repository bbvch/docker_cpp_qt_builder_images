FROM ubuntu:bionic as cmake_builder

ARG CMAKE_VERSION=3.17
ARG CMAKE_BUILD=1

RUN apt-get update
RUN apt-get install -y wget
RUN wget https://cmake.org/files/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.${CMAKE_BUILD}-Linux-x86_64.sh 
RUN mkdir /opt/cmake
RUN sh cmake-${CMAKE_VERSION}.${CMAKE_BUILD}-Linux-x86_64.sh --skip-license --prefix=/opt/cmake

FROM ubuntu:bionic

ARG CLANG_VERSION=9

ENV CC=clang CXX=clang++
ENV CMAKE_C_COMPILER=clang CMAKE_CXX_COMPILER=clang++

LABEL maintainer="Michel Estermann <michel.estermann@bbv.ch>"

#install qt
COPY --from=bbvch/qt:5.14.2 /usr/local/Qt /usr/local/Qt
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
RUN apt-get -qq install -y clang-${CLANG_VERSION} clang-tidy-${CLANG_VERSION} clang-format-${CLANG_VERSION} 
RUN apt-get -qq install -y llvm-${CLANG_VERSION} llvm-${CLANG_VERSION}-dev llvm-${CLANG_VERSION}-runtime llvm 
RUN apt-get -qq install -y libc++1 libc++abi1

RUN update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-${CLANG_VERSION} 100
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-${CLANG_VERSION} 100
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/clang-${CLANG_VERSION} 100
RUN update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-${CLANG_VERSION} 100
RUN update-alternatives --install /usr/bin/clang-tidy clang-tidy /usr/bin/clang-tidy-${CLANG_VERSION} 100
RUN update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-${CLANG_VERSION} 100

#install conan
RUN apt-get -qq install -y python3 python3-pip
RUN pip3 install conan


RUN conan profile new default --detect

#Cleanup
RUN apt-get -qq autoremove
RUN apt-get -qq clean