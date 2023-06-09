cmake_minimum_required(VERSION 3.10.2)
project(opengl_example)

set(CMAKE_CXX_STANDARD 17)
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
# Find GLFW
find_package(GLFW3 REQUIRED)
# Find GLEW
find_package(GLEW REQUIRED)
# link_directories(/opt/homebrew/Cellar/glew/2.2.0_1/lib)
# link_directories(/opt/homebrew/Cellar/glfw/3.3.8/lib)

# OPENGL_INCLUDE_DIR, GLUT_INCLUDE_DIR, OPENGL_LIBRARIES, and
# GLUT_LIBRARIES are CMake built-in variables defined when the packages
# are found.
set(INCLUDE_DIRS ${OPENGL_INCLUDE_DIR} ${GLUT_INCLUDE_DIR} ${GLEW_INCLUDE_DIRS} ${GLFW_INCLUDE_DIRS})
set(LIBRARIES ${OPENGL_LIBRARIES} ${GLUT_LIBRARIES})

include_directories(${INCLUDE_DIRS})

# Source files
FILE(GLOB_RECURSE SOURCE_FILES
    "${CMAKE_SOURCE_DIR}/src/*.cpp"
    "${CMAKE_SOURCE_DIR}/src/*.cc"
    "${CMAKE_SOURCE_DIR}/src/*.c"
)

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME} PUBLIC
    ${LIBRARIES}
    GLEW::glew
    glfw
)

