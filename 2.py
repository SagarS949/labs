def shringle_set_to_dictionary(shringle_set,Document):
  input_Dictionary={}
  ch = 'A'
  n = len(Document)
  for i in shringle_set:
    value=[0 for j in range(n)]
    index=0
    for j in Document.keys():
      if i in Document[j]:
        value[index]=1
      else:
        value[index]=0
      index = index+1
    input_Dictionary[ch] = value
    ch = chr(ord(ch) + 1)

  print(input_Dictionary)
  return input_Dictionary
