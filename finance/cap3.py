df["mu-r"] = f1(df, R)
df.sort_values(by = 'mu-r', ascending = False, inplace = True)
df.reset_index(inplace = True, drop = True)

df["mu-r-e2"] = f2(df["mu"], R, df["beta"], df["residue_var"])
df['cum-mu-r-e2'] = df['mu-r-e2'].cumsum()

df["beta-res"] = f3(df["beta"], df["residue_var"])
df['cum-beta-res'] = df['beta-res'].cumsum()

df["ci"] = f4(market_var, df["cum-mu-r-e2"], df["cum-beta-res"])
