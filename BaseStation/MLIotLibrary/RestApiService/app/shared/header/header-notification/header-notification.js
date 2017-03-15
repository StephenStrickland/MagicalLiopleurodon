'use strict';

/**
 * @ngdoc directive
 * @name izzyposWebApp.directive:adminPosHeader
 * @description
 * # adminPosHeader
 */
angular.module('lio')
	.directive('headerNotification',function(){
		return {
        templateUrl:'ngviews/shared/header/header-notification/header-notification',
        restrict: 'E',
        replace: true,
    	}
	});


