terms = []

for a in range(2,101):
    for b in range(2, 101):
        n = a ** b
        if not (n in terms):
            terms.append(n)
print(len(terms))
