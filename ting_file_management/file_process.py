from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    new_list = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(new_list),
        "linhas_do_arquivo": new_list,
        }
    for dict in instance._queue:
        if path_file == dict["nome_do_arquivo"]:
            return
    instance.enqueue(new_dict)
    print(new_dict)


def remove(instance: Queue):
    if len(instance) == 0:
        print("Não há elementos")
        return
    file_to_remove = instance.dequeue()["nome_do_arquivo"]
    if (file_to_remove):
        print(f"Arquivo {file_to_remove} removido com sucesso")


def file_metadata(instance: Queue, position):
    try:
        file_search = instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
        return
    print(file_search)
