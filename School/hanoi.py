def hanoi(n, D, A, I):
    if n > 0:
        hanoi(n-1, D, I, A)
        print("Deplacer le disque", n, "de", D, "vers", A)
        hanoi(n-1, I, A, D)


hanoi(3, "Départ", "Arrivée", "Intermédiaire")
