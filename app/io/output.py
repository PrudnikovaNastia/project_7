def output_text(text):
    print(text)

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print("Записано у файл:", file_path)
    except Exception as e:
        print("Помилка під час запису у файл:", str(e))
