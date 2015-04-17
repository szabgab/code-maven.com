function HelloWorldController() {
    this.message = "Hello Angular World";
};

angular.module('hw', []);
angular.module('hw').config(['$controllerProvider', function($controllerProvider) {
  $controllerProvider.allowGlobals();
}]);

