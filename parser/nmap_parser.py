import xml.etree.ElementTree as ET


def parse(xml_file):

    results = []

    if not xml_file:
        return results

    tree = ET.parse(xml_file)
    root = tree.getroot()

    for port in root.findall(".//port"):

        state = port.find("state")
        if state is None or state.get("state") != "open":
            continue

        service = port.find("service")

        results.append({
            "port": port.get("portid"),
            "service": service.get("name") if service is not None else None,
            "product": service.get("product") if service is not None else None,
            "version": service.get("version") if service is not None else None,
        })

    return results
