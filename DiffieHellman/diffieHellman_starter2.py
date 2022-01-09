
def order(g, p):

    for i in range(2, p):
        if pow(g, i, p) == g:
            return 1
    return p


p = 28151

for g in range(2, p):
    o = order(g, p)
    if o == p:

        print(f"{g = } is a generator")
        break