import os
import platform
import json
import xml.etree.ElementTree


def modify_misc_xml(path, name_custom):
    tree = xml.etree.ElementTree.parse(path)
    root = tree.getroot()
    root_manager = root.find('component[@name="ProjectRootManager"]')
    root_manager.set('project-jdk-name', name_custom)
    tree.write(path)


def modify_venn_diagram_iml(path, name_custom):
    tree = xml.etree.ElementTree.parse(path)
    root = tree.getroot()
    module = root.find('component[@name="NewModuleRootManager"]')
    order_entry = module.find('orderEntry[@type="jdk"]')
    order_entry.set('jdkName', name_custom)
    tree.write(path)


def get_interpreter_settings(os_name):
    with open('interpreter_settings.json', 'r') as f:
        settings = json.load(f)
    return settings[os_name]


# Main entry point of your script
if __name__ == '__main__':
    current_os_name = platform.system().lower()
    interpreter_settings = get_interpreter_settings(current_os_name)
    interpreter_name = interpreter_settings['interpreter_name']
    interpreter_name_custom = interpreter_settings['interpreter_name_custom']

    misc_xml_path = '.idea/misc.xml'
    venn_diagram_iml_path = '.idea/My-Venn-Diagram.iml'

    if os.path.exists(misc_xml_path):
        modify_misc_xml(misc_xml_path, interpreter_name_custom)
        print('Modified misc.xml')

    if os.path.exists(venn_diagram_iml_path):
        modify_venn_diagram_iml(venn_diagram_iml_path, interpreter_name_custom)
        print('Modified My-Venn-Diagram.iml')
