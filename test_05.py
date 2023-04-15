# código para una pistola
balas = int(input())
hit = 0
for i in range(balas):
    disparo = input()
    if disparo == "Hit!":
        hit += 1
print(hit)

