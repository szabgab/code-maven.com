angular.module('HelloUserApp', [])
      .controller('HelloUserController', function($scope) {
          $scope.NameChange = function () {
              $scope.greeting = "Hello " + $scope.name;
          };
      });
