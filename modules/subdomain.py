import subprocess



def find_subdomains(target):


    output_file = (

        f"reports/{target}_subdomains.txt"

    )


    command = [

        "subfinder",

        "-d",

        target,

        "-o",

        output_file

    ]


    print(
        "[+] Finding subdomains"
    )



    try:


        subprocess.run(

            command,

            capture_output=True,

            text=True

        )


        subdomains = []



        with open(output_file,"r") as file:


            for line in file:

                subdomains.append(
                    line.strip()
                )



        return subdomains



    except:


        print(
            "[-] Subdomain scan failed"
        )


        return []
