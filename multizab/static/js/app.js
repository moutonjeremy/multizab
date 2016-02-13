var app = angular.module('multiZab', ['angularMoment', 'chart.js'])

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

app.controller('AlertsListCtrl', function ($scope, $http, $q, $interval){
    this.loadNotifications = function (){
        var deferred = $q.defer()
        $http.get('api/alerts')
            .success(function (data, status) {
                deferred.resolve(data);
            }).error(function (data, status){
                deferred.reject('Error');
            });
            deferred.promise.then(function(results){
                $scope.results = results;
            })
    }

    $interval(function(){
       this.loadNotifications();
    }.bind(this), 10000);

    this.loadNotifications();

})

app.controller('CountPerZabbixCtrl', function ($scope, $http, $q, $interval){
    this.loadNotifications = function (){
        var deferred = $q.defer()
        $http.get('api/count/alerts')
            .success(function (data, status) {
                deferred.resolve(data);
            }).error(function (data, status){
                deferred.reject('Error');
            });
            deferred.promise.then(function(results){
                $scope.results = results.result;
                $scope.labels = []
                $scope.data = []
                angular.forEach($scope.results, function(value, key){
                    $scope.labels.push(key)
                    $scope.data.push(value)
                })
            })
    }

    $interval(function(){
       this.loadNotifications();
    }.bind(this), 10000);

    this.loadNotifications();
})

app.controller('CountPerTypeCtrl', function ($scope, $http, $q, $interval){
    this.loadNotifications = function (){
        var deferred = $q.defer()
        $http.get('api/count/types')
            .success(function (data, status) {
                deferred.resolve(data);
            }).error(function (data, status){
                deferred.reject('Error');
            });
            deferred.promise.then(function(results){
                $scope.results = results.result;
                $scope.labels = []
                $scope.data = []
                angular.forEach($scope.results, function(value, key){
                    $scope.labels.push(key)
                    $scope.data.push(value)
                })
            })
    }

    $interval(function(){
       this.loadNotifications();
    }.bind(this), 10000);

    this.loadNotifications();
})

app.controller('ZabbixListCtrl', function ($scope, $http, $q, $interval){
    this.loadNotifications = function (){
        var deferred = $q.defer()
        $http.get('api/list/zabbix')
            .success(function (data, status) {
                deferred.resolve(data);
            }).error(function (data, status){
                deferred.reject('Error');
            });
            deferred.promise.then(function(results){
                $scope.results = results;
            })
    }

    $interval(function(){
       this.loadNotifications();
    }.bind(this), 20000);

    this.loadNotifications();

})

app.controller('CountPerTypesZabbixCtrl', function ($scope, $http, $q, $interval){
    $scope.init = function(id) {
        $scope.id = id;
    }
    this.loadNotifications = function (){
        var deferred = $q.defer()
        $http.get('api/count/types/'+$scope.id)
            .success(function (data, status) {
                deferred.resolve(data);
            }).error(function (data, status){
                deferred.reject('Error');
            });
            deferred.promise.then(function(results){
                $scope.results = results.result;
                $scope.labels = []
                $scope.data = []
                angular.forEach($scope.results, function(value, key){
                    $scope.labels.push(key)
                    $scope.data.push(value)
                })
            })
    }

    $interval(function(){
       this.loadNotifications();
    }.bind(this), 10000);

    this.loadNotifications();
})