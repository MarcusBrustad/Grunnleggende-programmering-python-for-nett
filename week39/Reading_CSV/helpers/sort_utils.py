# Denne fila heter: "sort_utils" .py


def sort_by_key(data: list[dict], my_key:str) -> list[dict]:
    return sorted(data, key=dict.__getitem__(my_key))


def sort_by_name(data: list[dict]):
    """Sorter listen med dictionaries etter navn. """
    return sorted(data, key=lambda x: x["Navn"])

def sort_by_age(data: list[dict]):
    return sorted(data, key=lambda persondictionary: persondictionary["Alder"])


def get_name_from_dict_row(row: dict) -> str:
    return row["Navn"]

def sort_by_name_no_lambda(data):
    return sorted(data, key=get_name_from_dict_row)









# def sort_by_name_actually_no_lambda(data):
#     return sorted(data, key=str.__getitem__("Navn"))



