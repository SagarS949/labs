def f3(beta, residue_var):
    l = []
    for i in range(len(beta)):
        l.append(round((beta[i]**2 / residue_var[i]), 4))
    return l

def f4(market_var, cumsum1, cumsum2):
    l = []
    for i in range(len(cumsum1)):
        l.append((market_var * cumsum1[i]) / (1 + (market_var * cumsum2[i])))
    return l
