# coding: utf-8

import logging

from odoo import models, api, SUPERUSER_ID, fields
from odoo.exceptions import AccessDenied
from odoo.http import request

_logger = logging.getLogger(__name__)


class OwnUsers(models.Model):
    _inherit = 'res.users'

    @classmethod
    def _login(cls, db, login, password):
        if not password:
            return False
        user_id = False
        login_ip = request.httprequest.environ.get("REMOTE_ADDR")
        data = {
            'login_account': login,
            'login_time': fields.Datetime.now(),
            'login_ip': login_ip,
        }
        try:
            with cls.pool.cursor() as cr:
                self = api.Environment(cr, SUPERUSER_ID, {})[cls._name]
                user = self.search([('login', '=', login)])
                if user:
                    user_id = user.id
                    user.sudo(user_id).check_credentials(password)
                    user.sudo(user_id)._update_last_login()
                    data['login_status'] = 's'
                    data['login_user'] = user.name
                    data['note'] = u'成功'
                else:
                    user = self.search([('login', '=', login), ('active', '=', False)])
                    if user:
                        data['login_status'] = 'e'
                        data['login_user'] = user.name
                        data['note'] = u'账号禁用'
                    else:
                        data['login_status'] = 'e'
                        data['note'] = u'账号不存在'

        except AccessDenied:
            _logger.info("Login failed for db:%s login:%s", db, login)
            user_id = False
            data['login_status'] = 'e'
            data['note'] = u'密码错误'

        with cls.pool.cursor() as cr:
            api.Environment(cr, SUPERUSER_ID, {})['auth_login_log.log'].create(data)
        return user_id
