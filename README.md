print( "\t")
print( "\t")

TYELLOW =  '\033[33m' # yellow Text
ENDC = '\033[m' # reset to the defaults




receptes = {
    "Omlete🥚": ["olas", "piens"],
    "Kēksiņi🧁": ["milti", "olas", "piens", "cepamais pulveris"],
    "Pankūkas🥞": ["milti", "piens", "olas"],
    "Karstā šokolāde🍫" : ["piens", "šokolāde"],
    "Cepumi🍪" : ["milti", "sviests", "cukurs"],
    "Kūka🍰": ["milti", "olas", "piens", "cepamais pulveris"],
    "Piena kokteilis🥛" : ["piens", "šokolāde"],
    "Olu kārtojums🥘" : ["olas, piens, cepamais pulveris, sviests"],
    "Donuts🍩" : ["olas, sviests, cukurs, piens, milti, raugs, soda"],
    "Saldējums🍦" : ["piens, saldais krējums, olas, cukurs"]


}

sastavdalas = input(f"Vēlies kaut ko uzēst, bet nav ideju? \nĻauj man palīdzēt! \nIevadi savas pieejamās sastāvdaļas no šīm - olas, piens, saldais krējums, milti, cepamais pulveris, sviests, šokolāde, raugs atdalot tās ar komatiem: ").split(",")

sastavdalas = [s.strip() for s in sastavdalas]

pielaujamās_receptes = []

for recepte, sastavdalas_recepte in receptes.items():
    if all(sastavdala in sastavdalas for sastavdala in sastavdalas_recepte):
        pielaujamās_receptes.append(recepte)


if pielaujamās_receptes:

    print("Jūs varat uztaisīt šādus ēdienus: ")
    for recepte in pielaujamās_receptes:
        print("- " + TYELLOW + recepte, ENDC)
else:
    print("Ar dotajām sastāvdaļām nevar uztaisīt nevienu ēdienu.")


link = "https://www.google.com/search?q=" 
search_query = input("Ja esi aradis/usi to ko sirds kāro, ļauj mums tev ātri un vinkārši atrast perfekto recepti, ieraksti to ēdienu, kurš no šiem tev visvairāk iet pie sirds: ") 
full_link = link + search_query.replace(" ", "+") 
print("Aktīvais links: " , full_link )


# search_query = input("Ja esi atradis/usi to ko sirds kāro, ļauj mums tev ātri un vinkārši atrast perfekto recepti, ieraksti to ēdienu, kurš no šiem tev visvairāk iet pie sirds:  ")
# google_search_url = "https://www.google.com/search?q="
# form_code = f'''
# <form action="{google_search_url}" method="get" target="_blank">
#     <input type="hidden" name="q" value="{search_query}">
#     <input type="submit" value="Uzspied šeit">
# </form>
# '''
# print(f"Aktīvais links: ", form_code)





print( "\t")






print( "\t")



def atrod_receptes(receptes, sastavdalas):
    pielaujamās_receptes = []
    for recepte, sastavdalas_recepte in receptes.items():
        if all(sastavdala in sastavdalas for sastavdala in sastavdalas_recepte):
            pielaujamās_receptes.append(recepte)
    return pielaujamās_receptes








print( "\t")
print( "\t")


def meklē_recepti_internetā():
    link = "https://www.google.com/search?q="
    search_query = input("Ievadi ēdienu, kurš tev gribētos pagatavot: ")
    full_link = link + search_query.replace(" ", "+")
    print("Aktīvais links: " , full_link)


