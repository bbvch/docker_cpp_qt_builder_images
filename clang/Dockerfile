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

ARG UBUNTU_BASE=focal
ARG CLANG_VERSION=12
ARG DEBIAN_FRONTEND=noninteractive

ENV TZ=Etc/UTC
ENV CC=clang CXX=clang++
ENV CMAKE_C_COMPILER=clang CMAKE_CXX_COMPILER=clang++

LABEL maintainer="Michel Estermann <michel.estermann@bbv.ch>"

#install qt
COPY --from=qt_image /usr/local/Qt /usr/local/Qt
ENV Qt5_DIR=/usr/local/Qt

#install cmake
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
RUN apt-get -qq  install -y build-essential libstdc++-11-dev \
                            lcov \
                            ninja-build \
                            git wget \
                            doxygen graphviz

# add repos for clang
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
RUN if [ "${UBUNTU_BASE}" = "focal" ] && [ "${CLANG_VERSION}" -gt "9" ] ; then echo "deb http://apt.llvm.org/${UBUNTU_BASE}/ llvm-toolchain-${UBUNTU_BASE}-${CLANG_VERSION} main" | tee -a /etc/apt/sources.list ; fi
RUN if [ "${UBUNTU_BASE}" = "jammy" ] && [ "${CLANG_VERSION}" -gt "13" ] ; then echo "deb http://apt.llvm.org/${UBUNTU_BASE}/ llvm-toolchain-${UBUNTU_BASE}-${CLANG_VERSION} main" | tee -a /etc/apt/sources.list ; fi

RUN apt-get update

# install qt dependencies
RUN apt-get -qq install -y '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev \
                           libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev \
                           libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev \
                           libxtst-dev libxss-dev libdbus-1-dev libevent-dev libfontconfig1-dev \
                           libcap-dev libpulse-dev libudev-dev libpci-dev libnss3-dev libasound2-dev \
                           libfreetype6-dev libegl1-mesa-dev \
                           libasound2-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
                           libgstreamer-plugins-good1.0-dev libgstreamer-plugins-bad1.0-dev

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

# Show versions
RUN cmake --version && \
    clang --version && cc --version && \
    clang++ --version && c++ --version && \
    ${Qt5_DIR}/bin/qmake --version