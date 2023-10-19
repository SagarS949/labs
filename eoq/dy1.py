def baseInventory():
  demand = inputDict['demand'][0]

  diffOrder = demand - 1
  maxRange = sum(inputDict['demand']) - demand
  holdingCost = inputDict['holding'][0]
  setupCost = inputDict['setup'][0]
  baseMinInventCost = []

  for x in range(0,maxRange + 1):
    hx = holdingCost * x
    z = x + diffOrder
    CZ = findCost(z, setupCost)
    fx = CZ + hx
    baseMinInventCost.append(fx)

  return baseMinInventCost
