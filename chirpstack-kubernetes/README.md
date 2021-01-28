# kube-deploy-lora

### Run following commands:
```
#replace your cluster ip with [192.168.9.12] value
export myclusterIP=192.168.9.12

# Generate GlusterFS Endpoints files
# Edit the IP address range in the file first

mkdir influxdb # if it doesn't exist

./generate_glusterfs_endpoints.sh

kubectl apply -f mosquitto/mosquitto-glusterfs-endpoint.yaml
kubectl apply -f ./mosquitto/storage.yml
kubectl apply -f ./mosquitto/deployment.yml
envsubst < ./mosquitto/service.yml | kubectl apply -f -

kubectl apply -f ./postgres/
kubectl apply -k redis/.

# kubectl apply -f ./chirpstack-gateway-bridge/

kubectl apply -f ./chirpstack-network-server/configMap.yml
kubectl apply -f ./chirpstack-network-server/deployment.yml
envsubst < ./chirpstack-network-server/service.yml | kubectl apply -f -

kubectl apply -f ./chirpstack-application-server/configMap.yml
kubectl apply -f ./chirpstack-application-server/deployment.yml
envsubst < ./chirpstack-application-server/service.yml | kubectl apply -f -

kubectl apply -f ./monitoring/

kubectl apply -f ./nodered/deployment.yml
envsubst < ./nodered/service.yml | kubectl apply -f -

sh ./postgres/create_db.sh
```

### external IP (192.168.2.11 for now) is exposed in:
```
port:8080  /chirpstack-application-server/service.yml
port:8080  /chirpstack-network-server/service.yml
port:9090  /monitoring/prometheus.yaml
port:3000  /monitoring/grafana.yaml
port:1883  /mosquitto/service.yml
port:8086  /influxdb/service.yml
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
