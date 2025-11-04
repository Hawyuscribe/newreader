"""
Utility functions for MCQ data processing and validation.
"""

def is_nan_like(value):
    """
    Check if a value is NaN-like (None, NaN, 'nan', 'null', etc.).
    
    Args:
        value: Any value to check
        
    Returns:
        bool: True if the value is NaN-like, False otherwise
    """
    if value is None:
        return True
    if isinstance(value, str):
        # Check for string representations of NaN
        return value.strip().lower() in ('nan', 'none', 'null', '')
    # Check for other types of NaN (like pandas np.nan)
    try:
        # This will handle float('nan') and np.nan
        import math
        return math.isnan(value)
    except (TypeError, ValueError):
        return False

def clean_option_text(text):
    """
    Clean option text by trimming whitespace and removing trailing punctuation.
    
    Args:
        text: The option text to clean
        
    Returns:
        str: Cleaned option text
    """
    if not text or is_nan_like(text):
        return ""
    
    # Strip whitespace
    cleaned = text.strip()
    
    # Remove trailing punctuation (period, comma, semicolon)
    if cleaned and cleaned[-1] in ".,:;":
        cleaned = cleaned[:-1].strip()
        
    return cleaned

def normalize_option_letter(letter):
    """
    Normalize option letter to uppercase single letter.
    
    Args:
        letter: The option letter to normalize
        
    Returns:
        str: Normalized option letter
    """
    if not letter or is_nan_like(letter):
        return None
        
    # Get first character and convert to uppercase
    return letter[0].upper()