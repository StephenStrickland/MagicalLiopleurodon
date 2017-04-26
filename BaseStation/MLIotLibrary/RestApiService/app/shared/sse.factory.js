/**
 * Created by Stephen on 4/25/17.
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
    var factoryId = "sseFactory";
    app.factory(factoryId, [ sseFactory]);

    function sseFactory($uibModal) {

        var modalFactory = {
            close: close,
            addListener: addListener

        };

        var source = new EventSource('api/stream');
        return modalFactory;

        function close(){
            source.close()
        }

       function addListener(event_type, callback){
            source.addEventListener(event_type, callback, false);
       }
    }

})();
