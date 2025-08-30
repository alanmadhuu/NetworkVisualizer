# 🌐 Network Topology Visualizer  

> **Interactive visualization of your local network topology using Nmap + D3.js**  

---

## ✨ Features  
- 🔎 Scans your local network with **Nmap**  
- 📂 Saves device details (IP, MAC, OS) in **JSON**  
- 🎨 Renders an **interactive graph** using **D3.js**  
- 🖱️ Hover on nodes to view detailed device info  
- 📡 Differentiates between **routers (square)** and **hosts (circle)**  

---

## 📂 Project Structure  
- topology.json # Auto-generated network data from Nmap
- front.html # Visualization frontend (D3.js)
- README.md # Project documentation


---

## 🚀 How to Run  

1. Install **Nmap** on your system  
   - [Download Nmap](https://nmap.org/download.html)  

2. Run a network scan and save results as JSON:  


🛠️ Tech Stack

Nmap → Network scanning

JSON → Device data storage

D3.js → Data visualization

HTML/CSS/JS → Frontend
   nmap -O -sV -sn 192.168.1.0/24 -oX scan.xml
   xsltproc scan.xml -o topology.json
