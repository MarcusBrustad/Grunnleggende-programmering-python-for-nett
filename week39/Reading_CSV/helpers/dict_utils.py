import csv
def read_csv_manual(filename: str) -> list[dict]:
    """
    Les en csv fil og retunrere en liste med dicts (hver rad = et dict).
    :param filename: navnet på csv fil.
    :return: Liste med dictionaries.
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines: list[str] = f.readlines()

        # nøkkel
        keys = lines[0].strip().split(",")

        data: list[dict[str,str]] = []
        #henter ut verdier for key-value pair
        for line in lines[1:]:
            values: list[str] = line.strip().split(",")
            row: dict[str, str] = dict(zip(keys, values))
            data.append(row)
        return data

def read_csv_as_dicts(filename: str) -> list[dict]:
    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

