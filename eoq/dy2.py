def helper(period,MinInvestCost):
  demand = inputDict['demand'][period - 1]

  maxRange = 0
  for i in range(period, len(inputDict['demand'])):
    maxRange += inputDict['demand'][i]

  diffZ = demand
  holdingCost = inputDict['holding'][period -1]
  setupCost = inputDict['setup'][period - 1]

  finalFxList = []

  for x in range(0, maxRange + 1):
    fxList = []
    for z in range(0, x + diffZ + 1):
      hx = holdingCost * x
      CZ = findCost(z, setupCost)
      fxList.append(CZ + hx + MinInvestCost[x - z + demand])
    finalFxList.append(min(fxList))

  return finalFxList
