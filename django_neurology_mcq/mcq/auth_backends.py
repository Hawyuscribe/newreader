"""
Custom authentication backend to make usernames case-insensitive.
"""

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CaseInsensitiveModelBackend(ModelBackend):
    """
    Authentication backend that allows case-insensitive username matching.
    This enables users to log in regardless of the capitalization used in their username.
    """
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
            
        if username is None or password is None:
            return None
            
        # Use a case-insensitive lookup with iexact
        try:
            # Look up users with case-insensitive matching on username
            user = UserModel.objects.get(**{
                f'{UserModel.USERNAME_FIELD}__iexact': username
            })
            
            # Check the password for the user
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
                
        except UserModel.DoesNotExist:
            # Run the default password hasher to mitigate timing attacks
            UserModel().set_password(password)
            
        return None