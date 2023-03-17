"""""
TO-KNOW :
    -ce sera x (aleatoire) lettres choisies (aleatoirement) 
    -dexuieme fonctionnalité sera que on peut choisir son captcha 
TO-DO :
    -choisir la police 
    voir : https://www.dafont.com/ordionally.font,https://www.dafont.com/wasiat.font,https://www.dafont.com/bongkerspop.font, https://www.dafont.com/love-in-the-sky.font, https://www.dafont.com/nighty-tales-gt.font, https://www.dafont.com/witchi.font
    chercher une qui fais vrmt "fait main" 
    -choisir une methode pour rendre l'image dur a lire (il faut pouvoir passer outre), probablement filter de PIL pour gagner du temps 
    -voir si je veux les miniscules et les majuscules (ou un des deux, ou un mix des deux->en fct du dataset)
"""""
from PIL import Image,ImageDraw,ImageFont
import matplotlib.pyplot as plt
from random import choice, randint
from math import sin, ceil
def create_sequence_random():
    lettres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    nb_lettres = randint(3,7)
    sequence = ""
    for x in range(nb_lettres):
        lettre = choice(lettres)        
        sequence+=lettre
    return sequence
def filter(x,y):#ca sera juste distortion imo
    """""
    un pixel a des coordonées (x,y) et on doit les passer dans une fonction qui va nous donner des coordonnes(u,v), avec la meme couleur
    on peut faire un truc du genre fonction sinus pour la coordonné x
    ont peut faire un truc du genre fct sinus pour la coordonné y 
    le pixel ou ils étaient est remplace par un pixel blanc
    """""
    """""
    ca change souvent car les pixels ont de grandes valeur dcp sur l'image 10 pixels c pas grand chose dcp ca passe vite en negatif
    dcp leffet est pas etalé mais concentre a certains endroits et absent dans dautre
    il faut peut etre normaliser les pixels entre 0 et 30 par exemple 
    """""
    """""
    il reste des choses a regler : 
    -normalisation
    -remplacement des anciens pixels par des blancs
    """""
    """""
    x:
        quand sin(x) est negatif le pixel va vers la gauche 
        quand sin(x) est positif le pixel va vers la droite
    y(ne pas oublier que l'image est retourne):
        quand sin(y) est negatif le pixel va vers le bas
        quand sin(y) est positif le pixel va vers le haut
    """""
    #je sais pas vrmt ce quil faut faire ici 
    u = x #il faut laisser ca car ca se deplace pas sur les cotes mais ca monte et ca descend
    v = y+sin(y) #corespond a une fct du genre y-sin(y)
    return (ceil(u),ceil(v))
def genere_image_random():
    mot = create_sequence_random()
    mot = "a3fi"
    size_x = 1500 #on pourra passer ca en parametres
    size_y = 1000
    img = Image.new(mode="1",size=(size_x,size_y),color=1)#voir apres pour size
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype(r"C:\Users\dnybs\trophee NSI\image_generation\fonts\Wasiat v.2.otf",size = 250)#voir apres pour size (en fct des données)
    draw.text((500,250),text = mot,fill = 0, font= fnt, spacing = 5)#choisi le milieu en y et le debut en x
    img.show()
    #distortion
    for y in range(size_y):
        for x in range(size_x):
            if img.getpixel((x,y)) == 0:
                u,v = filter(x,y)
                #print('ancien coor: ',(x,y) ,"\n nouveau coor :",(u,v))
                if u != size_x and v!= size_y:
                    img.putpixel((u,v),0) #met le nv pixel  
                    #img.putpixel((x,y),1)
    img.putpixel((900,100),0)
    #img.show()
    #for pixel_coor in pixels_changes: #remplace par un pixel blanc lancien 
    #    img.putpixel((pixel_coor[0],pixel_coor[1]),0)
    img.show()
    #ein barriere ein barricade
    #print(mot)
genere_image_random()







def genere_image_chosen(mot):
    mot = input("choisi un mot :")
    print(mot)
    return 0
