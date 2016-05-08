angular.module("EditRecordApp", [])
  .controller("EditRecordController", function($scope) {
    $scope.page = 'list';
 
    $scope.records = get_data();
	$scope.values = get_values();
 
    $scope.edit = function(idx) {
        $scope.editor = angular.copy($scope.records[ idx ]);
        $scope.current_record = idx;
        $scope.page = 'editor'
    }
 
    $scope.cancel = function() {
        $scope.editor = null;
        $scope.page = 'list';
    }
 
    $scope.save = function() {
        $scope.records[ $scope.current_record ] = angular.copy($scope.editor);
        $scope.editor = null;
        $scope.page = 'list';
    }
    
});
 
var get_data = function() {
   return [
      {
        'name' : 'Foo'
      },
      {
        'name' : 'Bar',
        'planet' : {
            'id' : 1
        }
      },
      {
        'name' : 'Qux',
        'planet': {
            'name': 'Venus'
        }
      },
      {
        'name' : 'ET',
        'planet': 'Mars'
      }
   ];
};

var get_values = function() {
	return [
		{
			'id' : 1,
			'name' : 'Mercury'
		},
		{
			'id' : 2,
			'name' : 'Venus'
		},
		{
			'id' : 3,
			'name' : 'Earth'
		},
	];
};
