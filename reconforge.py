from modules import dns
from modules import nmap_scan
from modules import subdomain
from modules import rustscan

from parser import nmap_parser

import json
import os



target = input("Target: ").strip()



print("\n[+] Starting Recon")



# Create report folder

os.makedirs(
    "reports",
    exist_ok=True
)



# ---------------- DNS ----------------


ip = dns.resolve(target)



if ip:

    print(
        f"[+] IP Address: {ip}"
    )

else:

    print(
        "[-] DNS resolution failed"
    )

    exit()



# ---------------- Subdomains ----------------


subdomains = subdomain.find_subdomains(
    target
)


# ---------------- RustScan ----------------

ports = rustscan.scan(
    target
)


print(
    "[+] Open Ports:",
    ports
)


# ---------------- Nmap ----------------

xml_file = nmap_scan.run(
    target,
    ports
)

# ---------------- Parse Nmap ----------------


services = nmap_parser.parse(
    xml_file
)



print("\n[+] Open Services")


for service in services:

    print(service)



# ---------------- Report ----------------


report = {

    "target": target,

    "ip": ip,

    "subdomains": subdomains,

    "services": services

}



with open(
    f"reports/{target}.json",
    "w"
) as file:


    json.dump(
        report,
        file,
        indent=4
    )



print("\n[+] Recon completed")

print(
    "[+] Report saved"
)
