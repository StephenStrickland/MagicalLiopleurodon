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
    var directiveId = "coordinateModal";
    app.controller(directiveId, ['$scope', '$uibModal', 'nodeFactory', coordinateModalDirective]);

    function coordinateModalDirective($scope, $uibModal, nodeFactory) {
        function link(scope, elem, attrs) {

            scope.$watch('trigger', function(newVal){
                newVal = !newVal;
                var modalInstance = $uibModal.open({
                animation: $ctrl.animationsEnabled,
                ariaLabelledBy: 'modal-title',
                ariaDescribedBy: 'modal-body',
                templateUrl: 'ngviews/components/coordinate-modal/coordinate-modal',
                controller: 'lio.controllers.coordinate-modal',
                controllerAs: 'mc',
                size: 'lg',
                resolve: {
                    items: function() {
                        return $ctrl.items;
                    }
                }
            });

            modalInstance.result.then(function(coord) {
                scope.coordinates = coord;
            }, function() {
                console.log('Modal dismissed at: ' + new Date());
            });


            });

            

        }


        return {
            restrict: 'E',
            scope: {
                coordinates: '=',
                trigger: '='
            },
            link: link,
            transclude: false


        };

    }

})();
