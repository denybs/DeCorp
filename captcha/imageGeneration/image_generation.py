from PIL import Image,ImageDraw,ImageFont
from random import choice, randint
from math import sin, ceil
def create_sequence_random():
    lettres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    nb_lettres = randint(8,9)
    sequence = ""
    for x in range(nb_lettres):
        lettre = choice(lettres)  
        lettre = choice([lettre,lettre.upper()])   #choisi entre la lettre et sa majuscule (les nombres restent comme ils sont)   
        sequence+=lettre
    return sequence

def genere_image(mot, size_x, size_y, posX,posY,fnt):
    img = Image.new(mode="1",size=(size_x,size_y),color=1)#voir apres pour size
    draw = ImageDraw.Draw(img)
    draw.text((posX,posY),text = mot,fill = 0, font= fnt, spacing = 5)#pour que la variation sois pas tout le temps la meme
    return img

#ce filter a les amelioration du 2 + on distord sur les deux axes mais ducoup il faut faire ca l'un apres l'autre !
def filter(image,size_x,size_y):#ca sera juste distortion imo
#on veut distordre d'abord sur les x puis les y(on sen fout de lordre mais faut faire l'un apres lautre)
    for i in range(2):
        pixels_a_modifier = [] 
        for y in range(size_y):
            for x in range(size_x):
                if image.getpixel((x,y)) == 0:
                    pixels_a_modifier.append([x,y])
        for pixel_coor in pixels_a_modifier: #remplace par un pixel blanc mtn, pour ne pas supprimer ceux qu'on va mettre et qui sont la
            image.putpixel((pixel_coor[0],pixel_coor[1]),1)
        if i ==0: #distordre sur les y
            for p in pixels_a_modifier:
                x,y = p[0],p[1] 
                u = x 
                v = y-sin(x/100)*35 #corespond a une fct : v = f(x) = y+sin(x) SIN(X) PEUT ETRE NEGATIF
                #on peut tjrs changer le coeff de sin(x), le coeef de x
                u,v = ceil(u),ceil(v)
                if u <= size_x and v <= size_y:
                    image.putpixel((u,v),0)

        if i ==1: #distordre sur les x
            for p in pixels_a_modifier:
                x,y = p[0],p[1] 
                u = x +sin(y/50)*20
                v = y #corespond a une fct : v = f(x) = y+sin(x) SIN(X) PEUT ETRE NEGATIF
                #on peut tjrs changer le coeff de sin(y), le coeef de y
                u,v = ceil(u),ceil(v)
                if u <= size_x and v <= size_y:
                    image.putpixel((u,v),0)

def resizeImage(img,bord):
    largeur, hauteur = img.size
    #il faut couper sur les 4 cotes (en hauteur en haut et en bas, en largeur a droite et a gauche)
    #pour obtenir un rectangle : (largeur gauche,hauteur haut,largeur droite,hauteur bas)
    #en hauteur :
    #en bas : on sait a peu pres 
    for i in reversed(range(hauteur)):#on part du bas
        for j in range(largeur):#de gauche a droite
            if img.getpixel((j,i)) == 0:
                hauteurBas = i +bord
                break
        else:
            continue
        break                    
    #en haut : on sait a peu pres
    for i in range(hauteur):#on part du haut
        for j in range(largeur):#de gauche a droite
            if img.getpixel((j,i)) == 0:
                hauteurHaut = i-bord
                break
        else:
            continue
        break                    
    #en largeur:

    #a gauche : on sait a peu pres
    for j in range(largeur):#on part de la gauche
        for i in range(hauteur):#de haut en bas
            if img.getpixel((j,i)) == 0:
                largeurGauche = j-bord
                break
        else:
            continue
        break

    #a droite :

    for j in reversed(range(largeur)):# on part de la droite
        for i in range(hauteur):#de haut en bas
            if img.getpixel((j,i)) == 0:
                largeurDroite = j+bord
                break
        else:
            continue
        break
    img = img.resize(size = (largeurDroite,hauteurBas),box =(largeurGauche,hauteurHaut,largeurDroite,hauteurBas))
    return img

#on met le noise par dessus l'autre sinon le resize va etre bizarre
def noise(image,size_x,size_y,nbPoint,fnt):
    randomPose = [[(randint(-250,size_x), randint(-250,size_y)) for i in range(nbPoint)] for j in range(0,size_y,80)] #un tableau de toutes les positions tous les 80 pixels ver le bas et aleatoire vers sur x et y
    draw = ImageDraw.Draw(image)

    for j in randomPose:
        for coor in j:
            draw.text(coor,text = '.',fill = 0, font= fnt, spacing = 5)  

    return image

def save(image,nom,format):
    image.save('C:\\DeCorp\\'+nom+format,format.upper())

def genere_image_random(x):
    size_x = 2100 #on pourra passer ca en parametres
    size_y = 700
    posX =randint(50,200) #position du pixel le plus proche de la gauche
    posY =randint(60,300) 
    fnt = ImageFont.truetype(r"captcha\imageGeneration\fonts\Bongkerspop.ttf",size = 250)
    for i in range(x):
        mot = create_sequence_random()
        print(mot)
        img = genere_image(mot, size_x,size_y,posX,posY,fnt)
        img = resizeImage(img,60)
        size_x,size_y = img.size[0],img.size[1]
        filter(img,size_x,size_y)  
        img = noise(img,size_x,size_y,5,fnt) 
        img.show()
        #save(img,mot,'png') pour enregistrer sur l'ordi de l'utilisateur si il le veut (bouton)

genere_image_random(1)