(function() {
    'use strict';
    /**
     * @ngdoc function
     * @name sbAdminApp.controller:MainCtrl
     * @description
     * # MainCtrl
     * Controller of the sbAdminApp
     */
    var app = angular.module('lio');
    var controllerId = "lio.controllers.node.list";
    app.controller(controllerId, ['$scope', 'nodeFactory', nodeListController]);

    function nodeListController($scope, nodeFactory) {
    	var vm = this;
    	vm.nodes = []




        nodeFactory.getAllNodes()
        .success(function(result){
            vm.nodes = result.data.data;
        })
        .error(function(result){})

    }

})();
