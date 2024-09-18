import re

def validate_email(email: str) -> bool:
    # Regular expression for validating an email
    email_regex = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$'
    return re.match(email_regex, email) is not None

def validate_phone(phone: str) -> bool:
    # Regular expressions for validating phone numbers
    phone_regex_11 = r'^09\d{9}$'  # Starts with 09 and has 11 digits
    phone_regex_13 = r'^\+989\d{9}$'  # Starts with +989 and has 13 digits
    phone_regex_14 = r'^00989\d{9}$'  # Starts with 00989 and has 14 digits
    
    return re.match(phone_regex_11, phone) is not None or \
           re.match(phone_regex_13, phone) is not None or \
           re.match(phone_regex_14, phone) is not None
