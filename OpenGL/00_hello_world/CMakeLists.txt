cmake_minimum_required(VERSION 3.10.2)
project(opengl_example)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSION OFF)

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Suppress warnings of the deprecation of glut functions on macOS.
if(APPLE)
    add_definitions(-Wno-deprecated-declarations)
endif()

# Find OpenGL
find_package(OpenGL REQUIRED)
# Find GLUT
find_package(GLUT REQUIRED)
# Linux
# If not on macOS, we need glew.
if(UNIX AND NOT APPLE)
    find_package(GLEW REQUIRED)
endif()

# OPENGL_INCLUDE_DIR, GLUT_INCLUDE_DIR, OPENGL_LIBRARIES, and
# GLUT_LIBRARIES are CMake built-in variables defined when the packages
# are found.
set(INCLUDE_DIRS ${OPENGL_INCLUDE_DIR} ${GLUT_INCLUDE_DIR})
set(LIBRARIES ${OPENGL_LIBRARIES} ${GLUT_LIBRARIES})

# If not on macOS, add glew include directory and library path to lists.
if(UNIX AND NOT APPLE)
    list(APPEND INCLUDE_DIRS ${GLEW_INCLUDE_DIRS})
    list(APPEND LIBRARIES ${GLEW_LIBRARIES})
endif()

include_directories(${INCLUDE_DIRS})

# Source files
FILE(GLOB_RECURSE SOURCE_FILES
    "${CMAKE_SOURCE_DIR}/src/*.cpp"
    "${CMAKE_SOURCE_DIR}/src/*.cc"
    "${CMAKE_SOURCE_DIR}/src/*.c"
)

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(
    ${PROJECT_NAME}
    ${LIBRARIES}
)
