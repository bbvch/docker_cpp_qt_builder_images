cmake_minimum_required(VERSION 3.16)
project(mainwindow LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

if(DEFINED ENV{Qt5_DIR} AND EXISTS "$ENV{Qt5_DIR}/lib")
  set(CMAKE_LIBRARY_PATH ${CMAKE_LIBRARY_PATH} "$ENV{Qt5_DIR}/lib")
endif()

find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)

add_executable(mainwindow
    colorswatch.cpp 
    colorswatch.h
    main.cpp
    mainwindow.cpp 
    mainwindow.h
    toolbar.cpp 
    toolbar.h
    mainwindow.qrc
)

target_link_libraries(mainwindow PRIVATE
    Qt5::Core
    Qt5::Gui
    Qt5::Widgets
)
