<<<<<<< HEAD
# Copyright 2011,2012,2016 Free Software Foundation, Inc.
=======
# Copyright 2011,2012 Free Software Foundation, Inc.
>>>>>>> 670f541455fc2a4e38b7cf895dcf57851449c82d
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND vlp_sources
)

set(vlp_sources "${vlp_sources}" PARENT_SCOPE)
if(NOT vlp_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT vlp_sources)

add_library(gnuradio-vlp SHARED ${vlp_sources})
target_link_libraries(gnuradio-vlp ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-vlp PROPERTIES DEFINE_SYMBOL "gnuradio_vlp_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-vlp PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
<<<<<<< HEAD
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-vlp RUNTIME_COMPONENT "vlp_runtime" DEVEL_COMPONENT "vlp_devel")
=======
install(TARGETS gnuradio-vlp
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)
>>>>>>> 670f541455fc2a4e38b7cf895dcf57851449c82d

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_vlp_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_vlp.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_vlp.cc
)

add_executable(test-vlp ${test_vlp_sources})

target_link_libraries(
  test-vlp
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-vlp
)

GR_ADD_TEST(test_vlp test-vlp)
<<<<<<< HEAD

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")

=======
>>>>>>> 670f541455fc2a4e38b7cf895dcf57851449c82d
