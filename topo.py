from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        h1 = self.addHost( 'h1', ip='192.168.20.131' )
        h2 = self.addHost( 'h2', ip='192.168.20.132' )
        h3 = self.addHost( 'h3', ip='192.168.20.133' )
        h4 = self.addHost( 'h4', ip='192.168.20.134' )

        s1 = self.addSwitch( 's1' )

        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s1 )
        self.addLink( h4, s1 )

def run():
    topo = MyTopo()
    net = Mininet(topo=topo)
    net.start()

    info(net['h1'].cmd("ip route add default via 192.168.20.129"))
    info(net['h2'].cmd("ip route add default via 192.168.20.129"))
    info(net['h3'].cmd("ip route add default via 192.168.20.129"))
    info(net['h4'].cmd("ip route add default via 192.168.20.129"))

    info(net['h1'].cmd("ip route add 192.168.20.0/24 via 0.0.0.0 dev h1-eth0"))
    info(net['h2'].cmd("ip route add 192.168.20.0/24 via 0.0.0.0 dev h2-eth0"))
    info(net['h3'].cmd("ip route add 192.168.20.0/24 via 0.0.0.0 dev h3-eth0"))
    info(net['h4'].cmd("ip route add 192.168.20.0/24 via 0.0.0.0 dev h4-eth0"))
    
    info(net['h1'].cmd("ip route del 192.0.0.0/8 via 0.0.0.0 dev h1-eth0"))
    info(net['h2'].cmd("ip route del 192.0.0.0/8 via 0.0.0.0 dev h2-eth0"))
    info(net['h3'].cmd("ip route del 192.0.0.0/8 via 0.0.0.0 dev h3-eth0"))
    info(net['h4'].cmd("ip route del 192.0.0.0/8 via 0.0.0.0 dev h4-eth0"))
    
    net.pingAll()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()

topos = { 'mytopo': ( lambda: MyTopo() ) }