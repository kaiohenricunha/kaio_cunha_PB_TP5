from scapy.all import ARP, Ether, srp

def arp_scan(ip_range):
    # Cria um pacote ARP que solicita os IPs do intervalo informado
    arp_request = ARP(pdst=ip_range)
    # Cria um pacote Ethernet para broadcast
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combina os pacotes Ethernet e ARP
    packet = broadcast / arp_request

    # Envia o pacote e recebe as respostas (timeout de 3 segundos, sem exibir logs)
    answered_list = srp(packet, timeout=3, verbose=0)[0]

    # Extrai os endereços IP e MAC dos hosts que responderam
    hosts = []
    for sent, received in answered_list:
        hosts.append({'ip': received.psrc, 'mac': received.hwsrc})
    return hosts

if __name__ == "__main__":
    # Intervalo de IPs para varredura (execute com privilégios de administrador)
    ip_range = "192.168.1.0/24"
    print("Varredura ARP para o intervalo:", ip_range)
    active_hosts = arp_scan(ip_range)
    for host in active_hosts:
        print("IP: {}, MAC: {}".format(host['ip'], host['mac']))
