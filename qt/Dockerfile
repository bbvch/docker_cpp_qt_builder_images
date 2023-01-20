ARG UBUNTU_BASE=focal

FROM ubuntu:${UBUNTU_BASE}

ARG QT_VERSION=5.15.8
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Build and install Qt from source
RUN apt-get update
RUN apt-get -qq install -y build-essential python3 git perl 
RUN apt-get -qq install -y libglib2.0-dev libicu-dev libudev-dev

# Libxcb stuff
RUN apt-get -qq install -y '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev \
                           libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev

# Qt WebKit
RUN apt-get -qq install -y flex bison gperf libicu-dev libxslt-dev ruby

# Qt WebEngine
RUN apt-get -qq install -y libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev \
                           libxtst-dev libxss-dev libdbus-1-dev libevent-dev libfontconfig1-dev \
                           libcap-dev libpulse-dev libudev-dev libpci-dev libnss3-dev libasound2-dev \
                           libfreetype6-dev libegl1-mesa-dev gperf bison nodejs
# Qt Multimedia
RUN apt-get -qq install -y libasound2-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
                           libgstreamer-plugins-good1.0-dev libgstreamer-plugins-bad1.0-dev

RUN git clone https://code.qt.io/qt/qt5.git
WORKDIR qt5
RUN git checkout v${QT_VERSION}
RUN perl init-repository
WORKDIR ./qt-build
RUN ../configure -v -xcb -xcb-xlib -qt-zlib -qt-tiff -qt-libjpeg -qt-libpng -system-freetype -fontconfig -qt-pcre -qt-harfbuzz -opensource -qt-doubleconversion -nomake examples -nomake tests -confirm-license -prefix "/usr/local/Qt"
RUN make -s -j$(nproc)
RUN make install
WORKDIR /
RUN rm -rf qt5