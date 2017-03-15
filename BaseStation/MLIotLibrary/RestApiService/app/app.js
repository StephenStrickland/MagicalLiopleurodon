'use strict';
/**
 * @ngdoc overview
 * @name sbAdminApp
 * @description
 * # sbAdminApp
 *
 * Main module of the application.
 */
angular
  .module('lio', [
    'oc.lazyLoad',
    'ui.router',
    'ui.bootstrap',
    'angular-loading-bar',
  ])
  .config(['$stateProvider','$urlRouterProvider','$ocLazyLoadProvider',function ($stateProvider,$urlRouterProvider,$ocLazyLoadProvider) {
    
    $ocLazyLoadProvider.config({
      debug:false,
      events:true
    });

    $urlRouterProvider.otherwise('/dashboard/home');

    $stateProvider
      .state('dashboard', {
        url:'/dashboard',
        templateUrl: 'ngviews/components/dashboard/main',
        resolve: {
            loadMyDirectives:function($ocLazyLoad){
                return $ocLazyLoad.load(
                {
                    name:'lio',
                    files:[
                    'ngscripts/shared/header/header.js',
                    'ngscripts/shared/header/header-notification/header-notification.js',
                    'ngscripts/shared/nav/sidebar.js',
                    'ngscripts/shared/nav/sidebar-search/sidebar-search.js',
                    'ngscripts/shared/data.factory.js',
                    'ngscripts/shared/modal.factory.js'
                    ]
                }),
                $ocLazyLoad.load(
                {
                   name:'toggle-switch',
                   files:["libs/angular-toggle-switch/angular-toggle-switch.min.js",
                          "libs/angular-toggle-switch/angular-toggle-switch.css"
                      ]
                }),
                $ocLazyLoad.load(
                {
                  name:'ngAnimate',
                  files:['libs/angular-animate/angular-animate.js']
                })
                $ocLazyLoad.load(
                {
                  name:'ngCookies',
                  files:['libs/angular-cookies/angular-cookies.js']
                })
                $ocLazyLoad.load(
                {
                  name:'ngResource',
                  files:['libs/angular-resource/angular-resource.js']
                })
                $ocLazyLoad.load(
                {
                  name:'ngSanitize',
                  files:['libs/angular-sanitize/angular-sanitize.js']
                })
                $ocLazyLoad.load(
                {
                  name:'ngTouch',
                  files:['libs/angular-touch/angular-touch.js']
                })
            }
        }
    })
      .state('dashboard.home',{
        url:'/home',
        controller: 'MainCtrl',
        templateUrl:'ngviews/components/dashboard/home',
        resolve: {
          loadMyFiles:function($ocLazyLoad) {
            return $ocLazyLoad.load({
              name:'lio',
              files:[
              'ngscripts/components/main.js',
              'ngscripts/shared/timeline/timeline.js',
              'ngscripts/shared/notifications/notifications.js',
              'ngscripts/shared/chat/chat.js',
              'ngscripts/components/dashboard/stats/stats.js'
              ]
            })
          }
        }
      })
      .state('dashboard.form',{
        templateUrl:'ngviews/components/form',
        url:'/form'
    })
      .state('dashboard.blank',{
        templateUrl:'ngviews/components/blank',
        url:'/blank'
    })
      .state('login',{
        templateUrl:'ngviews/components/pages/login',
        url:'/login'
    })
      .state('dashboard.nodes-list',{
        templateUrl:'ngviews/components/nodes/node.list',
        url:'/nodes',
        controller: 'lio.controllers.node.list as vm',
        
        resolve: {
          loadMyFiles:function($ocLazyLoad) {
            return $ocLazyLoad.load({
              name:'lio',
              files:[
              'ngscripts/components/nodes/node.factory.js',
              'ngscripts/components/nodes/node.list.ctl.js'

              ],
              serie: true
            })
          }
        }
    })
      .state('dashboard.nodes-edit',{
        templateUrl:'ngviews/components/nodes/node.edit',
        url:'/:nodeId/edit',
        controller: 'lio.controllers.node.edit as vm',
        
        resolve: {
          loadMyFiles:function($ocLazyLoad) {
            return $ocLazyLoad.load({
              name:'lio',
              files:[
              'ngscripts/components/nodes/node.factory.js',
              'ngscripts/components/nodes/node.edit.ctl.js',
              'ngscripts/components/coordinate-modal/coordinate-modal.ctl.js'

              ],
              serie: true
            })
          }
        }
    })

      .state('dashboard.nodes.details',{
        templateUrl:'ngviews/components/nodes/node.details',
        url:'/nodes/:nodeId/details',
        controller: 'lio.controllers.node.list as vm',
        
        resolve: {
          loadMyFiles:function($ocLazyLoad) {
            return $ocLazyLoad.load({
              name:'lio',
              files:[
              'ngscripts/components/nodes/node.factory.js',
              'ngscripts/components/nodes/node.list.ctl.js'

              ],
              serie: true
            })
          }
        }
    })
       .state('dashboard.groups-list',{
        templateUrl:'ngviews/components/groups/group.list',
        url:'/groups',
        controller: 'lio.controllers.group.list as vm',
        
        resolve: {
          loadMyFiles:function($ocLazyLoad) {
            return $ocLazyLoad.load({
              name:'lio',
              files:[
              'ngscripts/components/groups/group.factory.js',
              'ngscripts/components/groups/node.list.ctl.js'

              ],
              serie: true
            })
          }
        }
    })
      .state('dashboard.chart',{
        templateUrl:'ngviews/components/chart',
        url:'/chart',
        controller:'ChartCtrl',
        resolve: {
          loadMyFile:function($ocLazyLoad) {
            return $ocLazyLoad.load({
              name:'chart.js',
              files:[
                'libs/angular-chart.js/dist/angular-chart.min.js',
                'libs/angular-chart.js/dist/angular-chart.css'
              ]
            }),
            $ocLazyLoad.load({
                name:'lio',
                files:['ngscripts/controllers/chartContoller.js']
            })
          }
        }
    })
      .state('dashboard.table',{
        templateUrl:'ngviews/components/table/table',
        url:'/table'
    })
      .state('dashboard.panels-wells',{
          templateUrl:'ngviews/components/ui-elements/panels-wells',
          url:'/panels-wells'
      })
      .state('dashboard.buttons',{
        templateUrl:'ngviews/components/ui-elements/buttons',
        url:'/buttons'
    })
      .state('dashboard.notifications',{
        templateUrl:'ngviews/components/ui-elements/notifications',
        url:'/notifications'
    })
      .state('dashboard.typography',{
       templateUrl:'ngviews/components/ui-elements/typography',
       url:'/typography'
   })
      .state('dashboard.icons',{
       templateUrl:'ngviews/components/ui-elements/icons',
       url:'/icons'
   })
      .state('dashboard.grid',{
       templateUrl:'ngviews/components/ui-elements/grid',
       url:'/grid'
   })
  }]);

    
