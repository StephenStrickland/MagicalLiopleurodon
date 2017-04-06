'use strict';

/**
 * @ngdoc directive
 * @name izzyposWebApp.directive:adminPosHeader
 * @description
 * # adminPosHeader
 */
angular.module('lio')
	.directive('chat',function(){
		return {
        templateUrl:'ngviews/shared/chat/chat',
        restrict: 'E',
        replace: true,
    	}
	});


