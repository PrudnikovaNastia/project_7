from app.io.input import input_text, read_file_builtin, read_file_with_pandas
from app.io.output import output_text, write_to_file

def main():
    text = input_text()

    output_text(text)

    write_to_file("output.txt", text)

    print("Function for reading from a file using Python's built-in capabilities"+read_file_builtin("output.txt")+" ")
    print(read_file_with_pandas("output.txt"))

if __name__ == '__main__':
    main()