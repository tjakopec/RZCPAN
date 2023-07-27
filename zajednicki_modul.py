def ulaz(poruka,tip):
    while True:
        try:
            return tip(input(poruka))
        except:
            print('Greška unosa')
