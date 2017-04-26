cmake_minimum_required(VERSION 2.6)

#the default instalation paths for Aria. This path must be set to point to the
#location where the lib/, include/, src/, etc, directories are located for Aria.

set(includeList "Aria.h")

if(WIN32)
	#Windows install path
	set(AriaInstallPath "C:/Program Files/MobileRobots/Aria")
	set(libList 
		"AriaDebugVC12"
		"winmm"
		"advapi32"
		"ws2_32"
		)
else(WIN32)
	#Linux install path
	set(AriaInstallPath "/usr/local/Aria")
	set(libList "Aria" "dl" "pthread")
endif(WIN32)

#if the environment variable sets the aria installation path then use that.
if("$ENV{ARIA_INSTALL_PATH}")
	set(AriaInstallPath "$ENV{ARIA_INSTALL_PATH}")
endif("$ENV{ARIA_INSTALL_PATH}")

#if a cache variable for the Aria install path has already been set then use that.
#This file will not be exporting this variable.
if(ARIA_INSTALL_PATH)
	set(AriaInstallPath ${ARIA_INSTALL_PATH})
endif(ARIA_INSTALL_PATH)

if(NOT IS_DIRECTORY ${AriaInstallPath})
	message(FATAL_ERROR 
		"Aria is not installed! (looking in ${AriaInstallPath}) "
		"If it is installed then set the environment variable: ARIA_INSTALL_PATH")
endif(NOT IS_DIRECTORY ${AriaInstallPath})

# find the include dirs
foreach(l ${includeList})

	find_path(${l}_include_found 
		NAMES ${l}
		PATHS "${AriaInstallPath}/include"
		)

	if(${l}_include_found EQUAL NOTFOUND)
		message(FATAL_ERROR 
			"Could not find include dir: ${l}"
			)
	endif(${l}_include_found EQUAL NOTFOUND)

	list(APPEND include_found ${${l}_include_found})
endforeach(l)


# find the dependency libraries
foreach(l ${libList})

	find_library(${l}_lib_found 
		NAMES ${l}
		PATHS "${AriaInstallPath}/lib"
		)

	if(${l}_lib_found EQUAL NOTFOUND)
		message(FATAL_ERROR 
			"Could not find library: ${l}"
			)
	endif(${l}_lib_found EQUAL NOTFOUND)

	list(APPEND lib_found ${${l}_lib_found})
endforeach(l)


set(Aria_INCLUDE_DIRS
	${include_found}
	CACHE INTERNAL "includes for Aria"
	)

set(Aria_LIBRARIES
	${lib_found}
	CACHE INTERNAL "libraries for Aria"
	)
