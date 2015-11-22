      $scope.f = {};

      $scope.filter_by = function(field) {
        if ($scope.g[field] === '') {
             delete $scope.f['__' + field];
             return;
        }
        $scope.f['__' + field] = true;
        $scope.planets.forEach(function(v) { v['__' + field] = v[field] < $scope.g[field]; })
      }
 
