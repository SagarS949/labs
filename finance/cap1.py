def f1(df, R):
    l = []
    for i in range(len(df)):
        l.append(round((df.mu[i] - R) / df.beta[i] , 4))
    return l

def f2(mu, R, beta, residue_var):
    l = []
    for i in range(len(mu)):
        l.append(round(((mu[i] - R) * beta[i]) / residue_var[i] , 4))
    return l

