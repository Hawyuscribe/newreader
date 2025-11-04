from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone
from mcq.models import UserProfile
from django.contrib.auth import logout

class AccountExpirationMiddleware:
    """
    Middleware to check if a user's account has expired.
    If the account is expired, the user will be logged out and redirected to the login page.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Process request before view is called
        # Check if user is authenticated and not a staff/superuser
        if request.user.is_authenticated and not request.user.is_staff and not request.user.is_superuser:
            try:
                # Get the user profile
                profile = UserProfile.objects.get(user=request.user)
                
                # Check if account is expired or manually deactivated
                if not profile.is_active:
                    # Determine reason for account inactivity
                    if profile.is_expired:
                        message_text = "Your account has expired. Please contact the administrator for renewal."
                    else:
                        message_text = "Your account has been deactivated. Please contact the administrator."
                    
                    # Log the user out
                    logout(request)
                    
                    # Add message that will appear on the login page
                    messages.warning(request, message_text)
                    
                    # Redirect to login page
                    return redirect(reverse('login'))
                
                # Show warning message if account is about to expire (within 3 days)
                if profile.expiration_date and (profile.expiration_date - timezone.now()).days <= 3:
                    days_remaining = max(0, (profile.expiration_date - timezone.now()).days)
                    if days_remaining == 0:
                        # Less than 24 hours remaining
                        hours_remaining = max(0, int((profile.expiration_date - timezone.now()).total_seconds() / 3600))
                        if hours_remaining > 0:
                            message_text = f"Your account will expire in {hours_remaining} hours. Please contact the administrator for renewal."
                        else:
                            message_text = "Your account is about to expire. Please contact the administrator for renewal immediately."
                    else:
                        message_text = f"Your account will expire in {days_remaining} days. Please contact the administrator for renewal."
                    
                    messages.warning(request, message_text)
            except UserProfile.DoesNotExist:
                # If the profile doesn't exist, create one with default expiration
                from datetime import timedelta
                UserProfile.objects.create(
                    user=request.user,
                    expiration_date=timezone.now() + timedelta(days=30)
                )
        
        # Process the response
        response = self.get_response(request)
        return response