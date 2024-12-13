# Convert UTF-16 to UTF-8
input_file = "db_backup.json"
output_file = "fixed_db_backup.json"

# Use the correct encoding detected
source_encoding = "utf-16"

with open(input_file, "r", encoding=source_encoding) as infile:
    content = infile.read()

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(content)

print("File successfully converted to UTF-8!")
