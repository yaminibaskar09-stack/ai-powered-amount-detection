import re

def extract_raw_tokens(text: str):
    if not text:
        return []

    # Match realistic money-like numbers
    pattern = r'\b\d{2,7}(\.\d{1,2})?\b'
    matches = re.findall(pattern, text)

    tokens = []
    for match in re.finditer(pattern, text):
        tokens.append({
            "value": match.group(),
            "start": match.start(),
            "end": match.end()
        })

    return tokens
