import webbrowser

print("#######################")
print("###ABRE##SUA##MUSICA###")
print("#######################")


musica = input("Qual sua musica favorita?:")

print("Aonde você quer escutar? (escolhendo o número")
print("1-Spotify")
print("2-Deezer")
print("3-Youtube")
print("4-Letras")

escutar_onde = int(input("Defina aonde:\n"))

if (escutar_onde <= 0 or escutar_onde >= 5):
    print("Escolha um número entre 1 e 4")
    print("1-Spotify")
    print("2-Deezer")
    print("3-Youtube")
    print("4-Letras")

    escutar_onde = int(input("Defina aonde:\n"))


if (escutar_onde == 1):
        new = 2
        url = ("https://open.spotify.com/search/" + musica)
        webbrowser.open(url, new=new)
        print("###########################")
        print("Obrigado por usar nosso app")
        print("###########################")
elif (escutar_onde == 2):
        new = 2
        url = ("https://www.deezer.com/search/" + musica)
        webbrowser.open(url, new=new)
        print("###########################")
        print("Obrigado por usar nosso app")
        print("###########################")
elif (escutar_onde == 3):
        new = 2
        url = ("https://www.youtube.com/results?search_query=" + musica)
        webbrowser.open(url, new=new)
        print("###########################")
        print("Obrigado por usar nosso app")
        print("###########################")
elif (escutar_onde == 4):
        new = 2
        url = ("https://www.letras.com/?q=" + musica)
        webbrowser.open(url, new=new)
        print("###########################")
        print("Obrigado por usar nosso app")
        print("###########################")