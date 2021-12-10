cmake_minimum_required(VERSION 3.10.2)
project(MultiThread C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSION OFF)

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Find Thread/pthread
find_package(Threads REQUIRED)

# Find OpenCV libraries
find_package(OpenCV REQUIRED)

# Include all files
include_directories("${CMAKE_SOURCE_DIR}/src")

# Targets multithread
foreach(_target
    pqueue pqueue_pair pqueue_pair_image)
    add_executable(${_target}
        "src/${_target}.cc")
    target_link_libraries(${_target}
        ${CMAKE_THREAD_LIBS_INIT}
        ${OpenCV_LIBS})
endforeach()
