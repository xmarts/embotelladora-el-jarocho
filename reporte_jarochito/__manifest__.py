# -*- coding: utf-8 -*-
{
    'name': "reporte_jarochito",

    'summary': """
        Descripción del producto y tipo de tarifa""",

    'description': """
        Creación de campos para la descripción del producto y muestra el tipo de tarifa en la dirección de envío
    """,

    'author': "Xmarts, Colaborador : Marco Aguilar ",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales, Stock, Contacts',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','product','stock','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/add_menu_items.xml',
        #'views/fac_ieps.xml',
        'views/presup.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}