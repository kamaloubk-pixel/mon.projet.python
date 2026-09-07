product=[]
print(product)
def ajout (a,b,c):
    z={"nom":a,"prix":b,"quant":c}
    product.append(z)
while True:
    a=input ("donner le nom svp")
    try:
        b=int(input("donner un prix svp"))
        c=int(input ("donner la quantité svp"))
    except:    
        print("veuillez entrer un nombre svp")
    ajout(a,b,c)
    x=input ("continuer?")
    if x!="oui":
        break
def affich():  
    if not product:
        print ("la liste est vide")
    else:
        for i in product:
            print(i["nom"],"-",i["prix"],"-","quant:",i["quant"])      

def cherche():
    m=input("entrez le nom du produit svp:")    
    for i in product:    
        if m ==i["nom"]:
            print (i)
            break
    else :
        print ("produit introuvable") 

def mod():
    m=input("entrez le nom du produit svp:")
    
    for i in product:    
        if m ==i["nom"]:
            try:
                q=int(input("mettez la nouvelle quantité svp"))
            except:
                print("veuillez entrer la quantité valide svp")    
            i["quant"]=q
            print (i["nom"],i["prix"],i["quant"])
            break
    else :
        print ("produit introuvable")
        

def valeur():
    t=0
    for i in product:
        t=t+i["prix"]*i["quant"]
    print (t)
def v():
    kam=open("produit.txt","w")    
    for i in product:
        kam.write(i["nom"]+" "+str(i["prix"])+" "+str(i["quant"])+"\n")
    kam.close ()

def lire():
    kam=open("produit.txt","r")
    print(kam.read())
    kam.close()    
def sup():
    pro=input("inserez le nom du produit svp")
    trouve=False
    for i in product:
        if pro==i["nom"]:
            product.remove(i)
            break
            trouve =True
        else:
            print ("produit introuvable")
choix =["1.ajouter un produit",
"2.afficher les produit",
"3.chercher un produit",
"4.modifier la quantité",
"5.valeur total du stock",
"6.sauvegarder",
"7.lire le fichier",
"8.suprimmer un produit",
"9.quitter"]
while True:
    for i in choix:
        print (i)
    try:    
        pop=int(input("que voulez vous faire"))
    except:   
        print ("veuillez entrer un nombre svp")    
        continue
    if pop =="1":
        ajout (a,b,c)
    elif pop =="2":
        affich()
    elif pop =="3":
        cherche()
    elif pop =="4":
        mod()
    elif pop =="5":
        valeur()
    elif pop =="6":
       v()
    elif pop =="7":
        lire()
    elif pop =="8":
        sup()
    elif pop =="9":
        print ("au revoir")
        break
print ("nv commit")