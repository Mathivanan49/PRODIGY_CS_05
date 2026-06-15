Task–05: Network Packet Analyzer – Overview
Objective

The objective of this project is to develop a Network Packet Analyzer (Packet Sniffer) that captures and analyzes network traffic in real time. The tool extracts useful information from packets such as source IP address, destination IP address, protocol type, and payload data.

Description

A Network Packet Analyzer is a network monitoring tool used to observe and inspect packets traveling across a network. Every time data is transmitted over the internet, it is broken into smaller units called packets. This project captures those packets and displays selected information for analysis.

The analyzer helps understand how communication occurs between devices and how different protocols operate within a network.

Features
Capture network packets
Display Source IP Address
Display Destination IP Address
Identify Protocol Type (TCP, UDP, ICMP, etc.)
Read and display packet payload information
Real-time packet monitoring
Educational and authorized usage
Technologies Used
Programming Language: Python
Library: Scapy
IDE: Visual Studio Code (VS Code)
Version Control: Git & GitHub
Working Principle
Start packet capture.
Monitor incoming and outgoing packets.
Extract packet information.
Analyze packet headers.
Display details to the user.
Stop after capturing required packets.
Expected Output

Example output:

Source IP: 192.168.1.10
Destination IP: 142.250.xxx.xxx
Protocol: TCP
Payload: GET / HTTP/1.1
Applications
Network monitoring
Learning network protocols
Troubleshooting connectivity issues
Educational cybersecurity labs
Traffic analysis
Ethical Consideration

This tool should be used only in authorized and educational environments. Packet capture should not be used to monitor networks or devices without permission.

Conclusion

The Network Packet Analyzer demonstrates how network communication can be captured and interpreted using Python. It provides practical understanding of packet structure, protocols, and real-time traffic analysis while emphasizing responsible and ethical usage.
