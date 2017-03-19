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
    	vm.nodes = [];
    	vm.filtered = [];




        nodeFactory.getAllNodes()
        .success(function(result){
            vm.nodes = result.data.data;
            vm.filtered = vm.nodes;
            vm.filterNodes('');
        })
        .error(function(result){})


        vm.filterNodes = function (text) {
            if(text)
                vm.filtered = _.filter(vm.nodes, function(item){return item.Name.substring(text) > -1})
            else
                vm.filtered = vm.nodes;
        }
    }

})();
