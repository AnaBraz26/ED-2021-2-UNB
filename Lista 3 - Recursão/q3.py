def divisores(a, b):
    if b == 0:
        return a
    else:
        return divisores(b, a % b)

q1,q2 = input().split(" ")

q1 = int(q1)
q2 = int(q2)

print(divisores(q1,q2))

