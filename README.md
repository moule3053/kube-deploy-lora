# kube-deploy-lora


### Run etcher from cli to burn images:
```
sudo /Applications/balenaEtcher.app/Contents/MacOS/balenaEtcher
```

### Allow ssh in SD cards
```
touch /Volumes/boot/ssh
```

### SSH into each Pis
```
ssh pi@raspberrypi.local
```

### Add inside /boot/cmdline.txt
```
cgroup_enable=memory
```

### Add inside /etc/network/interfaces
```
auto eth0
iface eth0 inet static
address 192.168.1.10
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 192.168.1.1 8.8.8.8
```

### Update the /etc/hosts with your cluster IPs
```
192.168.1.10 pc0
192.168.1.11 pc1
192.168.1.12 pc2
...
192.168.1.N pcN
```

### Edit the hostname and password by
```
sudo raspi-config
```

### And reboot
```
sudo reboot
```

### Lastly, enable passwordless connection by
```
ssh-copy-id pi@name
```

### The Pi is now ready to run ansible scripts
