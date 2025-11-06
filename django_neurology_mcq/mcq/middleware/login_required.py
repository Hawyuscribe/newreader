from django.shortcuts import redirect
from django.urls import reverse, resolve
from django.conf import settings
import re
import logging

logger = logging.getLogger(__name__)

class LoginRequiredMiddleware:
    """
    Middleware to ensure all pages except login redirect to login page when user is not authenticated.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Process request before view is called
        try:
            # List of URL names that are exempt from the login requirement
            exempt_urls = [
                'login',
                'admin:index',
                'admin:login',
                'logout',
                'healthz',
            ]
            
            # Get current URL path
            path = request.path_info
            
            # If user is not authenticated and path is not in exempt_urls, redirect to login
            if not request.user.is_authenticated:
                # Don't redirect for admin URLs or the login URL itself
                if (
                    path.startswith('/admin/')
                    or path == settings.LOGIN_URL
                    or path.startswith('/logout/')
                    or path.startswith('/healthz')
                    or path.startswith('/debug/clinical-reasoning/')  # allow token-protected debug APIs
                ):
                    return self.get_response(request)
                    
                # Try to resolve the URL to check if it matches exempt URLs
                try:
                    url_name = resolve(path).url_name
                    if url_name in exempt_urls:
                        return self.get_response(request)
                except Exception as e:
                    # If resolve fails, log it and default to checking path
                    logger.debug(f"Error resolving URL {path}: {str(e)}")
                    
                # Check for static files
                if path.startswith(settings.STATIC_URL):
                    return self.get_response(request)
                    
                # If not exempt, redirect to login
                return redirect(settings.LOGIN_URL)
            
            # Process the response for authenticated users
            return self.get_response(request)
            
        except Exception as e:
            # Log any errors but allow the request to proceed
            logger.error(f"Error in LoginRequiredMiddleware: {str(e)}")
            return self.get_response(request)
