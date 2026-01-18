def save_str_to_file(file_name: str,
                     content: str):
    with open(file_name, 'w') as f:
        f.write(content)
