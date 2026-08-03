import subprocess


def find_subdomains(target, timeout=300):

    output_file = f"reports/{target}_subdomains.txt"

    command = [
        "subfinder",
        "-d",
        target,
        "-o",
        output_file,
    ]

    print("[+] Finding subdomains")

    subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=timeout,
    )

    subdomains = []
    try:
        with open(output_file, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    subdomains.append(line)
    except FileNotFoundError:
        print("[-] subfinder produced no output file")

    return subdomains
