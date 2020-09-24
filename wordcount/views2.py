from django.http import HttpResponse
from django.shortcuts import render
import operator
import re  # RegEx


#######################################################################
def count(request):
    textreceived = request.GET['fulltext']
    wordlist = textreceived.split()

    # Create a dictionary list for words counts
    wordcountdictionary = {}
    # Prepare RegEx pattern for alphanumerics
    pattern = re.compile('\W')

    for word in wordlist:
        # Strip unwanted characters and Standardise case
        word = (re.sub(pattern, '', word)).capitalize()

        if word in wordcountdictionary:
            wordcountdictionary[word] += 1
        else:
            wordcountdictionary[word] = 1

    # Turn dictionary into list
    wordtotals = wordcountdictionary.items()

    # Now sort it on number - second item i.e. 1
    wordtotals = sorted( wordtotals, key = operator.itemgetter(1), reverse = True )

    # Split off Top 10
    wordtop10 = wordtotals[:10]

    return render(request, 'count.html', { 'fulltext':textreceived, 'wordlist': wordlist, 'dictionary':wordcountdictionary, "wordtotals":wordtotals,'count':len(wordlist), 'wordtotals':wordtop10 })
