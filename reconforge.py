import json
import os
import re
import sys

from modules import dns
from modules import nmap_scan
from modules import subdomain
from modules import rustscan

from parser import nmap_parser


# Matches hostnames, FQDNs, and IPv4 addresses only.
# Blocks anything starting with '-' (argument injection into nmap/rustscan/subfinder)
# and anything containing shell/path metacharacters.
TARGET_PATTERN = re.compile(
    r"^(?!-)[A-Za-z0-9]([A-Za-z0-9.-]{0,251}[A-Za-z0-9])?$"
)


def validate_target(target: str) -> str:
    if not target or not TARGET_PATTERN.match(target):
        print(
            "[-] Invalid target. Use a plain hostname, FQDN, or IPv4 "
            "address (no flags, paths, or special characters)."
        )
        sys.exit(1)
    return target


def main():
    target = validate_target(input("Target: ").strip())

    print("\n[+] Starting Recon")

    os.makedirs("reports", exist_ok=True)

    # ---------------- DNS ----------------
    try:
        ip = dns.resolve(target)
    except Exception as error:
        print("[-] DNS resolution error:", error)
        ip = None

    if ip:
        print(f"[+] IP Address: {ip}")
    else:
        print("[-] DNS resolution failed")
        sys.exit(1)

    # ---------------- Subdomains ----------------
    try:
        subdomains = subdomain.find_subdomains(target)
    except FileNotFoundError:
        print("[-] subfinder not installed or not on PATH — skipping")
        subdomains = []
    except Exception as error:
        print("[-] Subdomain discovery error:", error)
        subdomains = []

    # ---------------- RustScan ----------------
    try:
        ports = rustscan.scan(target)
    except FileNotFoundError:
        print("[-] rustscan not installed or not on PATH — skipping port scan")
        ports = []
    except Exception as error:
        print("[-] RustScan error:", error)
        ports = []

    if len(ports) > 100:
        print("[!] Unusually high open-port count — check `ulimit -n` against the --ulimit flag, or the target may be tarpitting scanners.")

    # ---------------- Nmap ----------------
    try:
        xml_file = nmap_scan.run(target, ports)
    except FileNotFoundError:
        print("[-] nmap not installed or not on PATH — skipping service detection")
        xml_file = None
    except Exception as error:
        print("[-] Nmap error:", error)
        xml_file = None

    # ---------------- Parse Nmap ----------------
    try:
        services = nmap_parser.parse(xml_file)
    except Exception as error:
        print("[-] Nmap XML parse error:", error)
        services = []

    # ---------------- Report ----------------
    report = {
        "target": target,
        "ip": ip,
        "subdomains": subdomains,
        "services": services,
    }

    report_path = f"reports/{target}.json"
    try:
        with open(report_path, "w") as file:
            json.dump(report, file, indent=4)
        print("\n[+] Recon completed")
        print(f"[+] Report saved to {report_path}")
    except OSError as error:
        print("[-] Failed to write report:", error)
        sys.exit(1)


if __name__ == "__main__":
    main()
