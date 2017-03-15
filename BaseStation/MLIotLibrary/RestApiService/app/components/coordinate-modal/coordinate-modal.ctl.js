(function() {
    'use strict';
    /**
     * @ngdoc function
     * @name lio.controller:coordinate-modal
     * @description
     * # MainCtrl
     * Controller of the sbAdminApp
     */
    var app = angular.module('lio');
    var controllerId = "lio.controllers.coordinate-modal";
    app.controller(controllerId, ['$scope', '$uibModalInstance', coordinateModalController]);

    function coordinateModalController($scope, $uibModalInstance) {
        var vm = this;
        vm.map = { center: { latitude: 45, longitude: -73 }, zoom: 8 };
        vm.ok = function() {
            $uibModalInstance.close(vm.map);
        };

        vm.cancel = function() {
            $uibModalInstance.dismiss('cancel');
        };

    }

})();
