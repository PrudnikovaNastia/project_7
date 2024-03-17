"""
    Function for outputting text to the console.

    Parameters:
        text (str): The text to be outputted to the console.
"""

def output_text(text):
    print(text)

"""
    Function for writing to a file using Python's built-in capabilities.

    Parameters:
        file_path (str): The path to the file.
        content (str): The content to be written to the file.
"""
def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print("Записано у файл:", file_path)
    except Exception as e:
        print("Помилка під час запису у файл:", str(e))
