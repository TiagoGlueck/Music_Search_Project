import webbrowser


print("##################")
print("SEARCH#YOUR#MUSIC")
print("##################")


musica = input("What is your favorite song?:\n")

print("where do you want to listen? (please select the number)")
print("1-Spotify")
print("2-Deezer")
print("3-Youtube")
print("4-Letras")

escutar = int(input("Where?:\n"))

if (escutar <= 0 or escutar >= 5):
    print("Choose the number between 1 and 4")
    print("1-Spotify")
    print("2-Deezer")
    print("3-Youtube")
    print("4-Letras")

if (escutar == 1):
            new = 2
            url = ("https://open.spotify.com/search/" + musica)
            webbrowser.open( url, new=new )



elif (escutar == 2):
    new = 2
    url = ("https://www.deezer.com/search/" + musica)
    webbrowser.open(url, new=new)


elif (escutar == 3):
    new = 2
    url = ("https://www.youtube.com/results?search_query=" + musica)
    webbrowser.open(url, new=new)


elif (escutar == 4):
    new = 2
    url = ("https://www.letras.com/?q=" + musica)
    webbrowser.open(url, new=new)
