INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_VLP vlp)

FIND_PATH(
    VLP_INCLUDE_DIRS
    NAMES vlp/api.h
    HINTS $ENV{VLP_DIR}/include
        ${PC_VLP_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    VLP_LIBRARIES
    NAMES gnuradio-vlp
    HINTS $ENV{VLP_DIR}/lib
        ${PC_VLP_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(VLP DEFAULT_MSG VLP_LIBRARIES VLP_INCLUDE_DIRS)
MARK_AS_ADVANCED(VLP_LIBRARIES VLP_INCLUDE_DIRS)

