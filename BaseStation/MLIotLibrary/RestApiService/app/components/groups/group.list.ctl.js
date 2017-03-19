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
    var controllerId = "lio.controllers.groups.list";
    app.controller(controllerId, ['$scope', 'groupFactory', groupListController]);

    function groupListController($scope, groupFactory) {
        var vm = this;
        vm.nodes = []




        groupFactory.getAllGroups()
            .success(function(result){
                vm.nodes = result.data.data;
            })
            .error(function(result){})

    }

})();
/**
 * Created by Stephen on 3/15/17.
 */
