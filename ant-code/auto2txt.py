import os
import xml.etree.ElementTree as ET


def iterate_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                xml_file = os.path.join(root, file)
                try:
                    process_xml_file(xml_file, root)
                except Exception as e:
                    print(f"Error processing file '{xml_file}': {str(e)}")
                    with open("./Error.eor", "a") as file:
                        file.write(f"Error processing file '{xml_file}': {str(e)}")
                        file.write("")
                    continue


def process_xml_file(xml_file, root_dir):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    title = root.find("TITLE").text.strip()
    abstract = root.find("ABSTRACT").text.strip()
    text = root.find("TEXT").text.strip()

    output_dir = os.path.join("./data", "title", root_dir)
    os.makedirs(os.path.join("./data", "title", root_dir), exist_ok=True)
    os.makedirs(os.path.join("./data", "abstract", root_dir), exist_ok=True)
    os.makedirs(os.path.join("./data", "text", root_dir), exist_ok=True)

    file_name = str(len(os.listdir(output_dir)) + 1).zfill(5) + ".txt"

    # Write the extracted information to the output file
    with open(os.path.join("./data", "title", root_dir, file_name), "w") as file:
        file.write(title)
    with open(os.path.join("./data", "abstract", root_dir, file_name), "w") as file:
        file.write(abstract)
    with open(os.path.join("./data", "text", root_dir, file_name), "w") as file:
        file.write(text)

    print(f"Processed file: {xml_file}")
    print()


directory_path = "./"
iterate_files(directory_path)
