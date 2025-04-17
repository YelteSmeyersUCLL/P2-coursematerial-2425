import re

def scrape_email_addresses(string):
    return re.findall(r"[a-zA-Z0-9._%+_]+@[a-zA-Z0-9._%+_]+", string)