hora = 0
minuto = 0
segundo = 0

while hora < 24:
    while minuto < 60:
        while segundo < 60:
            print(f"{hora}:{minuto}:{segundo}")
            segundo += 1
        minuto += 1
        segundo = 0
    hora += 1
    minuto = 0
    segundo = 0

print("Fin del reloj")

