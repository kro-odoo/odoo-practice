# -*- coding: utf-8 -*-

from odoo import api, fields, models

class MissionProject(models.TransientModel):
	_name = 'mission.project.wizard'

	name = fields.Char(string='Title', required=True)
	spaceship_id = fields.Many2one('space.spaceship', string='Spaceship')
	mission_id = fields.Many2one('space.mission', string='Mission')
	no_of_engines = fields.Integer(related='mission_id.number_of_engines',string='Number of Engines')
	fuel_type = fields.Selection(related='spaceship_id.fuel_type', readonly=True)

	def action_generate_project(self):
		self.ensure_one()
		new_project = self.env['project.project'].create({
			'name': self.name,
			'spaceship_id': self.spaceship_id.id,
			'mission_id': self.mission_id.id,
			'no_of_engines': self.no_of_engines,
			'fuel_type': self.fuel_type,
			})
		return new_project