import os
from docx import Document
from docx2pdf import convert
from pathlib import Path

def convert_all_dotx(source_folder, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for file in os.listdir(source_folder):
        if file.lower().endswith("dotx"):
            input_path = os.path.join(source_folder, file)
            new_name = file[:-4] + "docx"
            output_path = os.path.join(target_folder, new_name)

            document = Document(input_path)
            document.save(output_path)
            print("Converted:", file, "to:", new_name)

def convert_docx_folder_to_pdf(input_folder_path, output_folder_path):
    input_folder = Path(input_folder_path)
    output_folder = Path(output_folder_path)
    output_folder.mkdir(parents=True, exist_ok=True)

    convert(str(input_folder), str(output_folder))
    print("Batch conversion complete.")

if __name__ == "__main__":
    source_folder = "/Users/sooreoluwa/Downloads/daniel"
    target_folder = "/Users/sooreoluwa/Downloads/converted-pdf"
    convert_docx_folder_to_pdf(source_folder, target_folder)
