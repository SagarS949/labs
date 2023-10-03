  for i in range(0,no_of_docs):
    for j in range(0,no_of_docs):
      if i==j:
        similarity[i][j] = 1
      else:
        count=0
        for k in range(0,row):
          if(arr[k][i]==arr[k][j]):
            count+=1

        similarity[i][j] = count/row
