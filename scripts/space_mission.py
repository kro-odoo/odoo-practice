from xmlrpc import client

url = 'http://localhost:8069'
db = 'master'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

model = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = model.execute_kw(db, uid, password,
								'project.project', 'check_access_rights',
								['write'], {'raise_exception': False})
print(model_access)

uid_projects = model.execute_kw(db, uid, password,
								'project.project', 'search',
								[[['user_id', '=', uid]]])
print(uid_projects)

project_fields = model.execute_kw(db, uid, password,
								  'project.project', 'fields_get',
								  [], {'attributes': ['string', 'type', 'required']})
print(project_fields)