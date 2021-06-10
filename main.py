#Lab_3    Darcy and Mohamed
#Question 1

x = [(s) for s in input("Insert some words and integer: \n").split()] 
 
def int_or_word(x):
  List_int = []
  List_words = []
  for i in (x):
    if i.isdigit() == True:
      List_int.append(i)
    elif i.isdigit()== False: 
      List_words.append(i)
  return print('The integer list is: \n',List_int, '\n' 'The words list is : \n',List_words)

def sec_in_dec(x):
  List_int = []
  for i in (x): 
    if i.isdigit()== True:
      List_int.append(i)
  for l in range(List_int[::2]):
    return l 
