#TP integrador – Repetitivas- Condicionales y Secuenciales.

#------------------------------
#Ejercicio 1— “Caja del Kiosco”
#------------------------------

print("\nBienvenido a la caja del kiosco.")
nombre = input("Ingrese su nombre: ") 
while not nombre.isalpha():
    print("Error. Por favor ingrese solo letras.")
    nombre = input("Ingrese su nombre: ")

cant_productos = input("Ingrese la cantidad de productos a comprar: ")
while not cant_productos.isdigit() or cant_productos == "0":
    print("Error. Por favor ingrese un numero valido.")
    cant_productos = input("Ingrese la cantidad de productos a comprar: ")
cant_productos = int(cant_productos)

total_sin_descuentos = 0
total_con_descuentos = 0
ahorro_total = 0
resumen_productos = ""

for i in range(cant_productos):
    print(f"\nProducto {i + 1}")
    precio = input("Indique el precio del producto: ")
    while not precio.isdigit() or precio == "0":
        print("Error. Ingrese un precio válido mayor a 0.")
        precio = input("Indique el precio del producto: ")

    precio = int(precio)

    tiene_descuento = input("Tiene descuento? (S/N): ").lower()
    while tiene_descuento != "s" and tiene_descuento != "n":
        print("Error. Ingrese 's' para Sí o 'n' para No.")
        tiene_descuento = input("Tiene descuento? (S/N): ").lower()

    if tiene_descuento == "s":
        descuento_producto = precio * 0.10
        estado_descuento = "Aplica 10%"
    else:
        descuento_producto = 0.0
        estado_descuento = "Sin descuento"

    precio_final = precio - descuento_producto

    total_sin_descuentos += precio
    total_con_descuentos += precio_final
    ahorro_total += descuento_producto

    resumen_productos += f"Producto {i + 1} - Precio: ${precio} - Descuento: ${descuento_producto:.2f}\n"

promedio_por_producto = total_con_descuentos / cant_productos

print("\n--- Carrito del kiosco ---")
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cant_productos}\n")

print(resumen_productos)

print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")

#----------------------------------------------
#Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#----------------------------------------------

usuario_correcto = "usuario123"
clave_correcta = "python123"

intentos = 0
while intentos < 3:
    usuario_ingresado = input("\nIngrese su usuario: ")
    clave_ingresada = input("Ingrese su clave: ")
    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print("Acceso concedido. Bienvenido al sistema.")
        while True:
            print("\n--- Menú de Acciones ---")
            print("\n1) Ver estado de inscripción", end=" ")
            print("2) Cambiar clave", end=" ")
            print("3) Mostrar mensaje motivacional", end=" ")
            print("4) Salir")

            opcion = input("Seleccione una opción (1-4): ")
            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
                print("Error. Opcion fuera de rango.") 
                continue

            opcion = int(opcion)

            if opcion == 1:
                print("\nEstado de inscripción: Inscripto")
            elif opcion == 2:
                nueva_clave = input("Ingrese la nueva clave (mínimo 6 caracteres): ")
                if len(nueva_clave) < 6:
                    print("Error. La clave debe tener al menos 6 caracteres.")
                    continue
                confirmacion_clave = input("Confirme la nueva clave: ")
                if nueva_clave != confirmacion_clave:
                    print("Error. Las claves no coinciden.")
                    continue
                clave_correcta = nueva_clave
                print("\nClave cambiada exitosamente.")
            elif opcion == 3:
                print("\nMensaje motivacional: ¡Sigue adelante, lo estás haciendo genial!")
            elif opcion == 4:
                print("\nSaliendo del sistema. ¡Hasta luego!")
                break
        break
    else:
        intentos += 1
        print(f"Usuario o clave incorrectos. Intentos restantes: {3 - intentos}")

if intentos == 3:
    print("Cuenta bloqueada. Por favor, inténtelo más tarde.")

#--------------------------------------------------------------------
#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
#--------------------------------------------------------------------

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

print("\nBienvenido a la agenda de turnos.")
nombre_operador = ""
while not nombre_operador.isalpha() or nombre_operador == "":
    nombre_operador = input("\nIngrese su nombre (solo letras): ")
    if not nombre_operador.isalpha() or nombre_operador == "":
        print("Error: El nombre debe contener solo letras y no estar vacío.")

print("Nombre del operador registrado:", nombre_operador)

while True:
    print("\nMenú:")
    print("1. Reservar turno |", end=" ")
    print("2. Cancelar turno (por nombre) |", end=" ")
    print("3. Ver agenda del día |", end=" ")
    print("4. Ver resumen general |", end=" ")
    print("5. Cerrar sistema")
    
    opcion = input("\nSeleccione una opción (1-5): ")

    if opcion == "1":
        dia = input("\nSeleccione el día (1 = Lunes, 2 = Martes): ")
        
        if dia == "1" or dia == "2":
            nombre_paciente = ""
            while not nombre_paciente.isalpha() or nombre_paciente == "":
                nombre_paciente = input("\nIngrese el nombre del paciente (solo letras): ")
                if not nombre_paciente.isalpha() or nombre_paciente == "":
                    print("Nombre inválido. Debe contener solo letras y no estar vacío.")

            if dia == "1":
                if (nombre_paciente == lunes1 or nombre_paciente == lunes2 or 
                    nombre_paciente == lunes3 or nombre_paciente == lunes4):
                    print("El paciente ya tiene un turno reservado en Lunes.")
                elif lunes1 == "":
                    lunes1 = nombre_paciente
                    print("Turno reservado con éxito para", nombre_paciente, "en Lunes (Turno 1).")
                elif lunes2 == "":
                    lunes2 = nombre_paciente
                    print("Turno reservado con éxito para", nombre_paciente, "en Lunes (Turno 2).")
                elif lunes3 == "":
                    lunes3 = nombre_paciente
                    print("Turno reservado con éxito para", nombre_paciente, "en Lunes (Turno 3).")
                elif lunes4 == "":
                    lunes4 = nombre_paciente
                    print("Turno reservado con éxito para", nombre_paciente, "en Lunes (Turno 4).")
                else:
                    print("No hay turnos disponibles para Lunes.")

            elif dia == "2":
                if (nombre_paciente == martes1 or nombre_paciente == martes2 or 
                    nombre_paciente == martes3):
                    print("El paciente ya tiene un turno reservado en Martes.")
                elif martes1 == "":
                    martes1 = nombre_paciente
                    print("Turno reservado con éxito para", nombre_paciente, "en Martes (Turno 1).")
                elif martes2 == "":
                    martes2 = nombre_paciente
                    print("Turno reservado con éxito para", nombre_paciente, "en Martes (Turno 2).")
                elif martes3 == "":
                    martes3 = nombre_paciente
                    print("Turno reservado con éxito para", nombre_paciente, "en Martes (Turno 3).")
                else:
                    print("No hay turnos disponibles para Martes.")
        else:
            print("Día inválido. Seleccione 1 o 2.")

    elif opcion == "2":
        dia = input("\nSeleccione el día para cancelar (1 = Lunes, 2 = Martes): ")
        
        if dia == "1" or dia == "2":
            nombre_paciente = ""
            while not nombre_paciente.isalpha() or nombre_paciente == "":
                nombre_paciente = input("\nIngrese el nombre del paciente a cancelar (solo letras): ")
                if not nombre_paciente.isalpha() or nombre_paciente == "":
                    print("Nombre inválido. Debe contener solo letras y no estar vacío.")

            if dia == "1":
                if lunes1 == nombre_paciente:
                    lunes1 = ""
                    print("Turno cancelado para", nombre_paciente, "en Lunes.")
                elif lunes2 == nombre_paciente:
                    lunes2 = ""
                    print("Turno cancelado para", nombre_paciente, "en Lunes.")
                elif lunes3 == nombre_paciente:
                    lunes3 = ""
                    print("Turno cancelado para", nombre_paciente, "en Lunes.")
                elif lunes4 == nombre_paciente:
                    lunes4 = ""
                    print("Turno cancelado para", nombre_paciente, "en Lunes.")
                else:
                    print("No se encontró un turno para", nombre_paciente, "en Lunes.")

            elif dia == "2":
                if martes1 == nombre_paciente:
                    martes1 = ""
                    print("Turno cancelado para", nombre_paciente, "en Martes.")
                elif martes2 == nombre_paciente:
                    martes2 = ""
                    print("Turno cancelado para", nombre_paciente, "en Martes.")
                elif martes3 == nombre_paciente:
                    martes3 = ""
                    print("Turno cancelado para", nombre_paciente, "en Martes.")
                else:
                    print("No se encontró un turno para", nombre_paciente, "en Martes.")
        else:
            print("Día inválido. Seleccione 1 o 2.")

    elif opcion == "3":
        dia = input("\nSeleccione el día para ver la agenda (1 = Lunes, 2 = Martes): ")
        if dia == "1":
            print("\n--- Agenda del Lunes ---")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        elif dia == "2":
            print("\n--- Agenda del Martes ---")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")
        else:
            print("Día inválido. Seleccione 1 o 2.")

    elif opcion == "4":
        turnos_ocupados_lunes = 0
        if lunes1 != "": turnos_ocupados_lunes += 1
        if lunes2 != "": turnos_ocupados_lunes += 1
        if lunes3 != "": turnos_ocupados_lunes += 1
        if lunes4 != "": turnos_ocupados_lunes += 1

        turnos_disponibles_lunes = 4 - turnos_ocupados_lunes

        turnos_ocupados_martes = 0
        if martes1 != "": turnos_ocupados_martes += 1
        if martes2 != "": turnos_ocupados_martes += 1
        if martes3 != "": turnos_ocupados_martes += 1

        turnos_disponibles_martes = 3 - turnos_ocupados_martes

        print("\n--- Resumen General ---")
        print("Lunes: Turnos ocupados:", turnos_ocupados_lunes, "| Turnos disponibles:", turnos_disponibles_lunes)
        print("Martes: Turnos ocupados:", turnos_ocupados_martes, "| Turnos disponibles:", turnos_disponibles_martes)

        if turnos_ocupados_lunes > turnos_ocupados_martes:
            print("Día con más turnos ocupados: Lunes")
        elif turnos_ocupados_martes > turnos_ocupados_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Empate en la cantidad de turnos ocupados entre Lunes y Martes.")

    elif opcion == "5":
        print("Cerrando sistema. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")

#--------------------------------------
#Ejercicio 4 — “Escape Room: La Bóveda”
#--------------------------------------

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

nombre_agente = ""
while not nombre_agente.isalpha() or nombre_agente == "":
    nombre_agente = input("\nIngrese su nombre de agente (solo letras): ")
    if not nombre_agente.isalpha() or nombre_agente == "":
        print("Nombre inválido. Debe contener solo letras y no estar vacío.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma and tiempo <= 3:
        print("\n¡SISTEMA BLOQUEADO POR ALARMA!")
        break

    print(f"\n--- ESTADO DEL AGENTE {nombre_agente.upper()} ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    
    print("\nMenú de acciones:")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = ""
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        opcion = input("Seleccione una opción (1-3): ")
        if not opcion.isdigit() or opcion not in ["1", "2", "3"]:
            print("Opción inválida. Ingrese un número entre 1 y 3.")

    if opcion == "1":
        racha_forzar += 1
        energia -= 20
        tiempo -= 2

        if racha_forzar == 3:
            print("¡La cerradura se trabó por intentar forzar 3 veces seguidas! Se activó la alarma.")
            alarma = True
        else:
            alarma_activada = False
            if energia < 40:
                print("¡Energía baja! Hay riesgo de activar la alarma.")
                riesgo = ""
                while not riesgo.isdigit() or riesgo not in ["1", "2", "3"]:
                    riesgo = input("Elija un número de riesgo (1-3): ")
                if riesgo == "3":
                    print("¡Mala suerte! Activaste la alarma.")
                    alarma = True
                    alarma_activada = True

            if not alarma_activada:
                cerraduras_abiertas += 1
                print("¡Lograste forzar y abrir 1 cerradura!")

    elif opcion == "2":
        racha_forzar = 0  
        energia -= 10
        tiempo -= 3

        print("Hackeando panel...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso hackeo: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completado (8+ caracteres)! Se abrió automáticamente 1 cerradura.")

    elif opcion == "3":
        racha_forzar = 0  
        tiempo -= 1
        
        energia = min(100, energia + 15)

        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma sonando te desgasta (-10 energía extra).")
        else:
            print("Recuperaste energía al descansar.")

print("\n================ RESULTADO ================")
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El agente {nombre_agente} ha abierto la bóveda.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se ha bloqueado debido a la alarma.")
else:
    print("DERROTA: Te has quedado sin energía o sin tiempo.")

#---------------------------------------------------
#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
#---------------------------------------------------

print("\nBienvenido a la Arena del Gladiador.")

nombre = ""
while not nombre.isalpha() or nombre == "":
    nombre = input("Ingrese el nombre del Gladiador: ")
    if not nombre.isalpha() or nombre == "":
        print("Error: Solo se permiten letras.")

vida_jugador = 100        
vida_enemigo = 100        
pociones = 3              
dano_pesado = 15          
dano_enemigo = 12         
turno_gladiador = True    

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = ""
    while not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
        opcion = input("Opción: ")
        if not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
            print("Error: Ingrese un número válido (1, 2 o 3).")

    if opcion == "1":
        if vida_enemigo < 20:
            dano_final = dano_pesado * 1.5  
            print(f"¡GOLPE CRÍTICO! Atacaste al enemigo por {dano_final} puntos de daño!")
        else:
            dano_final = float(dano_pesado)
            print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")
        
        vida_enemigo -= dano_final

    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Te curaste 30 HP. Te quedan {pociones} pociones.")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= dano_enemigo
        print(f">> ¡El enemigo te atacó por {dano_enemigo} puntos de daño!")

print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
