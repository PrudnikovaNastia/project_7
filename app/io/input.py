import pandas as pd


"""
    Function for inputting text from the console.

    Returns:
        str: The text entered by the user.
    """
def input_text():
    text = input("Enter text: ")
    return text

"""
    Function for reading from a file using Python's built-in capabilities.

    Parameters:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file or None if the file is not found.
    """
def read_file_builtin(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None

"""
    Function for reading from a file using the Pandas library.

    Parameters:
        file_path (str): The path to the file.

    Returns:
        pandas.DataFrame or None: DataFrame of the read data or None if the file is not found.
"""
def read_file_with_pandas(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None