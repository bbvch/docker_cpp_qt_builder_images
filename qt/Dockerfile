FROM ubuntu:bionic

ARG QT_VERSION=5.15.2

# Build and install Qt from source
RUN apt-get update
RUN apt-get -qq install -y build-essential python python3 git perl 

RUN apt-get -qq install -y mesa-common-dev libglu1-mesa-dev libfontconfig1-dev libfreetype6-dev libx11-dev \
                           libxext-dev libxfixes-dev libxi-dev libxrender-dev libxcb1-dev libx11-xcb-dev \
                           libxcb-glx0-dev libxkbcommon-x11-dev libssl-dev libxkbcommon-dev libxkbcommon-x11-dev \
                           bluez libbluetooth-dev
RUN git clone https://code.qt.io/qt/qt5.git
WORKDIR qt5
RUN git checkout v${QT_VERSION}
RUN perl init-repository
WORKDIR ./qt-build
RUN ../configure -qt-zlib -qt-libjpeg -qt-libpng -qt-freetype -qt-pcre -qt-harfbuzz -opensource -nomake examples -nomake tests -confirm-license -prefix "/usr/local/Qt"
RUN make -s -j$(nproc)
RUN make install
WORKDIR /
RUN rm -rf qt
