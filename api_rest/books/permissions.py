# permissions.py
from rest_framework.permissions import BasePermission
from django.conf import settings

class HasAPIKey(BasePermission):
    """
    Permission qui valide l'API Key envoyée dans les en-têtes de la requête.
    """
    def has_permission(self, request, view):
        # Récupérer la clé API envoyée dans les en-têtes
        api_key = request.headers.get('Authorization')
        
        # Vérifier que la clé est bien présente et qu'elle correspond à celle dans les settings
        if api_key == f"Api-Key {settings.API_KEY}":
            return True
        return False
