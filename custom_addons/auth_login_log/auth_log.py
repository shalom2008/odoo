# coding: utf-8

from odoo import models, fields


class Log(models.Model):
    _name = 'auth_login_log.log'
    _order = 'id desc'

    login_account = fields.Char()
    login_user = fields.Char()
    login_ip = fields.Char()
    login_time = fields.Datetime()
    login_status = fields.Selection([
        ('s', 'success'),
        ('e', 'error'),
    ])
    note = fields.Text()

