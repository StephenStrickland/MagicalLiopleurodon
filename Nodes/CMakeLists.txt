cmake_minimum_required(VERSION 2.6)
cmake_policy(SET CMP0011 NEW)

project("mtr3710")

set(ARCB_MODULE_PATH 
		"${PROJECT_SOURCE_DIR}/cmake/arcb/cmake"
		CACHE INTERNAL "the cmake module path to arcb")

set(MODULARTEX_MODULE_PATH
	"${PROJECT_SOURCE_DIR}/cmake/modulartex/cmake/"
	CACHE INTERNAL "the cmake module path for modulartex")

set(CMAKE_MODULE_PATH 
	${CMAKE_MODULE_PATH} 
	${ARCB_MODULE_PATH}
	"${PROJECT_SOURCE_DIR}/cmake/"
	${MODULARTEX_MODULE_PATH}
	)

set(projects 
	"Arduino"
	)

foreach(p ${projects})
	add_subdirectory(${p})
endforeach(p)
