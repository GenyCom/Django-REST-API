import requests

BASE_URL = 'http://127.0.0.1:8000/api/books/'
API_KEY = 'YOUR_API_KEY'  # Remplace par ta clé d'API

# Définir les en-têtes avec la clé d'API
headers = {
    'Authorization': f'Token {API_KEY}',  # Assurez-vous que le format est correct pour votre API
    'Content-Type': 'application/json'  # Indiquer que le contenu est en JSON
}

def get_books():
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code == 200:
        print("Liste des livres :")
        for book in response.json():
            print(f"ID: {book['id']}, Titre: {book['title']}, Auteur: {book['author']}")
    else:
        print(f"Erreur lors de la récupération des livres : {response.status_code}")

def add_book(title, author):
    book_data = {'title': title, 'author': author}
    response = requests.post(BASE_URL, json=book_data, headers=headers)
    if response.status_code == 201:
        print(f"Livre ajouté : {response.json()}")
    else:
        print(f"Erreur lors de l'ajout du livre : {response.status_code}, {response.text}")

def update_book(book_id, title, author):
    book_data = {'title': title, 'author': author}
    response = requests.put(f"{BASE_URL}{book_id}/", json=book_data, headers=headers)
    if response.status_code == 200:
        print(f"Livre mis à jour : {response.json()}")
    else:
        print(f"Erreur lors de la mise à jour du livre : {response.status_code}, {response.text}")

def delete_book(book_id):
    response = requests.delete(f"{BASE_URL}{book_id}/", headers=headers)
    if response.status_code == 204:
        print(f"Livre avec ID {book_id} supprimé.")
    else:
        print(f"Erreur lors de la suppression du livre : {response.status_code}, {response.text}")

# Utilisation du script
if __name__ == "__main__":
    print("=== Gestion des livres ===")
    
    # Récupérer et afficher la liste des livres
    get_books()

    # Ajouter un nouveau livre
    add_book("Nouveau Livre", "Auteur Inconnu")

    # Mettre à jour un livre (changez l'ID pour un livre existant)
    update_book(1, "Titre Modifié", "Auteur Modifié")

    # Supprimer un livre (changez l'ID pour un livre existant)
    delete_book(2)

    # Afficher à nouveau la liste des livres après les opérations
    get_books()
