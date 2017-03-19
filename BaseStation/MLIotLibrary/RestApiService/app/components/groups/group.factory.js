/**
 * Created by Stephen on 3/15/17.
 */
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
    var factoryId = "groupFactory";
    app.factory(factoryId, ['data', groupFactory]);

    function groupFactory(data) {
        var apiPrefix = '/api/nodes';
        var nodeFactory = {
            getAllGroups: getAllNodes,
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
