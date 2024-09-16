import os

def write_to_file(file_name, data):
    if not file_name:
        raise ValueError("The file name cannot be an empty string.")
    
    
    # Ensure the directory exists
    directory = os.path.dirname(file_name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)
    print(f"Attempting to write to: {file_name}")