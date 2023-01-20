#!/bin/bash

set -e

CMAKE_FULL_VERSION=3.25.2
CLANG_VERSION=12
QT_VERSION=5.15.8
IMAGE_NAME=""
UBUNTU_BASE="focal"

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
      CLANG_VERSION="$2"
      shift # past argument
      shift # past value
      ;;
      --cmake_version)
      CMAKE_FULL_VERSION="$2"
      shift # past argument
      shift # past value
      ;;
      --qt_version)
      QT_VERSION="$2"
      shift # past argument
      shift # past value
      ;;
      -b|--base)
      UBUNTU_BASE="$2"
      shift # past argument
      shift # past value
      ;;
      -h|--help)
      echo "usage: build.sh [--version clang-version] [--cmake_version cmake-version] [--qt_version qt_version] [-b ubuntu_base] [-n image_name]"
      exit 1
      ;;
      *)    # unknown option
      POSITIONAL+=("$1") # save it in an array for later
      shift # past argument
      ;;
  esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

if [ -z "$IMAGE_NAME" ] ; then
  IMAGE_NAME=bbvch/conan_qt-${QT_VERSION}_builder:clang-${CLANG_VERSION}
fi
CMAKE_VERSION="${CMAKE_FULL_VERSION%.*}"
CMAKE_BUILD="${CMAKE_FULL_VERSION##*.}"

docker build --build-arg CMAKE_VERSION=${CMAKE_VERSION} --build-arg CLANG_VERSION=${CLANG_VERSION} --build-arg QT_VERSION=${QT_VERSION} --build-arg UBUNTU_BASE=${UBUNTU_BASE} -t ${IMAGE_NAME} .
