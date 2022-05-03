# -*- coding: utf-8 -*-
{
    'name': "banking_management",

    'summary': "Banking management Assignment",

    'description': """
        Long description of module's purpose
    """,

    'author': "Apoorv Saxena",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bank_data.xml',
        'views/bank_customer.xml',
        'views/templates.xml',
    ],
    'installable' : True,
    'application': True,
    'license': 'LGPL-3',
    'version' : '1.0',
    'sequence' : -200,
}
