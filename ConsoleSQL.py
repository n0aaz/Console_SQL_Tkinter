from tkinter import *
import sqlite3 as sql
import pandas as pd

# Exécute une commande SQL et renvoie sa sortie sous forme de chaine de caracteres
def executerCommandeSQL(commande):
    # On initialise la connection
    connectSQL = sql.connect('C:/Users/Melvin/Desktop/database.db')

    # On va exécuter la commande grâce à pandas et la fonction read_sql_query()
    sortieDataFrame = pd.read_sql_query(commande,connectSQL)

    # Par défaut Pandas nous retourne pas du texte affichable , il faut le convertir en chaine de caracteres
    sortieTexte = sortieDataFrame.to_string()
    return sortieTexte

# Quand un bouton est appuyé , cette fonction va se lancer
def changerVariable():
    # On va récupérer la commande qui a été écrite par l'utilisateur 
    commande = variableCommande.get()

    # On exécute cette commande: 
    texteSortie= executerCommandeSQL(commande)

    # On écrit la réponse de la commande dans la variable de réponse qui est toujours affichée
    reponse.set(texteSortie)

# Fenetre principale : 
window= Tk()
window.title('Requetes SQL : ')

# Initialiser des StringVar pour pouvoir stocker des chaines de caractères variables
# c'est à dire que si on les modifie, le changement sera immédiatement visible partout
# où elles sont utilisées.
reponse = StringVar()
reponse.set("Ici le retour")

labelReponse= Label(window, textvariable=reponse,justify=LEFT) 
# justify=LEFT nous permet de justifier le tableau texte à gauche, par défaut c'est au centre et c'est pas très joli
labelReponse.pack(side=TOP)
# on va coller cette case de label en haut de notre fenetre.

# là où on va écrire notre commande
variableCommande = StringVar()
variableCommande.set('Votre commande')

saisieCommande=Entry(window,textvariable=variableCommande,width=50)
saisieCommande.pack()

boutonExecuter= Button(window,text="Exécuter",command=changerVariable)
# à l'aide de "command=changerVariable" tkinter va exécuter la fonction changerVariable définie
# plus haut à chaque fois que le bouton est pressé
boutonExecuter.pack()

window.mainloop()