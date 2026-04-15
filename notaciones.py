def prioridad(op):
    if op in ('+', '-'): return 1
    if op in ('*', '/'): return 2
    if op == '^': return 3
    return 0


def infija_a_postfija(expresion):
    pila = []
    salida = []
    for caracter in expresion:
        if caracter.isalnum():
            salida.append(caracter)
        elif caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()
        else:
            while pila and prioridad(pila[-1]) >= prioridad(caracter):
                salida.append(pila.pop())
            pila.append(caracter)

    while pila:
        salida.append(pila.pop())

    return salida


def infija_a_prefija(expresion):
    # Invertir expresión
    expresion = expresion[::-1]

    # Cambiar paréntesis
    nueva = ""
    for c in expresion:
        if c == '(':
            nueva += ')'
        elif c == ')':
            nueva += '('
        else:
            nueva += c

    # Convertir a postfija
    postfija = infija_a_postfija(nueva)

    # Invertir resultado
    return postfija[::-1]


def generar_cuadruplos(postfija):
    pila = []
    contador_t = 1

    print(f"\n{'OP':<5} | {'ARG1':<6} | {'ARG2':<6} | {'RESULTADO'}")
    print("-" * 35)

    for token in postfija:
        if token.isalnum():
            pila.append(token)
        else:
            arg2 = pila.pop()
            arg1 = pila.pop()
            res = f"T{contador_t}"
            print(f"{token:<5} | {arg1:<6} | {arg2:<6} | {res}")
            pila.append(res)
            contador_t += 1


# ---- Bucle principal ----
while True:

    exp = input("\nIngresa la expresión infija (ej: a+b*c) o escribe 'salir': ")

    if exp.lower() == "salir":
        print("Programa finalizado.")
        break

    exp = exp.replace(" ", "")

    post = infija_a_postfija(exp)
    pre = infija_a_prefija(exp)

    print("\n--- RESULTADOS ---")
    print(f"1. Infija:     {exp}")
    print(f"2. Prefija:    {''.join(pre)}")
    print(f"3. Postfija:   {''.join(post)}")

    print("\n4. Cuádruplos:")
    generar_cuadruplos(post)
