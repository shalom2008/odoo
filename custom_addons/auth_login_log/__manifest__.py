# -*- coding: utf-8 -*-
{
    'name': "auth_login_log",

    'summary': """
        登录记录""",

    'description': """
        登录记录
    """,

    'author': "ZhangJie",
    'website': "http://www.bankcall.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'ir.model.access.csv',

        'views.xml',
    ],
    'installable': True,
    'auto_install': True,
}
