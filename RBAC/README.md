# Role-based access control
The scripts are using two environment variables:
	$varnamespace is the namespace
	and 
	$varsaname the service account name

## Create necessary objects for the admin role of each team 
	./createRoles.sh

### Get the token for the role to login into the dashboard
	./createToken

### Install kubectl in your computer using the guide provided by the official Kubernetes website

According to your operating system (OS), find the instructions to install kubectl below:

Linux OS: https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-linux
Mac OS: https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-macos
Windows OS: https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-windows

### Get the kubeconfig for your cluster

	./getConfig.sh

### Merge the kubeconfigs for each team

	KUBECONFIG=~/.kube/team1-pico1-config:~/.kube/team1-pico2-config

	kubectl config view --flatten > ~/.kube/allconfigs

### Test the kubeconfigs for each team

	kubectl config get-contexts

	kubectl --context [the-context-name] get pods