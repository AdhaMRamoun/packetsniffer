from scapy import all
show_packets = 1
sniffed_data = scapy.sniff(count=show_packets,filter="port 139")
for i in range(0,show_packets):
    sniffed_data[i].show()