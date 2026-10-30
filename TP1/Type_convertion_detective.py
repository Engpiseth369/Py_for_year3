# ---------------------------------------------------------------------------
# Problem 4 (Medium) · Type-conversion detective
# ---------------------------------------------------------------------------
# Part B — a safe converter

def safe_int(text):
    text = text.strip()
    if text.lstrip("-").isdigit():
        return int(text)
    try:
        return int(float(text))
    except:
        return None
    
for i in ["46", " -8 ", "3.9", "abc", ""]:
    print(repr(i), "->", safe_int(i))