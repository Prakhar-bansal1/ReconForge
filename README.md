# ReconForge

ReconForge is an automated reconnaissance framework designed to simplify the initial phases of security testing.

It combines multiple reconnaissance tools into a single workflow to collect information about a target, identify assets, discover open ports, detect services, and generate structured reports.

## Features

Current Features:

- DNS resolution
- Subdomain discovery using Subfinder
- Fast port discovery using RustScan
- Service and version detection using Nmap
- Nmap XML parsing
- JSON report generation


## ReconForge Workflow

```
Target Domain

      |
      v

DNS Resolution

      |
      v

Subdomain Discovery

      |
      v

RustScan
(Fast Port Discovery)

      |
      v

Nmap
(Service Detection)

      |
      v

Nmap XML Parser

      |
      v

JSON Report
```


## Project Structure

```
ReconForge/

├── reconforge.py

├── modules/
│   ├── dns.py
│   ├── subdomain.py
│   ├── rustscan.py
│   └── nmap_scan.py

├── parser/
│   └── nmap_parser.py

├── reports/

└── README.md
```


## Installation

Clone the repository:

```bash
git clone <your-repository-url>

cd ReconForge
```


Install required security tools:

### Nmap

```bash
sudo apt install nmap
```


### RustScan

Install RustScan:

```bash
sudo apt install rustscan
```


### Subfinder

Install Subfinder:

```bash
sudo apt install subfinder
```


### Verify Installation

```bash
nmap --version
rustscan --version
subfinder -version
```


## Usage

Run:

```bash
python3 reconforge.py
```

Enter the target domain:

Example:

```
Target: example.com
```


The tool will:

1. Resolve the target IP
2. Discover subdomains
3. Find open ports
4. Perform Nmap service detection
5. Generate reports


## Reports

Generated reports are stored inside:

```
reports/
```

Example:

```
reports/

├── example.com.json

└── example.com_nmap.xml
```


## Example Output

```
[+] Starting Recon

[+] IP Address: xxx.xxx.xxx.xxx

[+] Finding subdomains

[+] Open Ports:
[80,443]

[+] Running Nmap

[+] Nmap scan completed

[+] Report saved
```


## Disclaimer

ReconForge is created for educational purposes and authorized security testing only.

Always obtain proper permission before scanning any target.

# Trust Nothing Verify Everything!
