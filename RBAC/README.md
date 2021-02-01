# Role-based access control
The scripts are using two environment variables:
	$varnamespace is the namespace
	and 
	$varsaname the service account name

## Create necessary objects for the admin role of each team 
	./createRoles.sh

### Get the token for the role to login into the dashboard
	./createToken
