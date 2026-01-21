def normalize_tokens(tokens):
    normalized = []

    for token in tokens:
        if isinstance(token, dict):
            text = token.get("text", "")
        else:
            text = str(token)

        text = text.replace('l', '1').replace('O', '0')
        normalized.append(text)

    return normalized