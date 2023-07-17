import sys


def txt_importer(path_file):
    if ".txt" not in path_file:
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            text = file.read()
            text_list = text.split("\n")
            return text_list
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
