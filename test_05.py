balas = int(input())
hit = 0
for i in range(balas + 1):
    disparo = input()
    if disparo == "Hit!":
        hit += 1
print(hit)
