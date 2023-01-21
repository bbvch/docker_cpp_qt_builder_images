ARG QT_VERSION=5.15.8
ARG UBUNTU_BASE=focal

FROM ubuntu:${UBUNTU_BASE} as cmake_builder

ARG CMAKE_VERSION=3.25
ARG CMAKE_BUILD=2

RUN apt-get update
RUN apt-get install -y wget
RUN wget https://cmake.org/files/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.${CMAKE_BUILD}-linux-x86_64.sh 
RUN mkdir /opt/cmake
RUN sh cmake-${CMAKE_VERSION}.${CMAKE_BUILD}-linux-x86_64.sh --skip-license --prefix=/opt/cmake

FROM bbvch/${UBUNTU_BASE}_qt:${QT_VERSION} as qt_image

FROM ubuntu:${UBUNTU_BASE}

ARG GCC_VERSION=8
ARG DEBIAN_FRONTEND=noninteractive

ENV TZ=Etc/UTC
ENV CC=gcc CXX=g++
ENV CMAKE_C_COMPILER=gcc CMAKE_CXX_COMPILER=g++

LABEL maintainer="Michel Estermann <michel.estermann@bbv.ch>"

# install qt - unfortunately COPY --from does not support build args
COPY --from=qt_image /usr/local/Qt /usr/local/Qt
ENV Qt5_DIR=/usr/local/Qt

# install cmake
COPY --from=cmake_builder /opt/cmake /opt/cmake

RUN ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake
RUN ln -s /opt/cmake/bin/ctest /usr/local/bin/ctest
RUN ln -s /opt/cmake/bin/cpack /usr/local/bin/cpack
RUN ln -s /opt/cmake/bin/ccmake /usr/local/bin/ccmake
RUN ln -s /opt/cmake/bin/cmake-gui /usr/local/bin/cmake-gui

RUN apt-get update
RUN apt-get -qq install -y software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
RUN apt-get update
RUN apt-get -qq  install -y build-essential \
                            lcov \
                            ninja-build \
                            git \
                            doxygen graphviz

# install qt dependencies
RUN apt-get -qq install -y '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev \
                           libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev \
                           libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev \
                           libxtst-dev libxss-dev libdbus-1-dev libevent-dev libfontconfig1-dev \
                           libcap-dev libpulse-dev libudev-dev libpci-dev libnss3-dev libasound2-dev \
                           libfreetype6-dev libegl1-mesa-dev \
                           libasound2-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
                           libgstreamer-plugins-good1.0-dev libgstreamer-plugins-bad1.0-dev

# Install gcc and dependencies
RUN apt-get -qq install -y g++-${GCC_VERSION} gcc-${GCC_VERSION}
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-${GCC_VERSION} 100
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-${GCC_VERSION} 100
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-${GCC_VERSION} 100
RUN update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-${GCC_VERSION} 100
RUN update-alternatives --install /usr/bin/gcov gcov /usr/bin/gcov-${GCC_VERSION} 100

# install conan
RUN apt-get -qq install -y python3 python3-pip
RUN pip3 install conan

RUN conan profile new default --detect && \
    conan profile update settings.compiler.libcxx=libstdc++11 default

# Cleanup
RUN apt-get -qq autoremove
RUN apt-get -qq clean

# Show versions
RUN cmake --version && \
    gcc --version && cc --version && \
    g++ --version && c++ --version && \
    ${Qt5_DIR}/bin/qmake --version
