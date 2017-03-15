'use strict';

/**
 * @ngdoc directive
 * @name izzyposWebApp.directive:adminPosHeader
 * @description
 * # adminPosHeader
 */
angular.module('lio')
	.directive('timeline',function() {
    return {
        templateUrl:'ngviews/shared/timeline/timeline',
        restrict: 'E',
        replace: true,
    }
  });
