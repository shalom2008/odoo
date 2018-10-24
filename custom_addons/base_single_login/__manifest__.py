# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Auth: Gavin GU Email:guwenfengvip@163.com
{
    'name': '单点登录',
    'category': 'web',
    'summary': '帐号只允许一次登录',

    'description': """
        主要内容:
        ----------------
        *  一个帐号只允许一次登录，当前帐号登录时，清除该帐号下其它客户的session.
    """,

    'version': '0.1',
    'author': "Gavin Gu",
    'website': "",
    'depends': [
        'base', 'web', 'base_setup',
    ],
    'data': ["single_login.xml"],
    'installable': True,
    'auto_install': False,
    'application': False,
}
