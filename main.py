import turtle
def dibujar_estrella():
    print("¿Cuántas puntas tiene tu estrella?")
    puntas=int(input())
    while puntas <= 4:
        print("Número no válido, seleccione otro")
        print("¿Cuántas puntas tiene tu estrella?")
        puntas=int(input())
    angulo= (puntas - 2) * 180 / puntas #Fórmula del ángulo interno de un polígono
    angulo_positivo = (1 - 4/puntas) * 180 #Fórmula del ángulo interno positivo de un polígono
    estrella=turtle.Turtle()
    pantalla=turtle.Screen()
    turtle.hideturtle() #No se muestra el puntero
    turtle.pencolor("White")
    turtle.pensize(3) # Pongo el tamaño un poco más grueso
    pantalla.bgcolor("Black")
    estrella.speed(1) #Tiempo que tarda en dibujar en escala de 1: muy lento, 10 muy rápido
    for i in range(puntas):
        turtle.forward(20)
        turtle.right(180 - angulo_positivo)
        turtle.forward(20)
        turtle.left(180 - angulo)
    print("Se ha abierto en otra pestaña la estrella que querías")
    turtle.done()
dibujar_estrella()