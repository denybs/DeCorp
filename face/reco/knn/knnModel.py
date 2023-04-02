"""
il faut que :
-le dataset soit une liste des lignes de liste des colonnes (features) de taille (nLignes,mColones)
-les targets soient dans une liste séparé 
-les donnes de la classe inconnue doivent etre sous forme d'une liste contenant une ligne et les colonnes de taille (1,mColonnes) 
"""
def calculDistance(firstElement, secondElement):#firstelElement est la liste de features du premier element et same for secondElement
    distance = 0
    for value1, value2 in zip(firstElement,secondElement):
        distance+=abs(value1-value2) #metrique de Manathan
    return distance
def determineClass(kNearest,labels):
    classesIndex=[]
    smallestDistance = min(kNearest)
    for element in kNearest:
        classesIndex.append(element[1])       
    classes= []
    for i in classesIndex:
        classes.append(labels[i])
    classesSansDuplique= []
    for element in classes:
        if element not in classesSansDuplique:
            classesSansDuplique.append(element)
    classeOccur=[]
    for classe in classesSansDuplique:
        classeOccur.append(classes.count(classe))
    
    if len(classeOccur)==1:
            nearest = classesSansDuplique[classeOccur.index(max(classeOccur))]
    else:
        for i in range(len(classeOccur)-1):#quand les kNearest sont tous de classes differentes il faut faire une exception en prenant le plus proche des kNearest
            if classeOccur[i] == classeOccur[i+1]:
                nearest = labels[smallestDistance[1]]
            else:
                nearest = classesSansDuplique[classeOccur.index(max(classeOccur))]
    return nearest
        
def knn(classeInconnue,features,labels,k): #on considere que classeInconnue et les colonnes du dataset sont les memes tailles
    kNearest = []
    for feature in features:
        distance = calculDistance(classeInconnue,feature)
        kNearest.append((distance,features.index(feature)))
    kNearest.sort(reverse= True)
    kNearest = kNearest[len(kNearest)-k:]
    pred = determineClass(kNearest,labels)
    return pred