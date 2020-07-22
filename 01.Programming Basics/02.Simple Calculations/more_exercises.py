daljina = float(input())
shirochina = float(input())
strana = float(input())

zala_golemina = (daljina * 100) * (shirochina * 100)
garderob = pow(strana * 100, 2)
peika = zala_golemina / 10
svobodno = zala_golemina - (garderob + peika)
tanciori = svobodno // (40 + 7000)

print(round(tanciori))
