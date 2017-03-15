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
    var factoryId = "modalFactory";
    app.factory(factoryId, [ '$uibModal', modalFactory]);

    function modalFactory($uibModal) {
        
        var modalFactory = {
            openCoordinateModal: openCoordinateModal

        };
        return modalFactory;

        function openCoordinateModal(callbackFun){
            var modalInstance = $uibModal.open({
                animation: true,
                ariaLabelledBy: 'modal-title',
                ariaDescribedBy: 'modal-body',
                templateUrl: 'ngviews/components/coordinate-modal/coordinate-modal',
                controller: 'lio.controllers.coordinate-modal',
                controllerAs: 'mc',
                size: 'lg',
                
            });

            modalInstance.result.then(callbackFun(), function() {
                console.log('Modal dismissed at: ' + new Date());
            });
        }

      
    }

})();
