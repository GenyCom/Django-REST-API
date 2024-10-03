from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .permissions import HasAPIKey  # Importer la permission

# Récupérer tous les livres et ajouter un livre
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [HasAPIKey]  # Ajout de la permission par clé API
    
# Récupérer, mettre à jour ou supprimer un livre spécifique
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [HasAPIKey]  # Ajout de la permission par clé API
