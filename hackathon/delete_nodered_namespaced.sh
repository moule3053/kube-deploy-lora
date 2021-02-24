#!/bin/bash
#fill it with the namespce. e.g. "varnamespace=team1-namespace"
varnamespace=[]

kubectl delete -n $varnamespace -f ../chirpstack-kubernetes/nodered/
