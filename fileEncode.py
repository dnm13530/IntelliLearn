import chardet

# Detect file encoding
with open("fixed_db_backup.json", "rb") as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    print(f"Detected encoding: {result['encoding']}")
