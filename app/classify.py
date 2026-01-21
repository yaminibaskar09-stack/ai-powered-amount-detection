import re

def classify_amounts(text: str, amounts):
    results = []
    text = text.lower()

    def find_amount_after_keywords(keywords):
        for kw in keywords:
            # matches: keyword ... number
            match = re.search(rf"{kw}[^0-9]{{0,10}}([0-9]{{2,6}})", text)
            if match:
                return int(match.group(1))
        return None

    # ---------- Detect amounts ----------
    total = find_amount_after_keywords([
        "total", "grand total", "gross amount", "invoice amount", "bill amount"
    ])

    paid = find_amount_after_keywords([
        "paid", "amount paid", "amount settled", "received"
    ])

    due = find_amount_after_keywords([
        "due", "balance", "outstanding", "pending"
    ])

    if total:
        results.append({"type": "total", "value": total})
    if paid:
        results.append({"type": "paid", "value": paid})
    if due:
        results.append({"type": "due", "value": due})

    return results
