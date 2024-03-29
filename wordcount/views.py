
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'hello.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordDict = {}

    for word in wordlist:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    sortedWord = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'numberword':len(wordlist), 'sortedWord':sortedWord} )
