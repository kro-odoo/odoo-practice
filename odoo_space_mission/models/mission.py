# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Mission(models.Model):
	_name = "space.mission"
	_description = "Space Mission"

	name = fields.Char(string="Mission", required=True)
	spaceship_id = fields.Many2one('space.spaceship', string='Assigned Spaceship')
	crew_members_ids = fields.Many2many('res.partner', string='Crew Members')
	launch_date = fields.Date()
	return_date = fields.Date()
	number_of_engines = fields.Integer(required=True)
	fuel_required = fields.Float(string="Amount of Fuel", help="Amount of fuel required for the mission", required=True)
	safety_features = fields.Char('Safety Features')
	project_ids = fields.One2many('project.project', 'mission_id', string='Projects')

	@api.constrains('launch_date', 'return_date')
	def _check_launch_and_return_date(self):
		for rec in self:
			if rec.return_date < rec.launch_date:
				raise ValidationError('Return date cannot be before the Launch.')

	def action_create_project(self):
		self.ensure_one()
		return {
			'type': 'ir.actions.act_window',
			'res_model': 'mission.project.wizard',
			'view_mode': 'form',
			'target': 'new',
			'context': {
				'default_mission_id': self.id,
				'default_spaceship_id': self.spaceship_id.id,
				'default_no_of_engines': self.number_of_engines,
			}
		}		
