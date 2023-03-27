cmake_minimum_required(VERSION 3.15.3)
project(CANBusExamples C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSION OFF)

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Include all files
include_directories("${CMAKE_SOURCE_DIR}/src")

# Targets multithread
foreach(_target
    receive transmit)
    add_executable(${_target}
        "src/${_target}.cc")
    target_link_libraries(${_target})
endforeach()
