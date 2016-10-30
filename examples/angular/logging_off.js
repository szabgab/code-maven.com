angular.module('DemoApp', [])
.config(['$logProvider', function($logProvider) {
    $logProvider.debugEnabled(false); // turns off the calls to $log.debug, but not the others
}])
.controller('DemoController', ['$log', function($log) {
    console.debug("Calling console.debug");
    console.info("Calling console.info");
    console.log("Calling console.log");
    console.warn("Calling console.warn");
    console.error("Calling console.error");

    $log.debug("Some debug");
    $log.info("Some info");
    $log.log("Some log");
    $log.warn("Some warning");
    $log.error("Some error");
}]);
