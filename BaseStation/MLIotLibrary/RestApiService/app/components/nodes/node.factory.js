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
    var factoryId = "nodeFactory";
    app.factory(factoryId, ['data', nodeFactory]);

    function nodeFactory(data) {
        var apiPrefix = '/api/nodes';
        var nodeFactory = {
            getAllNodes: getAllNodes,
            getNodeById: getNodeById,

        };
        return nodeFactory;

        function getAllNodes() {
            return data.get(apiPrefix);
        }

        function getNodeById(nodeId){
            return data.get(apiPrefix + '/' + nodeId);
        }

    }

})();
