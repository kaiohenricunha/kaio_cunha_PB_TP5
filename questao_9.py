from scapy.all import sniff, ARP

# Dictionary to keep track of the observed IP-to-MAC mappings
ip_mac_mapping = {}

def process_packet(packet):
    """
    Callback function that processes each captured packet.
    Checks if an ARP packet indicates a change in the mapping for an IP.
    """
    if packet.haslayer(ARP):
        arp_layer = packet[ARP]
        # We're interested in ARP replies (operation 2)
        if arp_layer.op == 2:
            ip = arp_layer.psrc  # Source IP address from the ARP packet
            mac = arp_layer.hwsrc  # Source MAC address from the ARP packet

            # If we've seen this IP before with a different MAC, alert!
            if ip in ip_mac_mapping:
                if ip_mac_mapping[ip] != mac:
                    print(f"Alerta: Possível ARP Spoofing detectado para IP {ip}!")
                    print(f"MAC anterior: {ip_mac_mapping[ip]}, MAC atual: {mac}")
            else:
                # Store the initial mapping if not seen before
                ip_mac_mapping[ip] = mac

if __name__ == "__main__":
    print("Iniciando monitoramento ARP... (Execute com privilégios de administrador)")
    # Sniff ARP packets and process them with our callback
    sniff(filter="arp", prn=process_packet, store=0)
