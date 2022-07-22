#-*- coding: utf-8 -*-
{
	'name': 'Odoo Space Mission',
	'summary': 'Odoo Inc Moon mission',
	'description': """Odoo is all set to reach the Moon""",
	'author': 'Krina Oza',
	'category': 'Mission',
	'version': '1.0',

	'depends': ['project', 'portal', 'web'],

	'data': [
		'security/odoo_space_mission_security.xml',
		'security/ir.model.access.csv',
		'views/odoo_space_mission_menuitems.xml',
		'views/odoo_space_spaceship_views.xml',
		'views/odoo_space_mission_views.xml',
		'views/project_inherit_views.xml',
		'wizard/mission_project_views.xml',
		'report/spaceship_report_template.xml',
		'views/portal_template_views.xml',
	],

	'demo': [
		'demo/spaceship_demo.xml'
	],

	'installable': True,
	'license': 'LGPL-3',
	'application': True,
}