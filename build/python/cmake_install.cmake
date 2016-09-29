# Install script for directory: /home/rich/Desktop/vlp_repos/gr-vlp/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/rich/Desktop/repos2/target")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/vlp" TYPE FILE FILES
    "/home/rich/Desktop/vlp_repos/gr-vlp/python/__init__.py"
    "/home/rich/Desktop/vlp_repos/gr-vlp/python/poptical_2_distance_ff.py"
    "/home/rich/Desktop/vlp_repos/gr-vlp/python/trilat_fixed_4in_ff.py"
    "/home/rich/Desktop/vlp_repos/gr-vlp/python/error_distance.py"
    "/home/rich/Desktop/vlp_repos/gr-vlp/python/Algorithm2.py"
    "/home/rich/Desktop/vlp_repos/gr-vlp/python/Distance.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/vlp" TYPE FILE FILES
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/__init__.pyc"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/poptical_2_distance_ff.pyc"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/trilat_fixed_4in_ff.pyc"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/error_distance.pyc"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/Algorithm2.pyc"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/Distance.pyc"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/__init__.pyo"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/poptical_2_distance_ff.pyo"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/trilat_fixed_4in_ff.pyo"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/error_distance.pyo"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/Algorithm2.pyo"
    "/home/rich/Desktop/vlp_repos/gr-vlp/build/python/Distance.pyo"
    )
endif()

