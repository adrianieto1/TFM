sudo ovs-vsctl add-br br1
sudo ovs-vsctl add-br br2
sudo ovs-vsctl add-port br1 eth1
sudo ovs-vsctl add-port br2 eth3
sudo ovs-vsctl add-port s1 eth2
sudo ifconfig eth1 0
sudo ifconfig eth3 0
sudo ifconfig eth2 0
sudo ifconfig br1 200.175.2.129 netmask 255.255.255.0 up
sudo ifconfig br2 192.168.3.129 netmask 255.255.255.0 up
sudo ifconfig s1 192.168.20.129 netmask 255.255.255.0 up
sudo ovs-vsctl set-controller br1 tcp:192.168.8.128:6653
sudo ovs-vsctl set-controller br2 tcp:192.168.8.128:6653
sudo ovs-vsctl set-controller s1 tcp:192.168.8.128:6653
sudo sysctl -w net.ipv4.ip_forward=1
