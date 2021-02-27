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

# 
reponse = StringVar()
reponse.set("Ici le retour")

labelReponse= Label(window, textvariable=reponse,justify=LEFT)
labelReponse.pack(side=TOP)

variableCommande = StringVar()
variableCommande.set('Votre commande')

saisieCommande=Entry(window,textvariable=variableCommande,width=50)
saisieCommande.pack()

boutonExecuter= Button(window,text="Exécuter",command=changerVariable)
boutonExecuter.pack()

window.mainloop()