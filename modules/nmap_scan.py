import os
import subprocess


def run(target, ports):

    if not ports:
        print("[-] No ports received from RustScan")
        return None

    os.makedirs("reports", exist_ok=True)

    output_file = f"reports/{target}_nmap.xml"

    port_string = ",".join(map(str, ports))

    command = [
        "nmap",
        "-sV",  
        "-T4",   
        "-p",
        port_string,
        "-oX",
        output_file,
        target,
    ]

    print("[+] Running Nmap on ports:", port_string)

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=3600,
    )

    if result.stderr:
        print("[Nmap Warning]")
        print(result.stderr)

    print("[+] Nmap scan completed")

    return output_file
