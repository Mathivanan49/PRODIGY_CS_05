from scapy.all import sniff, IP


def analyze_packet(packet):

    if packet.haslayer(IP):
        print("\n----------------")
        print("Source:", packet[IP].src)
        print("Destination:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)


print("Capturing only 10 packets...\n")

sniff(
    prn=analyze_packet,
    store=False,
    count=10
)

print("\nCapture Completed")