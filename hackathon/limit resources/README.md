# Limit the resource usage for a namespace
Each fog cluster has 4 cpu cores and 4 GB RAM.
This quota file specifies a limit of 1/4 of the available resource on the cluster to each namespace. The teams should declare the required resources in their manifest files as the sample YAML file in the Example folder.
Note: We may adapt these amounts of resources during the hackathon depending to the needs of the teams
	kubectl apply -f ./quota.yaml --namespace=[team1-namespace]

# Specify default limit ranges for RAM usage
	kubectl apply -f ./default-mem-limits.yaml --namespace=[team1-namespace]

# Specify default limit ranges for CPU usage
	kubectl apply -f ./default-cpu-limits.yaml --namespace=[team1-namespace]
