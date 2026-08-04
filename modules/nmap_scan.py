import subprocess
import os



def run(target, ports):

    if not ports:
        print("[-] No ports received from RustScan")
        return None


    # Create reports folder if not exists
    os.makedirs(
        "reports",
        exist_ok=True
    )


    output_file = (
        f"reports/{target}_nmap.xml"
    )


    # Convert list into Nmap format
    # Example:
    # [22,80,443]
    # becomes:
    # 22,80,443

    port_string = ",".join(
        map(str, ports)
    )


    command = [

        "nmap",

        "-sV",          # Service/version detection

        "-T4",          # Faster timing

        "-p",
        port_string,

        "-oX",
        output_file,

        target
    ]


    print(
        "[+] Running Nmap on ports:",
        port_string
    )


    try:

        result = subprocess.run(

            command,

            capture_output=True,

            text=True,

            timeout=3600

        )


        if result.stderr:

            print(
                "[Nmap Warning]"
            )

            print(
                result.stderr
            )


        print(
            "[+] Nmap scan completed"
        )


        return output_file



    except subprocess.TimeoutExpired:


        print(
            "[-] Nmap scan timed out"
        )


        return None



    except Exception as error:


        print(
            "[-] Nmap error:",
            error
        )


        return None
