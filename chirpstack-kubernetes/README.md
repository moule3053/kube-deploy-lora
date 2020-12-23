# kube-deploy-lora

* Run following commands:
```
kubectl apply -f ./mosquitto/
kubectl apply -f ./postgres/
kubectl apply -k redis/.
kubectl apply -f ./chirpstack-gateway-bridge/
kubectl apply -f ./chirpstack-network-server/
kubectl apply -f ./chirpstack-application-server/
kubectl apply -f ./monitoring/
sh ./postgres/create_db.sh
```

* external IPs are set inside (192.168.2.11 for now):
```
port:8080  /chirpstack-application-server/service.yml
port:9090  /monitoring/prometheus.yaml
port:3000  /monitoring/grafana.yaml
```



more documentation is coming
