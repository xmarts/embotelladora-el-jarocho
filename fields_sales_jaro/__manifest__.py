# -*- coding: utf-8 -*-
{
    'name': "fields_sales_jaro",

    'summary': """
        Añade campos en otra información""",

    'description': """
        Añade campos de numero de orden, numero de cita y fecha de entrega.
    """,

    'author': "Xmarts",
    'Collaborator' : "Marco Aguilar",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/fields_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
    'installable' : True
} 