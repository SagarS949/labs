rows = len(inputDict["Regular"])*2
cols = len(inputDict["Demand"])
mat = [[0 for i in range(cols)] for j in range(rows)]
#fill regular demand
for i in range(0,len(regular)):
  output = min(regular[i], demand[i])
  demand[i] -= output
  regular[i] -= output
  mat[i*2][i] = output

#fill overtime demand
for i in range(0, len(overtime)):
  output = min(overtime[i], demand[i]);
  demand[i] -= output
  overtime[i] -= output
  mat[(i*2) + 1][i] = output

  if(demand[i] > 0):
    for j in reversed(range(i)):
      output = min(overtime[j], demand[i])
      if(output > 0):
        demand[i]-= output
        overtime[j] -= output
        mat[(j*2)+1][i] = output

surplus = 0
for i in range(len(regular)):
  surplus += regular[i]
  surplus += overtime[i]

print("The surplus:",surplus)
