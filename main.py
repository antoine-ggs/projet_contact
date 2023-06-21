class Numero:
    def __init__(self, label, indicatif, tableau):
        self.label = label
        self.indicatif = indicatif
        self.tableau = tableau

    def setNumero(self, label, indicatif, tableau):
        self.label = label
        self.indicatif = indicatif
        self.tableau = tableau

    def __str__(self):
        return self.label + " +" + self.indicatif + self.tableau

class Contact:
    def __init__(self, firstname, lastname, numero, email, cp, adress):
        self.firstname = firstname
        self.lastname = lastname
        self.numero = numero
        self.email = email
        self.cp = cp
        self.adress = adress
        self.telephoneList = [numero]

    def displayContact(self):
        print("\n=== Informations du contact ===")
        print(f"Nom     : {self.firstname}")
        print(f"Prénom  : {self.lastname}")
        print(f"Téléphone : {self.numero.label} {self.numero.indicatif} {self.numero.tableau}")
        print(f"Email   : {self.email}")
        print(f"Code postal : {self.cp}")
        print(f"Adresse : {self.adress}")
        print("==============================\n")

    def manageProfile(self):
        print("\n=== Gestion du profil ===")
        print("1. Modifier les informations")
        print("2. Modifier la photo de profil")
        print("3. Supprimer le contact")
        print("4. Partager le contact")
        print("5. Retourner à l'accueil")
        choice = input("Choisissez une option (1-5) : ")

        if choice == "1":
            self.editInfo()
        elif choice == "2":
            self.editProfilePic()
        elif choice == "3":
            self.delete()
        elif choice == "4":
            self.shareProfile()
        elif choice == "5":
            self.backToHome()
        else:
            print("Option invalide.")

    def editInfo(self):
        print("\n=== Modifier les informations ===")
        print("1. Modifier le nom")
        print("2. Modifier le prénom")
        print("3. Modifier l'adresse")
        print("4. Modifier le code postal")
        print("5. Modifier l'email")
        print("6. Modifier le numéro de téléphone")
        print("7. Retourner à la gestion du profil")
        choice = input("Choisissez une option (1-7) : ")

        if choice == "1":
            new_firstname = input("Nouveau nom : ")
            self.firstname = new_firstname
            print("Nom modifié avec succès.")
        elif choice == "2":
            new_lastname = input("Nouveau prénom : ")
            self.lastname = new_lastname
            print("Prénom modifié avec succès.")
        elif choice == "3":
            new_address = input("Nouvelle adresse : ")
            self.adress = new_address
            print("Adresse modifiée avec succès.")
        elif choice == "4":
            new_postalcode = input("Nouveau code postal : ")
            self.cp = new_postalcode
            print("Code postal modifié avec succès.")
        elif choice == "5":
            new_email = input("Nouvel email : ")
            self.email = new_email
            print("Email modifié avec succès.")
        elif choice == "6":
            print("Numéro(s) de téléphone actuel(s) :")
            for i, numero in enumerate(self.telephoneList):
                print(f"{i + 1}. {numero.label} {numero.indicatif} {numero.tableau}")
            num_choice = int(input(f"Choisissez le numéro à modifier (1-{len(self.telephoneList)}) : "))
            if 1 <= num_choice <= len(self.telephoneList):
                numero = self.telephoneList[num_choice - 1]
                new_label = input("Nouveau label : ")
                new_indicatif = input("Nouvel indicatif : ")
                new_tableau = input("Nouveau tableau : ")
                numero.setNumero(new_label, new_indicatif, new_tableau)
                print("Numéro de téléphone modifié avec succès.")
            else:
                print("Choix invalide.")
        elif choice == "7":
            print("Retour à la gestion du profil.")
        else:
            print("Option invalide.")

    def editProfilePic(self):
        print("\n=== Modifier la photo de profil ===")
        print("1. Ajouter une nouvelle photo")
        print("2. Modifier la photo existante")
        choice = input("Choisissez une option (1-2) : ")

        if choice == "1":
            print("Liste des avatars disponibles :")
            avatars = ["avatar1.jpg", "avatar2.jpg", "avatar3.jpg"]
            for i, avatar in enumerate(avatars):
                print(f"{i + 1}. {avatar}")
            avatar_choice = int(input(f"Choisissez un avatar (1-{len(avatars)}) : "))
            if 1 <= avatar_choice <= len(avatars):
                selected_avatar = avatars[avatar_choice - 1]
                self.profilePic = selected_avatar
                print("Photo de profil ajoutée avec succès.")
            else:
                print("Choix invalide.")
        elif choice == "2":
            new_profilepic = input("Entrez le chemin de la nouvelle photo de profil : ")
            self.profilePic = new_profilepic
            print("Photo de profil modifiée avec succès.")
        else:
            print("Option invalide.")

    def delete(self):
        confirm = input("Êtes-vous sûr de vouloir supprimer ce contact ? (O/N) : ")
        if confirm.upper() == "O":
            # Suppression du contact
            print("Le contact a été supprimé.")
        else:
            print("Suppression annulée.")

    def backToHome(self):
        print("Retour à l'accueil.")

    def shareProfile(self):
        # Partager le profil du contact
        print("Partager le profil.")


class ContactList:
    def __init__(self):
        self.contacts = []

    def addContact(self):
        firstname = input("Nom : ")
        lastname = input("Prénom : ")
        label = input("Label du numéro : ")
        indicatif = input("Indicatif du numéro : ")
        tableau = input("Tableau du numéro : ")
        email = input("Email: ")
        cp = input("Code postal: ")
        adress = input("Adresse: ")

        if not firstname or not lastname or not label or not indicatif or not tableau:
            print("Le nom, le prénom et au moins un numéro de téléphone sont obligatoires.")
            return

        new_numero = Numero(label, indicatif, tableau)
        new_contact = Contact(firstname, lastname, new_numero, email, cp, adress)
        self.contacts.append(new_contact)

        print("Le contact a été ajouté avec succès.")

    def displayContacts(self):
        sorted_contacts = sorted(self.contacts, key=lambda contact: contact.lastname)
 
        print("===========================")
        print("=== Liste des contacts ===")
        for contact in sorted_contacts:
            print(f"Nom     : {contact.firstname} {contact.lastname}")
            print(f"Téléphone : {contact.numero.label} {contact.numero.indicatif} {contact.numero.tableau}")
            print(f"Email   : {contact.email}")
            print(f"Code postal : {contact.cp}")
            print(f"Adresse : {contact.adress}")
            print("---------------------------")
    print("===========================")

    def searchContact(self):
        search_term = input("Entrez le nom ou le prénom du contact à rechercher : ")

        search_results = []
        for contact in self.contacts:
            if search_term.lower() in contact.firstname.lower() or search_term.lower() in contact.lastname.lower():
                search_results.append(contact)

        if not search_results:
            print("Aucun contact trouvé.")
        else:
            print(f"\n=== Résultats de recherche pour '{search_term}' ===")
            for i, contact in enumerate(search_results):
                print(f"Contact {i + 1}:")
                print(f"Nom     : {contact.firstname}")
                print(f"Prénom  : {contact.lastname}")
                print(f"Téléphone : {contact.numero.label} {contact.numero.indicatif} {contact.numero.tableau}")
                print(f"Email   : {contact.email}")
                print(f"Code postal : {contact.cp}")
                print(f"Adresse : {contact.adress}")
                print("---------------------------")
            print("===========================")


def main():
    contact_list = ContactList()
    while True:
        print("\n=== Gestion des contacts ===\n")
        print("1. Ajouter un contact")
        print("2. Afficher la liste des contacts")
        print("3. Rechercher un contact")
        print("4. Quitter")
        choice = input("Choisissez une option (1-4) : ")

        if choice == "1":
            contact_list.addContact()
        elif choice == "2":
            contact_list.displayContacts()
        elif choice == "3":
            contact_list.searchContact()
        elif choice == "4":
            print("Merci d'avoir utilisé notre application de gestion des contacts. Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()
