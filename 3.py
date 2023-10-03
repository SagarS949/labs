def Min_hash(input_Dict):
  No_of_random_shuffles = 3
  Keys_list = list(input_Dict.keys())

  col = len(input_Dict[Keys_list[0]])
  row = No_of_random_shuffles
  arr = [[0 for j in range(col)] for i in range(row)]

  no_of_docs=col
  similarity = [[0 for j in range(no_of_docs)] for i in range(no_of_docs)]

  for i in range(0,No_of_random_shuffles):
    Random_order = random.sample(Keys_list,len(Keys_list))
    print(Random_order)
    for j in range(0,col):
      count=1
      for k in Random_order:
        if input_Dict[k][j] == 1:
          break
        count+=1

      arr[i][j] = count
