def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()

    t = combined.count('t')
    r = combined.count('r')
    u = combined.count('u')
    e = combined.count('e')

    print(f"L occurs {t}")
    print(f"O occurs {r}")
    print(f"V occurs {u}")
    print(f"E occurs {e}")
    total1 = t + r + u + e
    print(f"Total = {total1}")

    l = combined.count('l')
    o = combined.count('o')
    v = combined.count('v')
    e = combined.count('e')
    print(f"L occurs {l}")
    print(f"O occurs {o}")
    print(f"V occurs {v}")
    print(f"E occurs {e}")
    total2 = l+o+v+e
    print(f"Total = {total2}")
    score = int(str(total1) + str(total2))
    print(f"Love Score = {score}")

calculate_love_score('Taye', 'Kehinde'.lower())