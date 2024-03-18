def nb_year(p0, percent, aug, p):
    # your code
    tahun = 0 
    while p0 < p:
        p0 += int(p0 * (percent / 100)) + aug
        tahun += 1
    return tahun