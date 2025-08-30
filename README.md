🛰️ Interactive Network Topology Map

An interactive visualization of devices in a local network, built with Nmap, JSON, and D3.js.
This project scans your LAN, saves device data into a JSON file, and displays a dynamic network graph in the browser.

📌 Features

📡 Nmap-powered discovery – Scan devices in your local network.

🗂️ JSON storage – Store device info (IP, MAC, OS, type).

🎨 Interactive D3.js graph – Routers (squares) and devices (circles).

🧾 Tooltips – Hover over devices to see:

Hostname / Name

IP address

MAC address

OS info

Device type (router, host, etc.)

🛠️ Tech Stack

Nmap – Network scanning

D3.js (v7) – Data-driven visualization

HTML / CSS / JavaScript – Frontend rendering

🚀 Usage

Scan your network with Nmap

nmap -O -sV -sn 192.168.1.0/24 -oX scan.xml


Or export to JSON using a parser:

nmap -oG scan.txt 192.168.1.0/24


Convert scan results to JSON
Example structure (topology.json):

{
  "nodes": [
    { "id": "192.168.1.1", "name": "Router", "mac": "90:67:17:26:02:EB", "os": "Unknown", "type": "router" },
    { "id": "192.168.1.39", "name": "Laptop", "mac": "AA:BB:CC:DD:EE:FF", "os": "Windows 11", "type": "host" }
  ],
  "links": [
    { "source": "192.168.1.1", "target": "192.168.1.39" }
  ]
}


Open index.html in a browser

The graph will render automatically from topology.json.

Drag nodes, zoom in/out, and hover to see details.

📸 Preview

(Add a screenshot here of your network graph visualization)

🔮 Future Improvements

✅ Automatic JSON generation from Nmap output

✅ OS detection refinement

🌍 Support for external/public network topology mapping

💾 Save graphs as PNG/SVG

⚡ Credits

Built with ❤️ using Nmap + D3.js

Inspired by real-world network topology visualization
