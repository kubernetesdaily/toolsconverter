import pandas as pd
import json

def convert_excel_to_js(excel_path, js_path):
    # Read the Excel file
    df = pd.read_excel(excel_path)

    # Convert the DataFrame to a list of dictionaries
    data_list = df.to_dict(orient='records')

    # Convert the list of dictionaries to a JSON formatted string
    json_data = json.dumps(data_list, indent=2)

    # Prepare the content to be written to a JS file
    js_content = f"const entries = {json_data};\n"

    # Write the JSON data to a .js file with a JavaScript variable assignment
    with open(js_path, 'w') as js_file:
        js_file.write(js_content)

    print(f"Data has been written to {js_path}")

# The paths to the Excel file and the output JS file
excel_file_path = './cloudnativetools.xlsx'  # Replace with your actual Excel file path
js_file_path = 'entries.js'  # Replace with your desired JS file path

# Run the conversion
convert_excel_to_js(excel_file_path, js_file_path)