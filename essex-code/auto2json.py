
import os
import json

def organize_files(source_directory):
    global counter
    category = source_directory[7:]

    for root, dirs, files in os.walk(source_directory):
        dirs.sort()
        files.sort()
        text = ""
        summaries = {}
        cnt = 0

        for file in files:
            print("Processing file:", file)
            file_extension = os.path.splitext(file)[1].lower() 

            if file_extension == ".txt":
                with open(os.path.join(root, file), "r") as source_file:
                    text = source_file.read()
                cnt += 1
            elif file_extension.startswith("."):
                summary_key = file_extension[1:].upper()

                cnt += 1
                with open(os.path.join(root, file), "r") as source_file:
                    summaries[summary_key] = source_file.read()

            if text and cnt == 6:
                for i, (summary_key, summary) in enumerate(summaries.items(), start=counter):
                    data = {
                        "example_id": i,
                        "paragraph": text,
                        "summary": summary,
                        "category": category,
                    }

                    with open("/content/text-ar-dataset-json/jsons/essex.jsonl", "a", encoding="utf-8") as json_file:
                        json_file.write(json.dumps(data, ensure_ascii=False))
                        json_file.write("\n")

                counter += len(summaries)
                cnt = 0

counter = 0
current_directory = "/content/text-ar-dataset-json/essex-code/data"

with open("/content/text-ar-dataset-json/jsons/essex.jsonl", "w") as file:
    file.truncate(0)

for folder_name in sorted(os.listdir(current_directory)):
    folder_path = os.path.join(current_directory, folder_name)

    if os.path.isdir(folder_path):
        organize_files(folder_path)

print("File conversion to JSONL completed.")

