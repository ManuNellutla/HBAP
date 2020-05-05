import xml.dom.minidom as md

filename = "truck.xml"

xmldoc = md.parse(filename)

graphicsCommands = xmldoc.getElementsByTagName("Command")

for commandElement in graphicsCommands:

    command = commandElement.firstChild.data.strip()
    print(command)
    attr = commandElement.attributes
    if command == "Circle":
        radius = float(attr["radius"].value)
        width = float(attr["width"].value)
        color = attr["color"].value.strip()
        print(f" Drawing a {command} with radius of {radius}, and color of {color}")