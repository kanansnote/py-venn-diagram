import os
import platform
import json
import xml.etree.ElementTree as ET


def modify_misc_xml(path, interpreter_name_custom):
    tree = ET.parse(path)
    root = tree.getroot()
    root_manager = root.find('component[@name="ProjectRootManager"]')
    root_manager.set('project-jdk-name', interpreter_name_custom)
    tree.write(path)


def modify_projectname_xml(path, interpreter_name_custom):
    tree = ET.parse(path)
    root = tree.getroot()
    module = root.find('component[@name="NewModuleRootManager"]')
    order_entry = module.find('orderEntry[@type="jdk"]')
    order_entry.set('jdkName', interpreter_name_custom)
    tree.write(path)


def get_interpreter_settings(current_os):
    with open('interpreter_settings.json', 'r') as f:
        settings = json.load(f)
    return settings[current_os]


# Main entry point of your script
if __name__ == '__main__':
    current_os = platform.system().lower()
    interpreter_settings = get_interpreter_settings(current_os)
    interpreter_name = interpreter_settings['interpreter_name']
    interpreter_name_custom = interpreter_settings['interpreter_name_custom']

    misc_xml_path = '/path/to/misc.xml'  # Update with the actual path to misc.xml
    projectname_xml_path = '/path/to/projectname.xml'  # Update with the actual path to projectname.xml

    if os.path.exists(misc_xml_path):
        modify_misc_xml(misc_xml_path, interpreter_name_custom)
        print('Modified misc.xml')

    if os.path.exists(projectname_xml_path):
        modify_projectname_xml(projectname_xml_path, interpreter_name_custom)
        print('Modified projectname.xml')

    # Your code follows...
