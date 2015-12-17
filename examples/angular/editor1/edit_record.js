angular.module("EditRecordApp", [])
  .controller("EditRecordController", function($scope) {
    $scope.page = 'list';
    $scope.records = get_data();

    $scope.edit = function(record) {
        $scope.editor = record;
        $scope.page = 'editor'
    }

    $scope.cancel = function() {
        $scope.page = 'list';
    }

    $scope.save = function() {
        // TODO
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

