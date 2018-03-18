angular.module("EditRecordApp", [])
  .controller("EditRecordController", function($scope) {
    $scope.page = 'list';
 
    $scope.records = get_data();
	$scope.values = get_values();
 
    $scope.edit = function(idx) {
        $scope.editor = angular.copy($scope.records[ idx ]);
        $scope.current_record = idx;
        $scope.page = 'editor'
    };
 
    $scope.cancel = function() {
        $scope.page = 'list';
    };

	$scope.delete_planet = function(idx) {
        $scope.editor.planets.splice(idx, 1);
	};
	$scope.add_planet = function() {
		console.log(angular.copy($scope.editor.planets));
        $scope.editor.planets.push( { 'id' : 0 } );
		console.log($scope.editor.planets);
    };
 
    $scope.save = function() {
		$scope.editor.planets =  $scope.editor.planets.filter( function(v) { return v.id });
        $scope.records[ $scope.current_record ] = angular.copy($scope.editor);
        $scope.page = 'list';
    };
    
});
 
var get_data = function() {
   return [
      {
        'name' : 'Foo'
      },
      {
        'name' : 'Bar',
        'planets' : [
           {
            'id' : 1
           }
         ]
      },
      {
        'name' : 'Qux',
        'planets': [
           {
             'id' : 2
           },
           {
             'id' : 1
           }

        ]
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
