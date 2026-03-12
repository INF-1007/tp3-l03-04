
"""
TP3 : Système de gestion de livres pour une bibliothèque

IMPORTANT :
- Suivre attentivement les directives dans le fichier README.md.
- Chaque partie du TP doit être réalisée à l'intérieur d'une fonction que vous devez créer.
- Vous devez ensuite appeler chacune des fonctions dans la fonction principale "main()"

"""

import csv
from datetime import datetime


##########################################################################################################
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
##########################################################################################################

"""
Créer une fonction `charger_collection` qui permet de : 
    - Lire le fichier collection_bibliotheque.csv
    - Créer un dictionnaire nommé 'bibliotheque'
        - La cote doit être la clé principale
        - Chaque clé principale doit contenir :
            - titre
            - auteur
            - date_publication

Cette partie doit être faite dans une fonction qui s'appelle "charger_collection". 
"""

# Écrire votre code ici
def charger_collection(fichier_csv):
    bibliotheque={}
    lecteur= csv.DictReader(open(fichier_csv, newline="", encoding="utf-8"))
    for ligne in lecteur:
            cote_rangement = ligne["cote_rangement"]
            bibliotheque[cote_rangement] = {
                "titre": ligne["titre"],
                "auteur": ligne["auteur"],
                "date_publication": ligne["date_publication"]
            }

    return bibliotheque








##########################################################################################################
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
##########################################################################################################

"""
Exigences :
- Lire nouvelle_collection.csv
- Ajouter seulement les livres dont la cote n'existe pas déjà
- Afficher les messages demandés dans l'énoncé
- Retourner ou mettre à jour la bibliothèque

Cette partie doit être faite dans une fonction qui s'appelle "ajouter_nouvelle_collection". 
"""

# Écrire votre code ici
def ajouter_nouvelle_collection(bibliotheque, nouvelle_collection_csv):
    nouvelle_bibliotheque={}
    lecteur= csv.DictReader(open(nouvelle_collection_csv, newline="", encoding="utf-8"))
    for ligne in lecteur:
            cote_rangement = ligne["cote_rangement"]
            nouvelle_bibliotheque[cote_rangement] = {
                "titre": ligne["titre"],
                "auteur": ligne["auteur"],
                "date_publication": ligne["date_publication"]
            }
    for cote_rangement in nouvelle_bibliotheque:

        titre = nouvelle_bibliotheque[cote_rangement]["titre"]
        auteur = nouvelle_bibliotheque[cote_rangement]["auteur"]

        if cote_rangement in bibliotheque:
            print(f"Le livre {titre} par {auteur} est déjà présent dans la bibliothèque")
        else:
            print(f"Le livre {titre} par {auteur} a été ajouté avec succès")
            bibliotheque[cote_rangement] = nouvelle_bibliotheque[cote_rangement]
    return bibliotheque 






##########################################################################################################
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
##########################################################################################################

"""
Exigences :
- Modifier les cotes des livres de William Shakespeare
- Exemple : S028 → WS028
- Modifier correctement les clés du dictionnaire

Cette partie doit être faite dans une fonction qui s'appelle "modifier_cote_shakespeare". 
"""

# Écrire votre code ici
def modifier_cote_shakespeare(bibliotheque):
    cote_a_modifier =[]
    for cote in bibliotheque:
        if bibliotheque[cote]["auteur"]=="William Shakespeare":
            cote_a_modifier.append(cote)
    for cote in cote_a_modifier:
        cote_modif='WS'+cote[1:]
        bibliotheque[cote_modif]=bibliotheque[cote]
        del bibliotheque[cote]
    return bibliotheque







##########################################################################################################
# PARTIE 4 : Emprunts et retours de livres
##########################################################################################################

"""
Exigences :
- Ajouter les clés :
    - emprunt
    - date_emprunt
- Lire emprunts.csv
- Mettre à jour l'état des livres

Cette partie doit être faite dans une fonction qui s'appelle "ajouter_emprunts". 
"""

# Écrire votre code ici

def ajouter_emprunts(bibliotheque, emprunts_csv):
    lecteur = csv.DictReader(open(emprunts_csv, newline="", encoding="utf-8"))
    emprunts ={}
    for ligne in lecteur:
         cote = ligne["cote_rangement"]
         date = ligne["date_emprunt"]
         emprunts[cote]=date
    for cote in bibliotheque:
        bibliotheque[cote]["emprunt"]="disponible"
        bibliotheque[cote]["date_emprunt"]=None
        if cote in emprunts:
            bibliotheque[cote]["emprunt"] = "emprunté"
            bibliotheque[cote]["date_emprunt"]=emprunts[cote]
    return bibliotheque











##########################################################################################################
# PARTIE 5 : Livres en retard
##########################################################################################################

"""
Exigences :
- Ajouter les clés :
    - frais_retard
    - livre_perdu
- 30 jours autorisés
- 2$ par jour de retard (max 100$)
- Livre perdu après 365 jours
- Utiliser datetime

Cette partie doit être faite dans une fonction qui s'appelle "ajouter_retards". 
"""
"%Y-%m-%d"
# Écrire votre code ici
from datetime import datetime
from datetime import date
def calculer_retards(bibliotheque):

    print("--- Livres en retard ---")

    for cote in bibliotheque:

        format_date = "%Y-%m-%d"
        date_emprunt = bibliotheque[cote]["date_emprunt"]
        bibliotheque[cote]["frais_retard"]=0
        bibliotheque[cote]["livre_perdu"]=False
        if date_emprunt is None:
            continue

        date_emprunt_format = datetime.strptime(date_emprunt,format_date).date()
        date_ajd = date.today()
        jours = (date_ajd - date_emprunt_format).days

        if jours>30:
            frais =min((jours-30)*2,100)
            bibliotheque[cote]["frais_retard"]=frais
            print(f"{cote} - {bibliotheque[cote]['titre']} : {frais}$ de frais")

        if jours >365:
            bibliotheque[cote]["livre_perdu"]=True
        else:
            bibliotheque[cote]["livre_perdu"]=False


    return bibliotheque














##########################################################################################################
# PARTIE 6 : Sauvegarde de la bibliothèque
##########################################################################################################

"""
Exigences :
- Créer le fichier bibliotheque_mise_a_jour.csv
- Colonnes obligatoires :
    cote, titre, auteur, date_publication,
    emprunt, date_emprunt, frais_retard, livre_perdu
- Utiliser le module csv pour écrire le fichier

Cette partie doit être faite dans une fonction qui s'appelle "sauvegarder_bibliotheque". 
"""

# Écrire votre code ici
def sauvegarder_bibliotheque(bibliotheque,fichier_sortie):
    file_open = open(fichier_sortie, "w", newline="", encoding="utf-8")
    headers =["cote", "titre", "auteur", "date_publication","emprunt","date_emprunt","frais_retard","livre_perdu"]
    liste_lignes =[]
    for cote in bibliotheque:
        ligne = {
            headers[0]:cote,
            headers[1]:bibliotheque[cote]["titre"],
            headers[2]:bibliotheque[cote]["auteur"],
            headers[3]:bibliotheque[cote]["date_publication"],
            headers[4]:bibliotheque[cote]["emprunt"],
            headers[5]:bibliotheque[cote]["date_emprunt"],
            headers[6]:bibliotheque[cote]["frais_retard"],
            headers[7]:bibliotheque[cote]["livre_perdu"]
        }
        liste_lignes.append(ligne)
    file_save = csv.DictWriter(file_open,fieldnames=headers)
    file_save.writeheader()
    file_save.writerows(liste_lignes)
    file_open.close()
    
    











##########################################################################################################
# PROGRAMME PRINCIPAL
##########################################################################################################

"""
Exigences :
- Appeler toutes vos fonctions dans le bon ordre
- Vérifier que le programme fonctionne sans erreur
- Afficher les résultats demandés
"""

# Écrire votre code ici
def main():



    ############################################################
    # Partie 1 : Appel de la fonction charger_collection 
    ############################################################
    
    # Écrire votre code ici 
    bibliotheque =(charger_collection("collection_bibliotheque.csv"))
    print(bibliotheque)


    ############################################################
    # Partie 2 : Appel de la fonction ajouter_nouvelle_collection
    ############################################################
    
    # Écrire votre code ici 
    bibliotheque = ajouter_nouvelle_collection(bibliotheque,"nouvelle_collection.csv")




    ############################################################
    # Partie 3 : Appel de la fonction modifier_cote_shakespeare
    ############################################################

    # Écrire votre code ici 
    bibliotheque = modifier_cote_shakespeare(bibliotheque)
    



    ############################################################
    # Partie 4 : Appel de la fonction ajouter_emprunts
    ############################################################

    # Écrire votre code ici 
    bibliotheque = ajouter_emprunts(bibliotheque,"emprunts.csv")




    ############################################################
    # Partie 5 : Appel de la fonction calculer_retards
    ############################################################

    # Écrire votre code ici 
    bibliotheque = calculer_retards(bibliotheque)

   

    ############################################################
    # Partie 6 : Appel de la fonction sauvegarder_bibliotheque
    ############################################################
    
    # Écrire votre code ici 
    sauvegarder_bibliotheque(bibliotheque, "bibliotheque_mise_a_jour.csv")




if __name__ == "__main__":
    main()