print( "\t")
print( "\t")

def atrod_receptes(receptes, sastavdalas):
    pielaujamās_receptes = []
    for recepte, sastavdalas_recepte in receptes.items():
        if all(sastavdala in sastavdalas for sastavdala in sastavdalas_recepte):
            pielaujamās_receptes.append(recepte)
    return pielaujamās_receptes

TYELLOW = '\033[33m' 
ENDC = '\033[m' 

receptes = {
    "Omlete🥚": ["olas", "piens"], 
    "Kēksiņi🧁": ["milti", "olas", "piens", "cepamais pulveris"], 
    "Pankūkas🥞": ["milti", "piens", "olas"], 
    "Karstā šokolāde🍫" : ["piens", "šokolāde"], 
    "Cepumi🍪" : ["milti", "sviests", "cukurs"], 
    "Kūka🍰": ["milti", "olas", "piens", "cepamais pulveris"], 
    "Piena kokteilis🥛" : ["piens", "šokolāde"], 
    "Olu kārtojums🥘" : ["olas", "piens", "cepamais pulveris", "sviests"], 
    "Donuts🍩" : ["olas", "sviests", "cukurs", "piens", "milti", "raugs", "soda"], 
    "Saldējums🍦" : ["piens", "saldais krējums", "olas", "cukurs"]
}

sastavdalas = input("Vēlies kaut ko uzēst, bet nav ideju? \nĻauj man palīdzēt! \nIevadi savas pieejamās sastāvdaļas no šīm - olas, piens, saldais krējums, milti, cepamais pulveris, sviests, šokolāde, raugs atdalot tās ar komatiem: ").split(",")
sastavdalas = [s.strip() for s in sastavdalas]

pielaujamās_receptes = atrod_receptes(receptes, sastavdalas)

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
