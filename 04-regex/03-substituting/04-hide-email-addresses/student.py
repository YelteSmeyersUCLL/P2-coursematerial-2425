import re

def hide_email_addresses(string):
    def replace(match):
        email = match.group()
        num = len(email)
        return "*" * num
    
    return re.sub(r"([a-zA-Z0-9._%+_]+@[a-zA-Z0-9._%+_]+)", replace, string)

print(hide_email_addresses("a.b@c.d"))