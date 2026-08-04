import subprocess
import re



def scan(target):


    command = [

        "rustscan",

        "-a",

        target,

        "--ulimit",

        "5000"

    ]


    print("[+] Running RustScan")


    result = subprocess.run(

        command,

        capture_output=True,

        text=True

    )


    # Debug output
    # print(result.stdout)


    ports = re.findall(

        r":(\d+)",

        result.stdout

    )


    ports = list(

        set(

            int(port)

            for port in ports

        )

    )


    ports.sort()


    return ports
