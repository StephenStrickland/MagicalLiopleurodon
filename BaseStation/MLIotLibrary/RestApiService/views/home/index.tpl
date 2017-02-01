<!doctype html>
<html class="no-js">
  <head>
    <meta charset="utf-8">
    <title></title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width">
    <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
    <!-- build:css(.) styles/vendor.css -->
    <!-- bower:css -->
    <link rel="stylesheet" href="libs/bootstrap/css/bootstrap.min.css" />
     <link rel="stylesheet" type="text/css" href="/css/style.css">
    <!-- endbower -->
    <!-- endbuild -->

    <!-- build:css(.tmp) styles/main.css -->
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/sb-admin-2.css">
    <link rel="stylesheet" href="css/timeline.css">
    <link rel="stylesheet" href="bower_components/metisMenu/dist/metisMenu.min.css">
    <link rel="stylesheet" href="bower_components/angular-loading-bar/build/loading-bar.min.css">
    <link rel="stylesheet" href="bower_components/font-awesome/css/font-awesome.min.css" type="text/css">
    <!-- endbuild -->

    <!-- build:js(.) scripts/vendor.js -->
    <!-- bower:js -->
    <script src="libs/jquery.min.js"></script>
    <script src="libs/angular/angular.min.js"></script>
    <script src="libs/bootstrap/js/bootstrap.min.js"></script>
    <script src="libs/angular-ui-router.min.js"></script>
    <script src="bower_components/json3/lib/json3.min.js"></script>
    <script src="bower_components/oclazyload/dist/ocLazyLoad.min.js"></script>
    <script src="bower_components/angular-loading-bar/build/loading-bar.min.js"></script>
    <script src="bower_components/angular-bootstrap/ui-bootstrap-tpls.min.js"></script>
    <script src="bower_components/metisMenu/dist/metisMenu.min.js"></script>
    <script src="bower_components/Chart.js/Chart.min.js"></script>
    <!-- endbower -->
    <!-- endbuild -->

    <!-- build:js({.tmp,app}) scripts/scripts.js -->

        <script src="js/sb-admin-2.js"></script>
    <!-- endbuild -->



    <script>
       (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
       (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
       m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
       })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
       ga('create', 'UA-XXXXX-X');
       ga('send', 'pageview');
    </script>
    <!-- Custom CSS -->

    <!-- Custom Fonts -->

    <!-- Morris Charts CSS -->
    <!-- <link href="styles/morrisjs/morris.css" rel="stylesheet"> -->


    </head>

    <body>

    <div ng-app="sbAdminApp">

        <div ui-view></div>

    </div>

    </body>

     % for script in scripts:
    <script  type="text/javascript" src="{{script}}"></script>
     % end

</html>