import os
import subprocess


def run(target, ports):

    if not ports:
        print("[-] No ports received from RustScan")
        return None

    os.makedirs("reports", exist_ok=True)

    output_file = f"reports/{target}_nmap.xml"

    # Convert list into Nmap format, e.g. [22, 80, 443] -> "22,80,443"
    port_string = ",".join(map(str, ports))

    command = [
        "nmap",
        "-sV",   # Service/version detection
        "-T4",   # Faster timing
        "-p",
        port_string,
        "-oX",
        output_file,
        target,
    ]

    print(f"[+] Running Nmap on {len(ports)} port(s)")

    # FileNotFoundError (nmap missing) and subprocess.TimeoutExpired are
    # intentionally allowed to propagate — the caller decides how to handle them.
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
