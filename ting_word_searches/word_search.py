from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    word_result = []
    for file in instance._queue:
        result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
            }
        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word.upper() in line.upper():
                result["ocorrencias"].append({"linha": i + 1})
        if not len(result["ocorrencias"]) == 0:
            word_result.append(result)
    return word_result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
