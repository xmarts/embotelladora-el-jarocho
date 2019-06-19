{
    'name': "POS Save Quotations",
    'live_test_url': 'http://posodoo.com/web/signup',
    'version': '3.1',
    'category': 'Point of Sale',
    'author': 'TL Technology',
    'sequence': 0,
    'summary': 'POS Save Quotations',
    'description': """
    POS Save Quotations
    ....
    """,
    'depends': ['point_of_sale', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'datas/ir_sequence.xml',
        'datas/email_template.xml',
        '__import__/template.xml',
        'views/pos_quotation.xml',
        'views/pos_shop.xml',
        'views/pos_order.xml',
        'views/pos_config.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml'
    ],
    'demo': ['demo/pos_shop.xml'],
    'price': '50',
    'website': 'http://posodoo.com',
    "currency": 'EUR',
    'application': True,
    'images': ['static/description/icon.png'],
    'support': 'thanhchatvn@gmail.com'
}
