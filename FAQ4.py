chislo = 5

mass = [1,2,3,4]

for i in range(len(mass)):
    for j in range(i+1, len(mass)):
        if (mass[i] + mass[j]) == chislo:
            print("Пара чисел:", mass[i], mass[j])
