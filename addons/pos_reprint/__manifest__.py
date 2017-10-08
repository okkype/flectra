# -*- coding: utf-8 -*-
# Part of Odoo,Flectra. See LICENSE file for full copyright and licensing details.

{
    'name': 'Point of Sale Receipt Reprinting',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Allow cashier to reprint receipts',
    'description': """

Allow cashier to reprint receipts

""",
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_reprint_templates.xml',
        'views/pos_config_views.xml'
    ],
    'qweb': [
        'static/src/xml/reprint.xml',
    ],
    'installable': True,
    'website': 'https://www.flectrahq.com/page/point-of-sale',
}
