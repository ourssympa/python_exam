import os
import pyttsx3
import speech_recognition as sr
import matplotlib.pyplot as mp
def banner():
    text = ''' 
    
                _______  _______    _______       _______  _______  _______  __   
        |\     /|(  ____ \(  ___  )(  ___  )     / ___   )(  __   )/ ___   )/  \  
        | )   ( || (    \/| (   ) || (   ) |     \/   )  || (  )  |\/   )  |\/) ) 
        | |   | || |      | (___) || |   | | _____   /   )| | /   |    /   )  | | 
        | |   | || |      |  ___  || |   | |(_____)_/   / | (/ /) |  _/   /   | | 
        | |   | || |      | (   ) || |   | |      /   _/  |   / | | /   _/    | | 
        | (___) || (____/\| )   ( || (___) |     (   (__/\|  (__) |(   (__/\__) (_
        (_______)(_______/|/     \|(_______)     \_______/(_______)\_______/\____/
            
    
       "7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7"7_/"7_/"7_/"7_/"7_/"7_/"7    
       "7_/                BIENVENUE DANS NOTRE PROGRAMME ELLE RESUME               "7_/
       "7_/                 NOS ACQUIS DURANT LE COURS DE PYTHON A UCAO             "7_/
       "7_/                                  2021-2022                              "7_/
       "7_/                                                                         "7_/
       "7_/                                                                         "7_/
       "7_/          MENU :                                                         "7_/
       "7_/                                                                         "7_/
       "7_/      1:TAPEZ UNE COMMANDE                                                "7_/
       "7_/      2:LECTURE AUDIO DES TEXTES                                         "7_/
       "7_/      3:COMMANDE VOCALE                                                  "7_/
       "7_/      4:GESTION DE LA CLASSE
       "7_/      5:INFORMATION SUR LE SYSTEME
       "7_/                                                                         "7_/
       "7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7_/"7"7_/"7_/"7_/"7_/"7_/"7_                    

                                                                          
    '''
    return text
def info():
    os.system("clear")
    print(os.uname())
    a=input("pour retourner au menu principal faite 1")
    if a=="1":
        main()
    
def commande():
    os.system("clear")
    #demande de la commande
    cmd=input("entrer la commande :")
    #execution de la commande entrer
    os.system(cmd)
    quiter=int(input("voulez vous retourner au menu principal? si oui tapez 1\n"))
    if quiter==1:
        main()

def reader():
    os.system("clear")
    
    saisie=input(''' 
        Menu:
        1 : pour faire lire un text 
        2 : pour faire lire un document
        3 : pour retourner au menu principal 
    ''')
    if(saisie=="1"):
        #ici on demande à l'utilisateur d'entrer un text qui est lu
        text=input("veuillez entre le text a lire :\n")
        #initialisation de la librairie
        engine = pyttsx3.init()
        #fonction de lecture du text
        engine.say(text)
        engine.runAndWait()
        reader()
    elif (saisie=="2"):
        poeme=input(''' 
        pour ecouter
        1 : demain dés l'aube
        2 : amour 
    ''')
        if(poeme=="1"):
            with open('demain.txt',encoding='utf8') as f:
                engine = pyttsx3.init()
                engine.say(f.read())
                engine.runAndWait()
                
                reader()
        elif(poeme=="2"):
            with open('amour.txt',encoding='utf8') as f:
                engine = pyttsx3.init()
                engine.say(f.read())
                engine.runAndWait()
                reader()
        else:
            print("mauvais choix")
            reader()
    elif (saisie=="3"):
        main()
    else:
        a=input("mauvais choix 1 pour retourner au menu principal et 0 pour le sous menu des lectures")
        if(a=="1"):
            main()
        elif(a=="0"):
            reader()
        else:
            print("mauvais choix!!!!")
            reader()
            
            
def recognition():
    #initialisation de la librairie
    var = sr.Recognizer()
    #mise en écoute du micro
    with sr.Microphone()as source:
        print(source)
        var2=var.listen(source)
    #traduction de la prise audio en text
    var3 = var.recognize_google(var2)
    print(var3)
    if ("code" in var3):
        os.system("code")
    elif("Firefox" in var3):
        os.system("firefox")
    else:
        print("commande non definie")
    retour = input("voulez vous retourner au menu principal si oui tapez 1 !!!")
    if (retour=="1"):
        main()
        
        
def classe1():
    classe(data=[])    

def classe(data):
    type=["M","F","f","m"]
    os.system("clear")
    liste=data
    select=input(''' 
        Gestion de classe
        1 -) affichez la liste des etudiants
        2 -)ajoutez des etudiants
        3 -)affichez les statistiques
    ''')
    def add(nom,prenom,sexe,note):
        liste.append([nom,prenom,sexe,note])
            
    if(select=="1"):
        if(len(liste)==0):
            print("la liste de la classe est vide pour le moment veuillez ajouter des etudiants")
            nbr=int(input("combien d'etudiant voulez vous ajouter?\n"))
            for i in range(nbr):
                nom=input("nom.....")
                prenom=input("prenom.....")
                sexe =input("sexe.....")
                while sexe not in type:
                  sexe=input("sexe.....")
                note=input("note.....")
                add(nom,prenom,sexe,note)
            print(liste)
            ab=input("\n voulez vous retournez au sous menu? si oui tapez 0 sinon tapez autre chose ")
            if(ab=="0"):
                classe(liste)
            else:
                main()
        else:
            print(liste)
            ab=input("\n voulez vous retournez au sous menu? si oui tapez 0 sinon tapez autre chose ")
            if(ab=="0"):
                classe(liste)
            else:
                main()
    elif(select=="2"):
        nbr=int(input("combien d'etudiant voulez vous ajouter ?"))
        for i in range(nbr):
            nom=input("nom.....")
            prenom=input("prenom.....")
            sexe =input("sexe.....")
            while sexe not in type:
              sexe=input("sexe.....")
            note=input("note.....")
            add(nom,prenom,sexe,note)
        print(liste)
        ab=input("\n voulez vous retournez au sous menu? si oui tapez 0 sinon tapez autre chose ")
        if(ab=="0"):
            classe(liste)
        else:
            main()
    elif(select=="3"):
        notes=[]
        noms=[]
        if(len(liste)==0):
            print("liste vide veuillez renseignez les informations svp!!!")
            classe1()
        else:

          for i in range(len(liste)):
            notes.append(liste[i][3])
            noms.append(liste[i][0])
          print(noms)
          print(notes)
          mp.bar(noms,notes,align='center')
          mp.show()
          
def menu(choix):
    # ici le switcher pour selectionner les options
    switcher = {
        1 :commande,
        2 :reader,
        3 :recognition,
        4 :classe1,
        5 :info
       
    }
    return switcher.get(choix,"votre entrer est invalide!!!!!")

#ici c est la fonction principale
def main():
    #ligne permet de vider le terminale
    os.system("clear")
    print(banner())
    #appel de la fonction output permettant de switcher
    choix=int(input("votre choix :\n"))
    output=menu(choix)
    output()
    
    
main()