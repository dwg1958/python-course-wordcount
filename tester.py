import re

string = "cl13@£$%[};'\""
pattern = re.compile('\W')


string = re.sub(pattern, '', string)
print(string.capitalize())


#################################################################
wordtotals = [('Version', 7), ('Django', 6), ('The', 5), ('Of', 4), ('Python', 3), ('To', 3), ('This', 2), ('Tutorial', 2), ('For', 2), ('If', 2)]

for word, totals in wordtotals:

  print(f"{word} = {totals}")

# endfor

print('Making a change to test GIT')
