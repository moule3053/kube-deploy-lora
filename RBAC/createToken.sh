export varnamespace=team1-namespace
export varsaname=team1-sa

#get service account properties
kubectl get serviceaccounts/$varsaname --namespace $varnamespace -o yaml

#get the token based on the output of the previous command
#kubectl describe secrets/[] -n $varnamespace


