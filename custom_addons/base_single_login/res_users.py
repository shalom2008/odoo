# -*- coding:utf-8 -*-
##############################################################################


from odoo import SUPERUSER_ID, models
from odoo import tools,fields,models,api

class res_users(models.Model):
    _inherit="res.users"

    session_id=fields.Char("SessionID",size=50)


class BaseConfigSettings(models.TransientModel):
    _inherit = 'base.config.settings'


    once_login = fields.Boolean(string='单次登陆', help='一个帐号只允许一次登录，当前帐号登录时，清除该帐号下其它客户的session',defaults=False)


    @api.model
    def get_default_once_login(self,fields):
        configs=self.env['base.config.settings'].search([])
        length = len(configs)
        if length != 0:
            config = configs[-1]
            return {"once_login": config.once_login}
        else:
            return {}


    @api.model
    def signin_login(self):
        configs = self.env['base.config.settings'].search([])
        length = len(configs)
        if length != 0:
            config = configs[-1]
            return config.once_login
        else:
            return " "
