# kube-deploy-lora

### Run following commands:
```
kubectl apply -f ./mosquitto/
kubectl apply -f ./postgres/
kubectl apply -k redis/.
# kubectl apply -f ./chirpstack-gateway-bridge/
kubectl apply -f ./chirpstack-network-server/
kubectl apply -f ./chirpstack-application-server/
kubectl apply -f ./monitoring/
kubectl apply -f ./nodered/
sh ./postgres/create_db.sh
```

### external IP (192.168.2.11 for now) is exposed in:
```
port:8080  /chirpstack-application-server/service.yml
port:8080  /chirpstack-network-server/service.yml
port:9090  /monitoring/prometheus.yaml
port:3000  /monitoring/grafana.yaml
port:1880  /nodered/service.yml
```

### For deleting everything:
```
kubectl delete -f ./mosquitto/
kubectl delete -f ./postgres/
kubectl delete -k redis/.
# kubectl delete -f ./chirpstack-gateway-bridge/
kubectl delete -f ./chirpstack-network-server/
kubectl delete -f ./chirpstack-application-server/
kubectl delete -f ./monitoring/
kubectl delete -f ./nodered/
kubectl delete pvc mosquitto postgres-pv-claim postgresinit-pv-claim
kubectl delete pv mosquitto-pv-volume postgres-pv-volume postgresinit-pv-volume
```



more documentation is coming
