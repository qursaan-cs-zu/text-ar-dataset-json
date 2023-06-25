import os
import xml.etree.ElementTree as ET
import json


def iterate_files(directory):
    count = 0  
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                xml_file = os.path.join(root, file)
                try:
                    process_xml_file(xml_file, root, count) 
                    count += 1  
                except Exception as e:
                    print(f"Error processing file '{xml_file}': {str(e)}")
                    with open("./Error.eor", "a") as file:
                        file.write(f"Error processing file '{xml_file}': {str(e)}")
                        file.write("\n")
                    continue


def process_xml_file(xml_file, root_dir, count):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    title = root.find("TITLE").text.strip()
    abstract = root.find("ABSTRACT").text.strip()
    text = root.find("TEXT").text.strip()
    data = {
        "example_id": count,
        "paragraph": text,
        "summary": abstract,
        "title": title,
        "category": root_dir[2:]
    }

    with open("data.json", "a", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data, ensure_ascii=False))  
        json_file.write("\n")
    print(f"Processed file: {xml_file}")
    print()


directory_path = "/content/text-ar-dataset-ant/code/data"
iterate_files(directory_path)

