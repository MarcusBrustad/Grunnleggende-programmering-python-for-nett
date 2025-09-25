import helpers as h
from helpers.dict_utils import read_csv_manual

data = h.rcsv("personer.csv")

for p in data:
    print(p)
# data2 = h.rcsvcheating("personer.csv")
print("\nDette er for en ny linje\n")

data_sorted_by_age = h.sort_by_age(data)

for p in data_sorted_by_age:
    print(p)




# data_sorted_name = h.sname(data)
# for p in data_sorted_name:
#     print(p)

# data_sorted_by_key = h.skey(data, "Navn")
#
# for p in data_sorted_by_key:
#     print(p)

