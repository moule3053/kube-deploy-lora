export varnamespace=team2-namespace
export varsaname=team2-sa

#get service account properties
kubectl get serviceaccounts/$varsaname --namespace $varnamespace -o yaml

#get the token based on the output of the previous command
#kubectl describe secrets/[] -n $varnamespace


