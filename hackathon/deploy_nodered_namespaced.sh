#!/bin/bash
#fill it with the namespce. e.g. "varnamespace=team1-namespace"
varnamespace=[]

kubectl apply -f ../chirpstack-kubernetes/nodered/deployment.yml --namespace $varnamespace
envsubst < ../chirpstack-kubernetes/nodered/service.yml | kubectl apply --namespace $varnamespace -f -