cmake_minimum_required(VERSION 3.10)

# set the project name
project(MyProjects)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 14)

# function to compile all projects in the src directory
function(compile_projects_in_directory DIRECTORY)
  # get all subdirectories
  file(GLOB SUBDIRECTORIES RELATIVE ${DIRECTORY} ${DIRECTORY}/*)
  foreach(SUBDIRECTORY ${SUBDIRECTORIES})
    # check if it's a directory
    if(IS_DIRECTORY ${DIRECTORY}/${SUBDIRECTORY})
      # add the executable
      add_executable(${SUBDIRECTORY} ${DIRECTORY}/${SUBDIRECTORY}/main.cpp)
    endif()
  endforeach()
endfunction()

# compile all projects in the src directory
compile_projects_in_directory(${CMAKE_CURRENT_SOURCE_DIR}/src)