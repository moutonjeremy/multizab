var app = angular.module('multiZab', ['angularMoment', 'chart.js'])

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

app.factory('CacheFactory', function($cacheFactory){
    return $cacheFactory('alerts_cache')
})

app.controller('RefreshCacheCtrl', function($scope, $http, $q, $interval, CacheFactory){
    var deferred = $q.defer();
    $http.get('api/graphics')
        .success(function (data, status) {
            deferred.resolve(data);
        }).error(function (data, status) {
            deferred.reject('Error');
        });
    deferred.promise.then(function(result){
        angular.forEach(result.result, function(value, key){
            CacheFactory.put(key, value)
            })
    });
})

app.controller('CountAlertsCtrl', function($scope, $interval, CacheFactory){
    this.loadNotifications = function (){
        $scope.labels = []
        $scope.data = []
        angular.forEach(CacheFactory.get('count_alerts'), function(value, key){
            $scope.labels.push(key)
            $scope.data.push(value)
        })
    }

    $interval(function(){
        this.loadNotifications();
    }.bind(this), 100)

    this.loadNotifications();
})

app.controller('CountPerTypeCtrl', function ($scope, $interval, CacheFactory){
    this.loadNotifications = function (){
        $scope.labels = []
        $scope.data = []
        angular.forEach(CacheFactory.get('count_types'), function(value, key){
            $scope.labels.push(key)
            $scope.data.push(value)
        })
    }

    $interval(function(){
       this.loadNotifications();
    }.bind(this), 100);

    this.loadNotifications();
})

app.controller('CountPerTypesZabbixCtrl', function ($scope, $interval, CacheFactory){
    $scope.init = function(id) {
        $scope.id = id;
    }

    this.loadNotifications = function (){
        $scope.labels = []
        $scope.data = []
        angular.forEach(CacheFactory.get('count_types_per_zabbix')[$scope.id], function(value, key){
            $scope.labels.push(key)
            $scope.data.push(value)
        })
    }

    $interval(function(){
       this.loadNotifications();
    }.bind(this), 100);

    this.loadNotifications();
})