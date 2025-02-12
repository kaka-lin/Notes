# Copyright 2018 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# cmake build file for C++ route_guide example.
# Assumes protobuf and gRPC have been installed using cmake.
# See cmake_externalproject/CMakeLists.txt for all-in-one cmake build
# that automatically builds all the dependencies before building route_guide.

cmake_minimum_required(VERSION 3.5.1)

project(ImageStreaming C CXX)

include(../common.cmake)

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Find OpenCV libraries
find_package(OpenCV REQUIRED)

# Proto file
get_filename_component(is_proto "./protos/image_streaming.proto" ABSOLUTE)
get_filename_component(is_proto_path "${is_proto}" PATH)

# Generated sources
set(is_proto_srcs "${CMAKE_SOURCE_DIR}/src/image_streaming.pb.cc")
set(is_proto_hdrs "${CMAKE_SOURCE_DIR}/src/image_streaming.pb.h")
set(is_grpc_srcs "${CMAKE_SOURCE_DIR}/src/image_streaming.grpc.pb.cc")
set(is_grpc_hdrs "${CMAKE_SOURCE_DIR}/src/image_streaming.grpc.pb.h")
add_custom_command(
    OUTPUT "${is_proto_srcs}" "${is_proto_hdrs}" "${is_grpc_srcs}" "${is_grpc_hdrs}"
    COMMAND ${_PROTOBUF_PROTOC}
    ARGS --grpc_out "${CMAKE_SOURCE_DIR}/src"
         --cpp_out "${CMAKE_SOURCE_DIR}/src"
         -I "${is_proto_path}"
         --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
         "${is_proto}"
    DEPENDS "${is_proto}")

# Include generated *.pb.h files
include_directories("${CMAKE_SOURCE_DIR}/src")

# is_grpc_proto
add_library(is_grpc_proto
    ${is_grpc_srcs}
    ${is_grpc_hdrs}
    ${is_proto_srcs}
    ${is_proto_hdrs})
target_link_libraries(is_grpc_proto
    ${_REFLECTION}
    ${OpenCV_LIBS}
    ${_GRPC_GRPCPP}
    ${_PROTOBUF_LIBPROTOBUF})

# Targets image_streaming_(client|server)
foreach(_target
    image_streaming_client image_streaming_server)
    add_executable(${_target}
        "src/${_target}.cc")
    target_link_libraries(${_target}
        is_grpc_proto
        ${_REFLECTION}
        ${_GRPC_GRPCPP}
        ${_PROTOBUF_LIBPROTOBUF})
endforeach()
