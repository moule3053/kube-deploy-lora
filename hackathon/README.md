# Specific requirements for the hackathon
The scripts are using the variables:
	$varnamespace is the namespace

The following two environment variables should be tuned:

Export port=[e.g.1881] #the port for the nodered service. I suggest to use port 1881 for team1, 1882 for team2, etc.
Export myclusterIP=[e.g.192.168.9.10] #the ip address of the picocluster

## Create node-red instance in $varnamespace namespace
	./deploy_nodered_namespaced.sh

### Delete node-red instance from $varnamespace namespace
	./delete_nodered_namespaced.sh
