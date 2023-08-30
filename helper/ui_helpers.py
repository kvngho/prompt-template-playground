import settings

def get_tokenizer_list():
    return [instance.Meta.name for instance in settings.TOKENIZER_CLASSES]