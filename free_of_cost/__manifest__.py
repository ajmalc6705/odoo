# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Free of Cost  V14 for Sale and Purchase Order  ",
    "summary": "Free of Cost For  Sales and Purchase  ",
    "author": "Ajmal C",
    'email': 'ajmalc6705@gmail.com',
    "website": "",
    "category": "Sale",
    "version": "14.1.1.1",
    'price': 0,
    'sequence': 1,
    "license": "AGPL-3",
    "live_test_url": "",
    'images': ['static/description/main_screenshot.png'],

    "depends": ["base", "sale_management", "purchase", ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_custom_views.xml',
        'views/purchase_order_custom_views.xml',
        'views/free_of_cost_views.xml'
    ],
    "demo": [],
    'installable': True,
    'auto_install': False,
    'application': True,

}
