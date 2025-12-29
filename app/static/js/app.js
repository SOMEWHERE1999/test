(function () {
  'use strict';

  angular
    .module('todoApp', [])
    .controller('TodoController', ['$http', TodoController]);

  function TodoController($http) {
    var vm = this;
    vm.items = [];
    vm.newTitle = '';
    vm.statuses = window.initialStatuses || [];
    vm.errorMessage = '';
    vm.isUpdating = false;

    function wrapData(response) {
      return response && response.data && response.data.data ? response.data.data : [];
    }

    vm.loadItems = function () {
      $http.get('/api/todos/').then(function (response) {
        vm.items = wrapData(response);
      });
    };

    vm.addItem = function () {
      if (!vm.newTitle.trim()) {
        vm.errorMessage = '请输入任务标题';
        return;
      }
      vm.isUpdating = true;
      $http
        .post('/api/todos/', { title: vm.newTitle, status: vm.statuses[0] || 'TODO' })
        .then(function (response) {
          vm.items.unshift(wrapData(response));
          vm.newTitle = '';
          vm.errorMessage = '';
        })
        .catch(function (error) {
          vm.errorMessage = (error.data && error.data.message) || '添加失败';
        })
        .finally(function () {
          vm.isUpdating = false;
        });
    };

    vm.updateStatus = function (item) {
      vm.isUpdating = true;
      $http
        .patch('/api/todos/' + item.id, { status: item.status })
        .then(function (response) {
          angular.extend(item, wrapData(response));
        })
        .catch(function () {
          vm.errorMessage = '更新状态失败';
        })
        .finally(function () {
          vm.isUpdating = false;
        });
    };

    vm.updateTitle = function (item) {
      if (!item.title || !item.title.trim()) {
        vm.errorMessage = '标题不能为空';
        item.title = item.title || '';
        return;
      }
      vm.isUpdating = true;
      $http
        .patch('/api/todos/' + item.id, { title: item.title })
        .then(function (response) {
          angular.extend(item, wrapData(response));
          vm.errorMessage = '';
        })
        .catch(function () {
          vm.errorMessage = '更新标题失败';
        })
        .finally(function () {
          vm.isUpdating = false;
        });
    };

    vm.removeItem = function (item) {
      vm.isUpdating = true;
      $http
        .delete('/api/todos/' + item.id)
        .then(function () {
          vm.items = vm.items.filter(function (row) {
            return row.id !== item.id;
          });
        })
        .catch(function () {
          vm.errorMessage = '删除失败';
        })
        .finally(function () {
          vm.isUpdating = false;
        });
    };

    vm.formatDate = function (value) {
      if (!value) return '';
      var date = new Date(value);
      return date.toLocaleString();
    };

    // init
    vm.loadItems();
  }
})();
