import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string
    
    def parse(self):
        tokens = re.split(r'[,\s]+', self.email_string)
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        valid_emails = [token for token in tokens if re.match(email_pattern, token)]
        return sorted(set(valid_emails))