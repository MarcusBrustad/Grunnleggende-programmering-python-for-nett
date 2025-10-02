#Eksempel på decoratorer


#--------------------------------------------------------------------------------#
def si_hei():
    print("Hei!")

#Uten decorator.
def si_hei_med_logging():
    print("🔵 Kjører funksjonen...")
    print("Hei!")
    print("🔵 Ferdig!")

si_hei_med_logging()

# logging men med decorator:
def logging_decorator(func):
    """
    En decorator som legger til logging rundt en funksjon.

    func = funksjon vi vil "pakke inn"
    """
    def wrapper():
        print("🔵 Kjører funksjonen...")
        func() # Kjører den originale funksjonen
        print("🔵 Ferdig!")
    return wrapper

# Måte 1 å bruke dette: manuell bruk av decorator
si_hei = logging_decorator(si_hei)
si_hei()

# Måte 2 med @ syntaks. (Dette er vanligste måten / best practice)
@logging_decorator
def si_hallo():
    print("Hallo!")

si_hallo()



# Med mulighet til å legge inn variabel tekst i print.
def oppgave_decorator(oppgave_navn):
    """
    Decorator som tar parametere
    """
    def decorator(func):
        def wrapper():
            print(f"\n{'='*50}")
            print(f"Kjører oppgave: {oppgave_navn}")
            print('='*50)
            func()
            print()
        return wrapper
    return decorator

@oppgave_decorator("5A")
def oppgave_5a():
    print("Regner ut total forlengelse...")
    print("Resultat: 123 dager for eks")

@oppgave_decorator("5B")
def oppgave_5b():
    print("Teller bøker per sjanger...")
    print("Fantasy: 10, Krim: 15")

oppgave_5a()
oppgave_5b()