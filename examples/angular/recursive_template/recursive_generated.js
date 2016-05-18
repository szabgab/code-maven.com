angular.module('DemoApp', [])
.controller('DemoController', function($scope, $log) {
    var build_tree = function(depth) {
        $log.log('build_tree', depth);
        var leaf = [
                {
                    title: "Level " + depth
                }
            ]
        if (depth > 1) {
            leaf[0].tree = build_tree(depth-1);
        }
        return leaf;
    }

    $scope.tree = build_tree(10);
    $log.log($scope.tree);
});
