# -*- coding: utf-8 -*-
import odoo
from odoo import http
from odoo import SUPERUSER_ID
import logging

_logging = logging.getLogger(__name__)


class session_web(http.Controller):
    @http.route('/web/session/remove/', type='json', auth="public", website=True)
    def remove(self, **kw):
        login = False
        para = http.request.jsonrequest.get("params")
        u = http.request.env['res.users']
        obj = u.sudo().browse(para['uid'])
        if obj.session_id and para["session"] and obj.session_id != para["session"]:
            print obj
            sess = odoo.http.root.session_store.get(obj.session_id)
            print sess
            odoo.http.root.session_store.delete(sess)
            login = True
        obj.write({"session_id": para["session"]})
        return login
