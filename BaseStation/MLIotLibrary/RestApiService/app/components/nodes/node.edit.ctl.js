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
    var controllerId = "lio.controllers.node.edit";
    app.controller(controllerId, ['$scope', 'data', '$stateParams', 'modalFactory', 'nodeFactory', nodeEditController]);

    function nodeEditController($scope, data, $stateParams, modalFactory, nodeFactory) {
    	var vm = this;
    	vm.node = {};
        
        vm.nodeId = 0
        if($stateParams && $stateParams.nodeId)
        {
            vm.nodeId = $stateParams.nodeId;    
        }
        vm.titleText =  (vm.nodeId == 0) ? "Create Node" : "Node Details";
        vm.submitBtnText = (vm.nodeId == 0) ? "Create" : "Save";
        vm.triggerCoordModal = false;

        vm.openCoordinateModal = function(){
           modalFactory.openCoordinateModal(function(coordinate){
            vm.coordinate = coordinate;
           });
        }



        if(vm.nodeId != 0)
        nodeFactory.getNodeById(vm.nodeId)
        .success(function(result){
            vm.node = result.data.data;
        })
        .error(function(result){})

    }

})();
