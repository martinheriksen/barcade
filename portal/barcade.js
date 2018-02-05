angular.module('barcade', ['ngRoute'])

.config(function($routeProvider) {
 	
  	$routeProvider
    	.when('/', {
      		controller:'ProgramListController as programList',
 	     	templateUrl:'portal/pages/programList.html'
   	 	})
    	.otherwise({
      		redirectTo:'/'
    	});
})


.controller('ProgramListController', function($scope, $http) {
	$scope.programs = []

	$http({
        url: "http://127.0.0.1:8081/programs",
        method: "GET",
        headers: {}
    }).then(function (response){
    	console.log('yes')
    	$scope.programs = response.data;

 	},function (error){

   });

})

