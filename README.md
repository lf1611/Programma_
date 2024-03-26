# Programma_

link = "https://www.google.com/search?q="
search_query = input("Ievadi meklēšanas vaicājumu: ")
full_link = link + search_query.replace(" ", "+")
print("Aktīvais links: ", full_link)



search_query = input("Ievadi meklēšanas vaicājumu: ")
google_search_url = "https://www.google.com/search?q="
full_url = f'<a href="{google_search_url}{search_query.replace(" ", "+")}">Uzspied šeit'
print("Aktīvais links: ", full_url)



search_query = input("Ievadi meklēšanas vaicājumu: ")
google_search_url = "https://www.google.com/search?q="
full_url = f'<a href="{google_search_url}{search_query.replace(" ", "+")}">Uzspied šeit</a>'
print("Aktīvais links: ", full_url)
