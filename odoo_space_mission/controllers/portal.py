# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class SpaceMissionController(CustomerPortal):

	@http.route(['/space/missions/'], type='http', auth='public', website=True)
	def mission_controller(self, **kwargs):
		missions = request.env['space.mission'].search([])
		return request.render('odoo_space_mission.mission_website_controller', {'missions': missions})
