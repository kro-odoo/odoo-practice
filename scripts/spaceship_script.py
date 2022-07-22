from xmlrpc import client

url = 'http://localhost:8069'
db = 'master'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))

uid = common.authenticate(db, username, password, {})

model = client.ServerProxy("{}/xmlrpc/2/object".format(url))

new_spaceship = model.execute_kw(db, uid, password,
								'space.spaceship', 'create',
								[
									{
										'name': 'Mangal Yaan',
										'spaceship_type': 'orbiter',
										'width': 143,
										'length': 1689,
										'fuel_type': 'liquid',
										'active': True,
									}
								])
