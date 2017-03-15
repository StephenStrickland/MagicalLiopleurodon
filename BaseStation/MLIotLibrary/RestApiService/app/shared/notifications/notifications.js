'use strict';

/**
 * @ngdoc directive
 * @name izzyposWebApp.directive:adminPosHeader
 * @description
 * # adminPosHeader
 */
angular.module('lio')
	.directive('notifications',function(){
		return {
        templateUrl:'ngviews/shared/notifications/notifications',
        restrict: 'E',
        replace: true,
    	}
	});


