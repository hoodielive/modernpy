import PyPDF2
import json

# Open the PDF file
pdf_file_path = 'odu.pdf'
pdf_file = open(pdf_file_path, 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Initialize an empty dictionary to store the Odus
odus_data = {}

# Loop through each page and extract text
for page_number in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_number)
    text = page.extractText()
    
    # Split the text into Odus (assuming each Odu is separated by a specific delimiter)
    odu_statements = text.split("YOUR_DELIMITER_HERE")
    
    # Populate the dictionary with Odu statements
    odu_name = f"Odu_{page_number + 1}"
    odus_data[odu_name] = odu_statements

# Close the PDF file
pdf_file.close()

# Convert the dictionary to JSON
odus_json = json.dumps(odus_data, indent=4)

# Save the JSON data to a file
with open('odus_data.json', 'w') as json_file:
    json_file.write(odus_json)

print("PDF data has been converted to JSON.")

