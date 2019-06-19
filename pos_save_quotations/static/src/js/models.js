odoo.define('pos_save_quotations_model', function (require) {
    var models = require('point_of_sale.models');
    var rpc = require('web.rpc');
    var core = require('web.core');
    var _t = core._t;
    models.load_models([
        {
            model: 'pos.shop',
            fields: [],
            loaded: function (self, shops) {
                self.shops = shops;
            },
        }
    ]);

    var _super_posmodel = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({
        _save_to_server: function (orders, options) {
            var res = _super_posmodel._save_to_server.apply(this, arguments);
            for (var i = 0; i < orders.length; i++) {
                var order = orders[i];
                if (order.data.quotation_name) {
                    var quotation_name = order.data.quotation_name;
                    var quotation = this.db.quotations.find(function (quotation) {
                        return quotation.name = quotation_name;
                    })
                    var quotations = [];
                    if (quotation) {
                        for (var x = 0; x < this.db.quotations.length; x++) {
                            if (this.db.quotations[x].name != quotation.name) {
                                quotations.push(this.db.quotations[x]);
                            }
                        }
                    }
                    this.db.quotations = quotations;
                }
            }
            return res;
        },

        get_order_by_uid: function (uid) {
            var orders = this.get('orders').models;
            var order = orders.find(function (order) {
                return order.uid == uid;
            });
            return order;
        },
        // load_new_product_by_id: function (product_id) {
        //     var self = this;
        //     var def = new $.Deferred();
        //     var fields = _.find(this.models, function (model) {
        //         return model.model === 'product.product';
        //     }).fields;
        //     new Model('product.product')
        //         .query(fields)
        //         .filter([['id', '=', product_id]])
        //         .all({'timeout': 3000, 'shadow': true})
        //         .then(function (products) {
        //             self.db.add_products(products[0]);
        //         }, function (err, event) {
        //             event.preventDefault();
        //             def.reject();
        //         });
        //     return def;
        // },
        // load_new_partners_by_id: function (partner_id) {
        //     var self = this;
        //     var def = new $.Deferred();
        //     var fields = _.find(this.models, function (model) {
        //         return model.model === 'res.partner';
        //     }).fields;
        //     new Model('res.partner')
        //         .query(fields)
        //         .filter([['id', '=', partner_id]])
        //         .all({'timeout': 3000, 'shadow': true})
        //         .then(function (partners) {
        //             if (self.db.add_partners(partners)) {
        //                 def.resolve();
        //             } else {
        //                 def.reject();
        //             }
        //         }, function (err, event) {
        //             event.preventDefault();
        //             def.reject();
        //         });
        //     return def;
        // },
    });

    var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
        initialize: function (attributes, options) {
            var self = this;
            var res = _super_order.initialize.apply(this, arguments);
            if (!this.order_time) {
                this.order_time = new Date().toLocaleTimeString();
            }
            setInterval(function () {
                self.get_quotations();
            }, 20000);
            return res;
        },
        get_quotations: function () {
            var self = this;
            if (this.pos && this.pos.config && this.pos.config.allow_load_data == true) {
                var records = rpc.query({
                    model: 'pos.quotation',
                    method: 'get_quotations',
                    args: [this.pos.config.shop_id[0]],
                });
                records.then(function (quotations) {
                    self.pos.db.add_quotations(quotations);
                    self.pos.trigger('update:quotation-screen');
                })
            }
        },
        save_quotation: function (order_json) {
            var self = this;
            var records = rpc.query({
                model: 'pos.quotation',
                method: 'save_quotation',
                args: [order_json],
            });
            records.then(function (result) {
                if (self.pos.config.delete_after_save == true) {
                    self.destroy({'reason': 'abandon'});
                }
            }).fail(function (error, event) {
                if (error.code === -32098) {
                    self.pos.gui.show_popup('error', {
                        'title': _t("Warning"),
                        'body': _t("your internet have problem, please checking"),
                    });
                    event.preventDefault();
                }
                if (error.code == 200) {
                    self.pos.gui.show_popup('error', {
                        'title': _t("Warning"),
                        'body': _t(error.data.message),
                    });
                    event.preventDefault();
                }
            });
        },
        init_from_JSON: function (json) {
            var res = _super_order.init_from_JSON.apply(this, arguments);
            this.uid = json.uid;
            this.order_time = json.order_time;
            if (json.quotation_name) {
                this.quotation_name = json.quotation_name;
            }
            if (json.note) {
                this.note = json.note;
            }
            return res;
        },
        export_as_JSON: function () {
            var json = _super_order.export_as_JSON.apply(this, arguments);
            json.uid = this.uid;
            json.order_time = this.order_time;
            if (this.quotation_name) {
                json.quotation_name = this.quotation_name;
            }
            if (this.note) {
                json.note = this.note;
            }
            return json;
        },
    });

    // var _super_order_line = models.Orderline.prototype;
    // models.Orderline = models.Orderline.extend({
    //     initialize: function (attr, options) {
    //         var res = _super_order_line.initialize.apply(this, arguments);
    //         if (!this.uid) {
    //             this.uid = this.order.uid + '-' + this.pos.config.id + '-' + this.id;
    //         }
    //         this.order_uid = this.order.uid;
    //         return res;
    //     },
    //     init_from_JSON: function (json) {
    //         var res = _super_order_line.init_from_JSON.apply(this, arguments);
    //         this.uid = json.uid;
    //         return res;
    //     },
    //     export_as_JSON: function () {
    //         var json = _super_order_line.export_as_JSON.apply(this, arguments);
    //         json.uid = this.uid;
    //         json.order_uid = this.order.uid;
    //         return json;
    //     }
    // });

});
