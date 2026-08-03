import re
import subprocess


# Matches RustScan's default "Open <ip>:<port>" lines, anchored to line start
# so it can't false-positive on timestamps, banners, or other colon+digit text.
OPEN_PORT_PATTERN = re.compile(r"^Open\s+\S+:(\d+)\s*$", re.MULTILINE)


def scan(target, timeout=600):

    command = [
        "rustscan",
        "-a",
        target,
        "--ulimit",
        "5000",
        "--no-banner",
    ]

    print("[+] Running RustScan")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        print("[-] RustScan timed out")
        return []

    if result.returncode != 0:
        print("[-] RustScan exited with an error")
        if result.stderr:
            print(result.stderr)
        return []

    ports = sorted(
        set(int(port) for port in OPEN_PORT_PATTERN.findall(result.stdout))
    )

    return ports