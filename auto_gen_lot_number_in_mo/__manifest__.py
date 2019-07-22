{
    "name": "Auto Generate Lot Number in Manufacturing",
    "version": "12.0.16.5",
    "category": "Manufacturing",
    "summary": """
	Auto generate Lot no in Manufacturing when we have Produce Manufacturing Order lot no generate based on production Date/Today Date.
	""",
    "author": 'Vraja Technologies',
    'price': 18,
    'currency': 'EUR',
    "depends": ['mrp','stock'],
    "data": [
        'wizard/res_config.xml',
    ],
    'qweb': [],
    'css': [],
    'js': [],
    'images': [
        'static/description/auto_generate_mo.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
