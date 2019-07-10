# -*- coding: utf-8 -*-

import logging
import re

from odoo import http
from odoo.http import Response

class CustomFilter(logging.Filter):
    def filter(self, record):
        return re.search('(GET|HEAD) /k8s_health_check/status', record.getMessage()) is None

class K8sHealthCheck(http.Controller):
    @http.route('/k8s_health_check/status', auth='none', methods=['GET', 'HEAD'])
    def status(self):
        return Response("", status=204)

logger = logging.getLogger("werkzeug")
logger.addFilter(CustomFilter())
