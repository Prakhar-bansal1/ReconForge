import xml.etree.ElementTree as ET



def parse(xml_file):


    results = []



    if not xml_file:

        return results



    tree = ET.parse(
        xml_file
    )


    root = tree.getroot()



    for port in root.findall(
        ".//port"
    ):



        state = port.find(
            "state"
        )



        if state.get("state") == "open":



            service = port.find(
                "service"
            )


            results.append({

                "port":
                port.get("portid"),


                "service":
                service.get("name"),


                "product":
                service.get("product"),


                "version":
                service.get("version")

            })


    return results
