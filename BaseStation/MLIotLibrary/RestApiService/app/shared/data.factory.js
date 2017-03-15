(function (s) {
    "use strict";

    var app = s.angular.module("lio");
    app.factory("data", ["$http", "$q", "$window",
        function ($http, $q, $window) {

            var createResult = function (args) {
                var data = args[0];
                return {
                    data: data,
                    status: args[1],
                    headers: args[2],
                    config: args[3],
                    isCollection: _.isArray(data),
                    itemCount: ((_.isArray(data)) ? data.length : 1)
                };
            };

            var checkStatus = function(status) {
                if (status == 401)
                    $window.location.href = "/login";
            };


            var data = {
                get: function (url) {
                   // $logging.log("requesting data from '" + url + "'");
                    var deferred = $q.defer(),
                        onSuccess,
                        onError,
                        onFinally;
                    deferred.promise.success = function (callback) {
                        onSuccess = callback;
                        return deferred.promise;
                    };
                    deferred.promise.error = function (callback) {
                        onError = callback;
                        return deferred.promise;
                    };
                    deferred.promise.finally = function (callback) {
                        onFinally = callback;
                        return deferred.promise;
                    };
                    $http({ method: "GET", url: url })
                        .then(function (response, status, headers, config) {
                            checkStatus(status);
                            var result = createResult(arguments);
                            switch (typeof (result.data)) {
                                case "string":
                                    if (result.data.indexOf("<form action=\"/Account/Login") > -1) {
                                        sessionTimeout("GET", "returned the login form", url, result);
                                    } else {
                                       // $logging.log(result, "HTTP/GET request to '" + url + "' return unexpected results");
                                        onError(result);
                                        deferred.reject(result);
                                    }
                                    break;
                                case "object":
                                    onSuccess(result);
                                    deferred.resolve(result);
                                    break;
                                default:
                                   // $logging.log(result, "HTTP/GET request to '" + url + "' return unexpected results");
                                    onError(result);
                                    deferred.reject(result);
                                    break;
                            }
                            if (typeof onFinally === "function") onFinally();
                        }, function (response, status, headers, config) {
                            checkStatus(status);
                            var result = createResult(arguments);
                            if (_.has(result.data, "ClassName") && result.data.ClassName.indexOf("EmptySessionException") > -1) {
                                sessionTimeout("GET", "indicated an invalid session", url, result);
                            }
                            else if (_.has(result.data, "exceptionType") && result.data.exceptionType.indexOf("System.InvalidOperationException") > -1) {
                                sessionTimeout("GET", "indicated an invalid session", url, result);
                            }
                            else {
                               // $logging.log(result, "HTTP/GET request to '" + url + "' returned an error");
                                onError(result);
                                deferred.reject(result);
                            }
                            if (typeof onFinally === "function") onFinally();
                        });
                    return deferred.promise;
                },

                post: function (url, data) {
                   // $logging.log("requesting data from '" + url + "'");
                    var deferred = $q.defer(),
                        onSuccess,
                        onError,
                        onFinally;
                    deferred.promise.success = function (callback) {
                        onSuccess = callback;
                        return deferred.promise;
                    };
                    deferred.promise.error = function (callback) {
                        onError = callback;
                        return deferred.promise;
                    };
                    deferred.promise.finally = function (callback) {
                        onFinally = callback;
                        return deferred.promise;
                    };
                    $http({ method: "POST", url: url, data: data })
                        .then(function (response, status, headers, config) {
                            checkStatus(status);
                            var result = createResult(arguments);
                            switch (typeof (result.data)) {
                                case "string":
                                    if (result.data.indexOf("<form action=\"/Account/Login") > -1) {
                                        sessionTimeout("GET", "returned the login form", url, result);
                                    } else {
                                        //  $logging.log(result, "HTTP/GET request to '" + url + "' return unexpected results");
                                        onSuccess(result);
                                        deferred.resolve(result);
                                    }
                                    break;
                                case "object":
                                    onSuccess(result);
                                    deferred.resolve(result);
                                    break;
                                default:
                                    // $logging.log(result, "HTTP/GET request to '" + url + "' return unexpected results");
                                    onError(result);
                                    deferred.reject(result);
                                    break;
                            }
                            if (typeof onFinally === "function") onFinally();
                        }, function (response, status, headers, config) {
                            checkStatus(status);
                            var result = createResult(arguments);
                            if (_.has(result.data, "ClassName") && result.data.ClassName.indexOf("EmptySessionException") > -1) {
                                sessionTimeout("GET", "indicated an invalid session", url, result);
                            }
                            else if (_.has(result.data, "exceptionType") && result.data.exceptionType.indexOf("System.InvalidOperationException") > -1) {
                                sessionTimeout("GET", "indicated an invalid session", url, result);
                            }
                            else {
                                // $logging.log(result, "HTTP/GET request to '" + url + "' returned an error");
                                onError(result);
                                deferred.reject(result);
                            }
                            if (typeof onFinally === "function") onFinally();
                        });
                    return deferred.promise;
                },
                put: function (url, data) {
                   // $logging.log("requesting data from '" + url + "'");
                    var deferred = $q.defer(),
                        onSuccess,
                        onError,
                        onFinally;
                    deferred.promise.success = function (callback) {
                        onSuccess = callback;
                        return deferred.promise;
                    };
                    deferred.promise.error = function (callback) {
                        onError = callback;
                        return deferred.promise;
                    };
                    deferred.promise.finally = function (callback) {
                        onFinally = callback;
                        return deferred.promise;
                    };
                    $http({ method: "PUT", url: url, data: data })
                        .then(function (response, status, headers, config) {
                            checkStatus(status);
                            var result = createResult(arguments);
                            switch (typeof (result.data)) {
                                case "string":
                                    if (result.data.indexOf("<form action=\"/Account/Login") > -1) {
                                        sessionTimeout("GET", "returned the login form", url, result);
                                    } else {
                                        //  $logging.log(result, "HTTP/GET request to '" + url + "' return unexpected results");
                                        onSuccess(result);
                                        deferred.resolve(result);
                                    }
                                    break;
                                case "object":
                                    onSuccess(result);
                                    deferred.resolve(result);
                                    break;
                                default:
                                    // $logging.log(result, "HTTP/GET request to '" + url + "' return unexpected results");
                                    onError(result);
                                    deferred.reject(result);
                                    break;
                            }
                            if (typeof onFinally === "function") onFinally();
                        }, function (response, status, headers, config) {
                            checkStatus(status);
                            var result = createResult(arguments);
                            if (_.has(result.data, "ClassName") && result.data.ClassName.indexOf("EmptySessionException") > -1) {
                                sessionTimeout("GET", "indicated an invalid session", url, result);
                            }
                            else if (_.has(result.data, "exceptionType") && result.data.exceptionType.indexOf("System.InvalidOperationException") > -1) {
                                sessionTimeout("GET", "indicated an invalid session", url, result);
                            }
                            else {
                                // $logging.log(result, "HTTP/GET request to '" + url + "' returned an error");
                                onError(result);
                                deferred.reject(result);
                            }
                            if (typeof onFinally === "function") onFinally();
                        });
                    return deferred.promise;
                },
                save: function (url, data) {
                    // $logging.log("posting data to '" + url + "'");
                    var deferred = $q.defer(),
                        onSuccess,
                        onError,
                        onFinally;
                    deferred.promise.success = function (callback) {
                        onSuccess = callback;
                        return deferred.promise;
                    };
                    deferred.promise.error = function (callback) {
                        onError = callback;
                        return deferred.promise;
                    };
                    deferred.promise.finally = function (callback) {
                        onFinally = callback;
                        return deferred.promise;
                    };
                    $http.post(url, data)
                        .then(function (data, status, headers, config) {
                            checkStatus(status);
                            var result = createResult(arguments);
                            switch (typeof (result.data)) {
                                case "string":
                                    if (result.data.indexOf("<form action=\"/Account/Login") > -1) {
                                        sessionTimeout("POST", "returned the login form", url, result);
                                    } else {
                                        // $logging.log(result, "HTTP/POST request to '" + url + "' return unexpected results");
                                        onError(result);
                                        deferred.reject(result);
                                    }
                                    break;
                                case "object":
                                    onSuccess(result);
                                    deferred.resolve(result);
                                    break;
                                default:
                                    // $logging.log(result, "HTTP/POST request to '" + url + "' return unexpected results");
                                    onError(result);
                                    deferred.reject(result);
                                    break;
                            }
                            if (typeof onFinally === "function") onFinally();
                        }, function (data, status, headers, config) {
                            checkStatus(status);
                            var result = createResult(arguments);
                            switch (result.status) {
                                case 302:
                                    sessionTimeout("POST", "prompted a redirect", url, result);
                                    break;
                                default:
                                    //$logging.log(result, "HTTP/POST request to '" + url + "' returned an error");
                                    onError(result);
                                    deferred.reject(result);
                                    break;
                            }
                            if (typeof onFinally === "function") onFinally();
                        });
                    return deferred.promise;
                },
                "delete": function (url, data) {
                    //$logging.log("sending delete request to '" + url + "'");
                    var deferred = $q.defer(),
                        onSuccess,
                        onError,
                        onFinally;
                    deferred.promise.success = function (callback) {
                        onSuccess = callback;
                        return deferred.promise;
                    };
                    deferred.promise.error = function (callback) {
                        onError = callback;
                        return deferred.promise;
                    };
                    deferred.promise.finally = function (callback) {
                        onFinally = callback;
                        return deferred.promise;
                    };
                    $http.delete(url, data)
                        .then(function (data, status, headers, config) {
                            checkStatus(status);
                            var result = createResult(arguments);
                            switch (typeof (result.data)) {
                                case "string":
                                    if (result.data.indexOf("<form action=\"/Account/Login") > -1) {
                                        sessionTimeout("DELETE", "returned the login form", url, result);
                                    } else {
                                        // $logging.log(result, "HTTP/DELETE request to '" + url + "' return unexpected results");
                                        onError(result);
                                        deferred.reject(result);
                                    }
                                    break;
                                case "object":
                                    onSuccess(result);
                                    deferred.resolve(result);
                                    break;
                                default:
                                    // $logging.log(result, "HTTP/DELETE request to '" + url + "' return unexpected results");
                                    onError(result);
                                    deferred.reject(result);
                                    break;
                            }
                            if (typeof onFinally === "function") onFinally();
                        }, function (data, status, headers, config) {
                            checkStatus(status);
                            var result = createResult(arguments);
                            switch (result.status) {
                                case 302:
                                    sessionTimeout("DELETE", "promted a redirect", url, result);
                                    break;
                                default:
                                    // $logging.log(result, "HTTP/DELETE request to '" + url + "' returned an error");
                                    onError(result);
                                    deferred.reject(result);
                                    break;
                            }
                            if (typeof onFinally === "function") onFinally();
                        });
                    return deferred.promise;
                }

            }

            return data;
        }
    ]);
})(window || scope);