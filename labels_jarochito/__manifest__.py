# -*- coding: utf-8 -*-
{
    'name': "labels_jarochito",

    'summary': """
        Crea etiquetas para tarimas""",

    'description': """
        Creación de etiquetas para tarimas, con datos como turno, fecha y tarima a seleccionar.
    """,

    'author': "Xmarts",
    'Collaborator' : "Marco Aguilar",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/layout.xml',
        'reports/print_pallets.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable' : True,
    'application' : True
}