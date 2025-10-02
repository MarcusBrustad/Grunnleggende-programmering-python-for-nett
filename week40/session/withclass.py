import csv


class Book:

    VALID_GENRES = ['Fantasy', 'Krim', 'Fiksjon', 'Sakprosa']
    VALID_RETURNED = ['ja', 'nei']

    @staticmethod
    def validate_int(value):
        try:
            num = int(value)
            return num >= 0
        except:
            return False

    @staticmethod
    def validate_genre(genre):
        return genre in Book.VALID_GENRES

    @staticmethod
    def validate_returned(returned):
        return returned.lower() in Book.VALID_RETURNED



    def __init__(self, first_name, last_name, title, genre,
                 loan_period, extended, returned):
        if not self.validate_int(loan_period):
            raise ValueError(f"Ugyldig låneperiode: {loan_period}")
        if not self.validate_int(extended):
            raise ValueError(f"Ugyldig forlengelse: {extended}")
        if not self.validate_genre(genre):
            raise ValueError(f"Ugyldig sjanger: {genre}")
        if not self.validate_returned(returned):
            raise ValueError(f"Ugyldig status: {returned}")


        # Hvis valideringer == ok
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.genre = genre
        self.loan_period = int(loan_period)
        self.extended = int(extended)
        self.returned = returned

    def __str__(self):
        return f'Boken: "{self.title}", ble lånt av: {self.first_name} {self.last_name}'

    def total_loan_days(self):
        """Beregner total lånetid inkl. forlengelse"""
        return self.loan_period + self.extended

    def is_overdue(self):
        """Sjekker om boken ikke er levert tilbake"""
        return self.returned == "Nei" # Får her ut en bool, true hvis ikke er levert. False hvis den er returnert.

    def full_name_borrower(self):
        """Returnerer fullt navn på låner"""
        return f"{self.first_name} {self.last_name}"


books = []
errors_count = 0

with open('bokutlån.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            book = Book(
                first_name=row['Fornavn'],
                last_name=row['Etternavn'],
                title=row['Boktittel'],
                genre=row['Sjanger'],
                loan_period=row['Låneperiode'],
                extended=row['Forlenget'],
                returned=row['Tilbakelevert'])
            books.append(book)
        except ValueError:
            errors_count += 1



# Under her ligger testing gjort underveis.
# --------------------------------------------------------------------------------------------------------------------#

# try:
#     good_book = Book("Kari", "Hansen", "Snømannen", "Krim", 14, 0, "Ja")
#     print(f"  ✅ {good_book}")
# except ValueError as e:
#     print(f" ❌Feil: {e}")
#
#
# try:
#     bad_book = Book("Per", "Jensen", "Test", "Science Fiction", 14, 0, "Nei")
#     print(f"  ✅ {bad_book}")
# except ValueError as e:
#     print(f"  ❌ Validering stoppet: {e}")


# print(f"✅ Leste inn {len(books)} gyldige bøker")
# print(f"❌ Hoppet over {errors_count} ugyldige rader")
# print()
#
# print("Skal se total antall extended data for alle bøker")
# total_summed = 0
# for book in books:
#     total_summed += book.extended
# print(f"5A) Total forlengelse: {total_summed} dager")
# print()
#
#
# print("Antall bøker per sjanger")
# genre_count = {}
#
# for book in books:
#     if book.is_overdue():
#         genre_count[book.genre] = genre_count.get(book.genre, 0) +1
#
#
#
# print("Resultat")
# for genre, count in genre_count.items():
#     print(f"{genre}: {count}")
# print()