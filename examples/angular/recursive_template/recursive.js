angular.module('DemoApp', [])
.controller('DemoController', function($scope, $log) {
    $scope.tree = [
        {
            title: "Level 1",
            tree: [
                {
                    title: "Level 2",
                    tree: [
                        {
                            title: "Level 3"
                        }
                    ]
                }
            ]
        }
    ];
});
