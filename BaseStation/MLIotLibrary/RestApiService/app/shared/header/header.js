'use strict';

/**
 * @ngdoc directive
 * @name izzyposWebApp.directive:adminPosHeader
 * @description
 * # adminPosHeader
 */
angular.module('lio')
	.directive('header',function(){
		return {
        templateUrl:'ngscripts/shared/header/header.html',
        restrict: 'E',
        replace: true,
    	}
	});


