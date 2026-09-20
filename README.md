# NetSecure
### Network Security Assessment Tool

NetSecure is a beginner-friendly tool that performs a basic security assessment of authorized systems or networks. It scans for open ports using Nmap, checks the services running, assigns a risk level, and generates a simple report. Every scan is also logged for future reference.

> This project is for educational purposes only. Only scan systems/networks you have permission to test.

## Features
- Discover active devices on a network
- Scan common open ports using Nmap
- Display detected services
- Classify risk as Low, Medium, or High
- Generate a security report
- Log every scan and view past scan history

## Modules

| Module | Description |
|---|---|
| Scanning | Takes an IP/domain and runs the Nmap scan |
| Risk Analysis | Classifies the scan result as Low, Medium, or High |
| Logging | Stores each scan in SQLite and retrieves past logs |
| Report & Dashboard | Flask web interface for viewing results and reports |

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Backend | Flask |
| Frontend | HTML, CSS, Bootstrap |
| Scanning | Nmap, Wireshark |
| Database | SQLite |

## Documentation
Full project proposal is in [`docs/`](./docs).
