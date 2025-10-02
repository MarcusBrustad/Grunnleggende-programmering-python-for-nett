import csv
def validate_int(value):
    """Sjekker om en verdi er et positivt heltall"""
    try:
        num = int(value)
        return num >= 0
    except:
        return False

def validate_genre(genre):
    """Sjekker om sjangeren er gyldig"""
    valid = ['Fantasy', 'Krim', 'Fiksjon', 'Sakprosa']
    return genre in valid

def validate_returned(returned):
    """Sjekker om returned-status er gyldig"""
    return returned in ['Ja', 'Nei']





titles = []
first_names = []
last_names = []
genres = []
loan_periods = []
extensions = []
returned_list = []

errors = []

with open('bokutlån.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row_num, row in enumerate(reader, start=2):  # Start på 2 (rad 1 er header)
        # # Valider data
        # if not validate_int(row['Låneperiode']):
        #     errors.append(f"Rad {row_num}: Ugyldig låneperiode '{row['Låneperiode']}'")
        #     continue
        # if not validate_int(row['Forlenget']):
        #     errors.append(f"Rad {row_num}: Ugyldig forlengelse '{row['Forlenget']}'")
        #     continue
        # if not validate_genre(row['Sjanger']):
        #     errors.append(f"Rad {row_num}: Ugyldig sjanger '{row['Sjanger']}'")
        #     continue
        # if not validate_returned(row['Tilbakelevert']):
        #     errors.append(f"Rad {row_num}: Ugyldig status '{row['Tilbakelevert']}'")
        #     continue

        #If everything is ok. Legg til data i listene.
        titles.append(row['Boktittel'])
        first_names.append(row['Fornavn'])
        last_names.append(row['Etternavn'])
        genres.append(row['Sjanger'])
        loan_periods.append(int(row['Låneperiode']))
        extensions.append(int(row['Forlenget']))
        returned_list.append(row['Tilbakelevert'])

print(f"✅ Leste inn {len(titles)} gyldige bøker")
print(f"❌ Fant {len(errors)} feil")
if errors:
    print("\nFørste 3 feil:")
    for error in errors[:3]:
        print(f"  {error}")

genre_count = {}
for i in range(len(titles)):
    if returned_list[i] == "Nei":
        genre_count[titles[i]] = genre_count.get(genres[i], 0) + 1