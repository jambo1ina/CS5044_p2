import xml.etree.ElementTree as ET

def generate_mappings(input_xmls, output_dir, variables):
    if output_dir[-1] != "/":
        output_dir += "/"

    for input in input_xmls:
        round = input[input.rfind("/round") + 6:input.rfind(".xml")]

        tree = ET.parse(input)
        root = tree.getroot()

        for var in root[3]:
            try:
                name = var.attrib["name"]
                if name in variables:
                    description = ""
                    mapping = dict()

                    for item in var:
                        if item.tag == "{http://www.icpsr.umich.edu/DDI}labl":
                            description = item.text.replace("\n", "")

                        if item.tag == "{http://www.icpsr.umich.edu/DDI}catgry":
                            mapping[item[0].text.replace("\n", "")] = item[1].text.replace("\n", "")

                    with open(output_dir + round + "/" + name + ".csv", 'w') as out:
                        out.write(description + "\n")
                        print(mapping)
                        for key in mapping.keys():
                            out.write(key + "," + mapping[key] + "\n")
            except KeyError:
                continue