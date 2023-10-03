def documents_to_shringles(Document):
  k=3
  shringle_set=[]

  for i in Document.keys():
    sentence = Document[i]
    list_of_words = sentence.split()

    #print(list_of_words)
    for j in range(0,len(list_of_words)-(k-1)):
      shringle=""
      for l in range(j,j+k):
         shringle += list_of_words[l]
         if not l==(j+k-1):
          shringle +=" "
      #print(shringle)
      if not shringle in shringle_set:
        shringle_set.append(shringle)

  return shringle_set
