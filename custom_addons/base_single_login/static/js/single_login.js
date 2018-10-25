/**
 * Created by shalo_000 on 2018/10/25.
 */

// odoo.define('base_single_login', function (require) {
//     var web_menu = require("web_enterprise.Menu");
//     var session = require('web.session');
//     web_menu.include({
//         start: function (id) {
//                 var self = this;
//                 this._super.apply(this, arguments);
//                 this.rpc("/web/session/remove/", {session:session.session_id,uid:session.uid});
//             }
//     });
// });

odoo.define('base_single_login', function (require) {
"use strict";
    var ajax = require('web.ajax');
    var web_menu = require("web_enterprise.Menu");
    var session = require('web.session');
    var Model = require('web.DataModel');

    web_menu.include({

        start: function () {
                var self = this;
                this._super.apply(this, arguments);
                  var signin = new Model("base.config.settings");
                   signin.call("signin_login").then(function(result){
                    console.log(result)
                    if(result){
                        ajax.jsonRpc("/web/session/remove/",[],{session:session.session_id,uid:session.uid});
                        // .then(function (data) {
                        //     console.log(data)
                        //     if (data){
                        //          alert("您的账号已在异地登陆,另一账号即将下线");
                        //     }
                        //
                        //     });
                    }

                    return false;
                })

                return self;
        }
    });
});

