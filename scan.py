import nmap 
import json

nm=nmap.PortScanner()
subnet="192.168.1.0/24"

print("Nmap version:", nm.nmap_version())

print(f"Scanning subnet: {subnet}")
nm.scan(hosts=subnet, arguments='-sn')# Ping scan

nodes = []
links = []

# Add a default "router" node
router_ip = "192.168.1.1"
nodes.append({"id": router_ip, "type": "router"})

if router_ip in nm.all_hosts():
    router_mac = nm[router_ip]['addresses'].get('mac', 'Unknown')
    nodes.append({"id": router_ip, "type": "router", "mac": router_mac})

for host in nm.all_hosts():
    mac = nm[host]['addresses'].get('mac', 'Unknown')
    hostname = nm[host].hostname() or host
    
    # Skip router (already added above)
    if host == router_ip:
        continue

    # Add host node
    if nm[host].state() == "up":
        nodes.append({"id": host, "type": "host", "mac": mac, "hostname": hostname})
        links.append({"source": router_ip, "target": host})

# Save JSON
topology = {"nodes": nodes, "links": links}
with open("topology.json", "w") as f:
    json.dump(topology, f, indent=2)

print("Topology saved to topology.json")