angular.module("EditRecordApp", [])
  .controller("EditRecordController", function($scope) {
    $scope.page = 'list';

    $scope.records = get_data();

    $scope.edit = function(idx) {
        $scope.stash = {
            'name' : $scope.records[ idx ].name
        };
        $scope.current_record = idx;
		$scope.editor = $scope.records[ idx ];
        $scope.page = 'editor'
    }

    $scope.cancel = function() {
        $scope.records[ $scope.current_record ].name = $scope.stash.name;
        $scope.page = 'list';
    }

    $scope.save = function() {
        $scope.page = 'list';
    }
    
});

var get_data = function() {
   return [
      {
        'name' : 'Foo'
      },
      {
        'name' : 'Bar'
      },
      {
        'name' : 'Qux'
      }
   ];
}

