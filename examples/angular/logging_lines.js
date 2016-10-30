angular.module('DemoApp', [])
.controller('DemoController', ['$log', function($log) {
    $log.log = console.log.bind(console);
    $log.debug = console.debug.bind(console);

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
