import matplotlib.pyplot as plt

MOD = 998244353

def pow_mod(a, b, mod=MOD):
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b >>= 1
    return res

def ans(s: str) -> int:
    """
    Calculamos el número de formas validas de la cadena s
    siguiendo la fórmula matemática.
    """
    if not s:
        return 0

    rest = s[1:]  # sufijo
    q = rest.count('?')
    pw = pow_mod(2, q, MOD)
    
    # Caso especial: si la cadena tiene solo un carácter
    if not rest:
        if s[0] == '?':
            return 2
        else:
            return 1

    hasZero = 1 if '0' in rest else 0

    A = 0
    B = 0

    # A: si s[0] es '1' o '?'
    if s[0] in ['1', '?']:
        A = pw

    # B: si s[0] es '0' o '?'
    if s[0] in ['0', '?']:
        if hasZero == 1:
            B = pw
        else:
            B = (pw - 1 + MOD) % MOD  # evitar negativos

    return (A + B) % MOD

def validar_cadena(s: str) -> bool:
    return all(c in ['0', '1', '?'] for c in s)

# ==============================
#    Ejecución interactiva.
# ==============================
while True:
    s = input("Ingrese la cadena s (compuesta solo por 0, 1 y ?): ").strip()
    if validar_cadena(s):
        print(f"ans(s) = {ans(s)}")
        break
    else:
        print("Entrada inválida. USE SOLO 0, 1 o ?. Intente de nuevo.")
