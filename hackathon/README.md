# Specific requirements for the hackathon
The scripts are using two environment variables:
	$varnamespace is the namespace
	and 
	$port the port for the nodered service. I suggest to use port 1881 for team1, 1882 for team2, etc.

## Create node-red instance in $varnamespace namespace
	./deploy_nodered_namespaced.sh

### Delete node-red instance from $varnamespace namespace
	./delete_nodered_namespaced.sh
