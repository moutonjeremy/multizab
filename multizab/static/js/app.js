var app = angular.module('multiZab', ['angularMoment', 'chart.js'])

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

app.factory('GetFactory', function($http, $q) {
    var factory = {
        result : false,
        getResult : function(path) {
            var deferred = $q.defer();
            $http.get(path)
                .success(function (data, status) {
                    factory.result = data;
                    deferred.resolve(factory.result);
                }).error(function (data, status) {
                    deferred.reject('Error');
                });
                return deferred.promise;
        }
    }
    return factory;
});

app.controller('AlertsListCtrl', function ($scope, $interval, GetFactory){
    this.loadNotifications = function (){
        GetFactory.getResult('api/alerts').then(function(result){
            $scope.results = result
        })
    }

    $interval(function(){
        this.loadNotifications();
    }.bind(this), 5000)

    this.loadNotifications();
})

app.controller('CountPerZabbixCtrl', function ($scope, $interval, GetFactory){
    this.loadNotifications = function (){
        GetFactory.getResult('api/count/alerts').then(function(result){
            $scope.results = result.result;
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

app.controller('CountPerTypeCtrl', function ($scope, $interval, GetFactory){
    this.loadNotifications = function (){
        GetFactory.getResult('api/count/types').then(function(result){
            $scope.results = result.result;
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

app.controller('ZabbixListCtrl', function ($scope, $interval, GetFactory){
    this.loadNotifications = function (){
        GetFactory.getResult('api/list/zabbix').then(function(result){
            $scope.results = result
        })
    }

    $interval(function(){
       this.loadNotifications();
    }.bind(this), 20000);

    this.loadNotifications();

})

app.controller('CountPerTypesZabbixCtrl', function ($scope, $interval, GetFactory){
    $scope.init = function(id) {
        $scope.id = id;
    }

    this.loadNotifications = function (){
        GetFactory.getResult('api/count/types/'+$scope.id).then(function(result){
            $scope.results = result.result;
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