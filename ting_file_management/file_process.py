from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
