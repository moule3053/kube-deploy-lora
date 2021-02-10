# your server name goes here
pico1ip=https://192.168.9.10:6443
varnamespace=team1-namespace
varsaname=team1-sa
# the name of the secret containing the service account token goes here
secretname=$(kubectl get serviceaccounts/$varsaname --namespace $varnamespace -o jsonpath='{.secrets[0].name}')
ca=$(kubectl get secret $secretname -n $varnamespace -o jsonpath='{.data.ca\.crt}')
token=$(kubectl get secret $secretname -n $varnamespace -o jsonpath='{.data.token}' | base64 --decode)
namespace=$(kubectl get secret $secretname -n $varnamespace -o jsonpath='{.data.namespace}' | base64 --decode)

echo "
apiVersion: v1
kind: Config
name: team1-config
clusters:
- cluster:
    certificate-authority-data: ${ca}
    server: ${pico1ip}
  name: picocluster1
contexts:
- context:
    cluster: picocluster1
    namespace: ${namespace}
    user: team1-user
  name: team1-pico1-context
current-context: team1-pico1-context
users:
- name: team1-user
  user:
    token: ${token}
" > team1-config