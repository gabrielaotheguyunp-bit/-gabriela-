intentos_restantes = 3

while intentos_restantes > 0:
    password = input("Introduce una contraseña (mínimo 5 caracteres): ")
    
    # Caso 1: CONTINUE
    if len(password) < 5:
        print("Contraseña muy corta. Inténtalo de nuevo.")
        continue  # Salta directo al inicio del 'while' sin restar intentos
        
    # Caso 2: BREAK
    if password == "secreto123":
        print("¡Acceso concedido!")
        break  # Rompe el bucle por completo
        
    # Restamos un intento si la contraseña tiene el largo correcto pero es incorrecta
    intentos_restantes -= 1
    print(f"Contraseña incorrecta. Intentos restantes: {intentos_restantes}")

if intentos_restantes == 0:
    print("Cuenta bloqueada por seguridad.")
 