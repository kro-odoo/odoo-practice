# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class Spaceship(models.Model):

	_name = "space.spaceship"
	_description = "Spaceship for Mission"

	name = fields.Char('Spaceship Name', required=True)
	spaceship_type = fields.Selection(
		[('flyby', 'Flyby'), 
		('orbiter', 'Orbiter'), 
		('atmospheric', 'Atmospheric'), 
		('lander', 'Lander'),
		('rover', 'Rover')],
		string="Type", required=True)
	fuel_type = fields.Selection(
		[('solid', 'Solid'), ('liquid', 'Liquid')], string='Fuel Type')
	active = fields.Boolean('Is Spaceship Active')
	number_of_passengers = fields.Integer(string='Number of Passengers', help='Number of Passengers the Spaceship can carry', readonly=True)
	description = fields.Text(string='Description', help='Description about the Spaceship..')
	length = fields.Float(string='Height')
	width = fields.Float(string='Width')
	mission_ids = fields.One2many('space.mission', 'spaceship_id', string='Missions')

	@api.constrains('length', 'width')
	def _check_length_and_height(self):
		for rec in self:
			if rec.width > rec.length:
				raise UserError(_("Width of the Spaceship cannot be more than the Length"))
