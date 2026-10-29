"""Conversione e aritmetica con i numeri romani (1 - 3999)."""

import re

MIN, MAX = 1, 3999

_VALORI = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]

_REGEX = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")


class ErroreRomano(ValueError):
    """Numero romano non valido o risultato fuori intervallo."""


def a_romano(n: int) -> str:
    if not isinstance(n, int) or not MIN <= n <= MAX:
        raise ErroreRomano("I Romani scrivevano solo da I a MMMCMXCIX")
    out = []
    for valore, simbolo in _VALORI:
        while n >= valore:
            out.append(simbolo)
            n -= valore
    return "".join(out)


def da_romano(s: str) -> int:
    s = s.strip().upper()
    if not s or not _REGEX.match(s):
        raise ErroreRomano(f"«{s or '?'}» non è un numero romano valido")
    totale, i = 0, 0
    for valore, simbolo in _VALORI:
        while s.startswith(simbolo, i):
            totale += valore
            i += len(simbolo)
    return totale


def calcola(a: str, op: str, b: str) -> str:
    """Esegue a op b su due numeri romani e restituisce il risultato in romano."""
    x, y = da_romano(a), da_romano(b)
    if op == "+":
        r = x + y
    elif op in ("-", "−"):
        r = x - y
        if r == 0:
            return "NVLLA"  # i Romani non avevano lo zero
        if r < 0:
            raise ErroreRomano("I Romani non conoscevano i numeri negativi")
    elif op in ("*", "×"):
        r = x * y
    elif op in ("/", "÷"):
        q, resto = divmod(x, y)
        if q == 0:
            return f"NVLLA resto {a_romano(resto)}"
        return a_romano(q) + (f" resto {a_romano(resto)}" if resto else "")
    else:
        raise ErroreRomano(f"Operazione sconosciuta: {op}")
    return a_romano(r)
