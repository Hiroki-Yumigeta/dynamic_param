cmake_minimum_required(VERSION 2.8.3)
project(dynamic_param)


find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure # add
  roscpp
  rospy
)

find_package(Boost REQUIRED)
find_package(OpenCV REQUIRED)

# add
generate_dynamic_reconfigure_options(
  cfg/Tutorial.cfg
  cfg/cv_param.cfg
)


catkin_package(
#  INCLUDE_DIRS include
  LIBRARIES dynamic_param
  CATKIN_DEPENDS dynamic_reconfigure roscpp rospy # add
  DEPENDS eigen opencv
#  DEPENDS system_lib
)

## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
  ${EIGEN_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

add_executable(server src/server.cpp) # add(C++)

add_dependencies(server dynamic_param_gencfg) # add(C++)

target_link_libraries(server ${catkin_LIBRARIES} ${Boost_LIBRARIES} ${OpenCV_LIBS}) # add(C++)