#!/bin/bash

set -e

QT_VERSION=5.15.8
UBUNTU_BASE="focal"
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
      echo "usage: build.sh [--qt_version qt-version] [-b ubuntu_base] [-n image_name]"
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
  IMAGE_NAME=bbvch/${UBUNTU_BASE}_qt:${QT_VERSION}
fi

docker build --build-arg QT_VERSION=${QT_VERSION} --build-arg UBUNTU_BASE=${UBUNTU_BASE} -t ${IMAGE_NAME} .
