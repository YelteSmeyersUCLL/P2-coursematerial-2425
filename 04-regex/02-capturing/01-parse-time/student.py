import re

def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string)

    if match:
        h, m, s, ms = match.groups('000')
    else:
        return None
    return (int(h), int(m), int(s), int(ms[1:]))