import fitz
import json
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def process_folder(root_dir):
    data = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(subdir, file)
                print(f"Processing file: {pdf_path}")
                text = extract_text_from_pdf(pdf_path)
                item = {
                    "product_name": os.path.basename(subdir),
                    "category": os.path.basename(os.path.dirname(subdir)),
                    "section": os.path.basename(os.path.dirname(os.path.dirname(subdir))),
                    "description": text,
                    "pdf_path": pdf_path,
                    "images": [],
                }
                data.append(item)
    return data

data = process_folder(r"E:\sales\LLM_")

# Checking if data is extracted successfully
print(f"Extracted {len(data)} items.")

with open(r"E:\sales\generic app\data.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("data.json created successfully.")
