# kube-deploy-lora

## Deploy

### Replace your cluster ip with [192.168.9.12] value
```
export myclusterIP=192.168.1.10
```

### Generate GlusterFS Endpoints files: edit the IP address range in the file first
```
./generate_glusterfs_endpoints.sh
```

### Run following to deploy all:
```
sh ./deploy_all.sh
```

### Or run following commands for debugging:
```
kubectl apply -f ./mosquitto/mosquitto-glusterfs-endpoint.yaml
kubectl apply -f ./mosquitto/storage.yml
kubectl apply -f ./mosquitto/configmap.yaml
kubectl apply -f ./mosquitto/deployment.yml
envsubst < ./mosquitto/service.yml | kubectl apply -f -

kubectl apply -f ./influxdb/influxdb-glusterfs-endpoint.yaml
kubectl apply -f ./influxdb/configmap.yaml
kubectl apply -f ./influxdb/storage.yml
kubectl apply -f ./influxdb/deployment.yml
envsubst < ./influxdb/service.yml | kubectl apply -f -

kubectl apply -f ./postgres/
kubectl apply -k redis/.

# kubectl apply -f ./chirpstack-gateway-bridge/

kubectl apply -f ./chirpstack-network-server/configMap.yml
kubectl apply -f ./chirpstack-network-server/deployment.yml
envsubst < ./chirpstack-network-server/service.yml | kubectl apply -f -

kubectl apply -f ./chirpstack-application-server/configMap.yml
kubectl apply -f ./chirpstack-application-server/deployment.yml
envsubst < ./chirpstack-application-server/service.yml | kubectl apply -f -

kubectl apply -f ./monitoring/configmap.yaml
kubectl apply -f ./monitoring/kube-state-metrics.yaml
kubectl apply -f ./monitoring/node-exporter.yaml
kubectl apply -f ./monitoring/rbac.yaml
envsubst < ./monitoring/grafana.yaml | kubectl apply -f -
envsubst < ./monitoring/prometheus.yaml | kubectl apply -f -

kubectl apply -f ./nodered/deployment.yml
envsubst < ./nodered/service.yml | kubectl apply -f -
```

### After the pod creation:
```
sh ./postgres/create_db.sh
```

### external IP is exposed in:
```
port:8080  /chirpstack-application-server/service.yml
port:8000  /chirpstack-network-server/service.yml
port:9090  /monitoring/prometheus.yaml
port:3000  /monitoring/grafana.yaml
port:1883  /mosquitto/service.yml
port:8086  /influxdb/service.yml
port:1880  /nodered/service.yml
```

## Delete
### Run following to delete all:
```
sh ./delete_all.sh
```

### Or run following commands for deleting 1 by 1:
```
kubectl delete -f ./mosquitto/
kubectl delete -f ./influxdb/
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
