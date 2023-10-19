optimal_c = max(df['ci'])
df['zi'] = ''
for i in range(4):
  z = (df['beta'][i] / df['residue_var'][i]) * (df['mu-r'][i] - optimal_c)
  df['zi'][i] = z

df["weights"] = ''
for i in range(4):
  df['weights'][i] = df['zi'][i] / sum(df['zi'][:4])
weights_sum = 0
for i in range(4):
    weights_sum += df["weights"][i]
