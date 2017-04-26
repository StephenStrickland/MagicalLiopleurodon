cmake_minimum_required(VERSION 2.6)
cmake_policy(SET CMP0011 NEW)

project("avrlab")

# only set this if it's the very toplevel project where your module directory is
# located (in this case it's cmake)
set(CMAKE_MODULE_PATH 
	${CMAKE_MODULE_PATH} 
	"${PROJECT_SOURCE_DIR}/cmake"
	)

include(ARCB)
include(AVR)

# should be "toplevel","executable","staticlib",or "sharedlib"
set(buildType "toplevel")

# the source files located in the src/ directory
set(sources "")

#the name of the projects this project depends on
set(subProjects "")

# the internal subprojecs. NOTE: include these subprojects in the order that
# they depend on each other. For example, if proj1 depends on proj2 list proj2
# BEFORE proj1
set(internalSubDirs 
	"util" 
	"lab1"
	"lab2"
	"lab3"
	)

# DO NOT REMOVE OR MODIFY
BuildProject(
	"${buildType}"
	"${sources}"
	"${subProjects}"
	"${internalSubDirs}"
	)
