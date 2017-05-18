# importujemy moduł wbudowany Pythona
import string

def czy_pangram(fraza):
    """Sprawdza czy fraza jest pangramem"""

    # używamy element z modułu
    # podajemy nazwę modułu kropka i wew. element
    for litera in string.ascii_lowercase:
        if litera not in str(fraza).lower():
            return False

    return True

print(czy_pangram("abcDE"))
print(czy_pangram("The quick brown fox jumps over the lazy dog"))

