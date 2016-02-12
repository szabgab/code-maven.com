angular.module("EditRecordApp", [])
  .controller("EditRecordController", function($scope) {
    $scope.page = 'list';

    $scope.records = get_data();

    $scope.edit = function(idx) {
        $scope.editor = {
            'name' : $scope.records[ idx ].name
        };
        $scope.current_record = idx;
        $scope.page = 'editor'
    }

    $scope.cancel = function() {
        $scope.page = 'list';
    }

    $scope.save = function() {
        $scope.records[ $scope.current_record ].name = $scope.editor.name;
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

