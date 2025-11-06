from django import template
import re

register = template.Library()

@register.filter
def to_drive_preview_url(url):
    """Convert Google Drive direct URL to preview URL for iframe"""
    if not url or 'drive.google.com' not in url:
        return url
    
    # Extract the file ID
    patterns = [
        r'/file/d/([a-zA-Z0-9_-]+)',  # /file/d/FILE_ID/ format
        r'/d/([a-zA-Z0-9_-]+)',  # /d/FILE_ID/ format
        r'id=([a-zA-Z0-9_-]+)',  # ?id=FILE_ID format
        r'uc\?export=view&id=([a-zA-Z0-9_-]+)',  # current format
    ]
    
    file_id = None
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            file_id = match.group(1)
            break
    
    if file_id:
        return f'https://drive.google.com/file/d/{file_id}/preview'
    
    return url

@register.filter  
def is_google_drive_url(url):
    """Check if URL is from Google Drive"""
    return url and 'drive.google.com' in url