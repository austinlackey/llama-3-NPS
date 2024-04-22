import pandas as pd
import jsonlines

def excel_to_jsonl(excel_file, jsonl_file):
    # Read Excel file into pandas DataFrame
    df = pd.read_excel(excel_file)
    
    # Open JSONL file for writing
    with jsonlines.open(jsonl_file, mode='w') as writer:
        # Iterate through each row in the DataFrame
        for index, row in df.iterrows():
            # Extract prompt and completion from the current row
            prompt = str(row.iloc[0])  # First column
            completion = str(row.iloc[1])  # Second column
            
            # Write JSON object to JSONL file
            writer.write({"prompt": prompt, "completion": completion})

# Provide the paths to your Excel and JSONL files
excel_file = 'data.xlsx'
jsonl_file = 'Data/output.jsonl'

# Call the function to convert Excel to JSONL
excel_to_jsonl(excel_file, jsonl_file)

print("Conversion complete.")
