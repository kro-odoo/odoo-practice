# -*- coding: utf-8 -*-

from odoo import api, models, fields

class Project(models.Model):
	_inherit = 'project.project'


	mission_id = fields.Many2one('space.mission', string='Mission')
	spaceship_id = fields.Many2one('space.spaceship', string="Spaceship")
	no_of_engines = fields.Integer(related='mission_id.number_of_engines', string='Number of Engines')
	fuel_type = fields.Selection(related='spaceship_id.fuel_type', readonly=True)
	