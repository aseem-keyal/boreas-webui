#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import math
import string
import urllib2
import re


def setupOptions(category, difficulty, answer, answerLines):
        if category is None:
            category = "All"
        if difficulty is None:
            difficulty = "All"

        if answer and answer in answerLines:
            answerLines2 = []
            answerLines2.append(answer)
        elif answer and not answer in answerLines:
            answerLines2 = answerLines
        else:
            answerLines2 = answerLines

        return {'category': category, 'difficulty': difficulty, 'answer': answer, 'answerLines': answerLines, 'answerLines2': answerLines2}


def displayAllAnswerLines(answerLines, documentList, lower, upper, collection):
    allAnswerLines = []
    for answerLine in answerLines:
        allAnswerLines.append(analyzeAnswerLine(answerLine, answerLines, documentList, lower, upper, collection))

    return allAnswerLines


def analyzeAnswerLine(answerLine, answerLines, documentList, lower, upper, collection):
        documentNumber = answerLines.index(answerLine)
        realWords = stripWords(documentList[documentNumber], lower, upper)

        words = {}
        for word in realWords:
            words[word] = tfidf(word, documentNumber, documentList, collection)

        return words


def stripWords(tossups, lower, upper):
    allWords = tossups.split(None)
    commonWords = {"the", "of", "and", "a", "to", "in", "is", "you", "that", "it", "he", "was", "for", "on", "are", "as", "with", "his", "they", "I", "at", "be", "this", "have", "from", "or", "one", "had", "by", "word", "but", "not", "what", "all", "were", "we", "when", "your", "can", "said", "there.", "use", "an", "each", "which", "she", "do", "how", "their", "if", "will", "up", "other", "about", "out", "many", "then", "them", "these", "so", "some", "her", "would", "make", "like", "him", "into", "time", "has", "look", "two", "more", "write", "go", "see", "number", "no", "way", "could", "people", "my", "than", "first", "water", "been", "call", "who", "oil", "its", "now", "find", "long", "down", "day", "did", "get", "come", "made", "may", "part"}
    realWords = [x for x in allWords if x.lower() not in commonWords]

    if upper and not lower:
        realWords = [x for x in realWords if x[0].isupper()]
    elif lower and not upper:
        realWords = [x for x in realWords if not x[0].isupper()]
    return realWords


def getTossups(url, name):
    print "Retrieving " + name + " tossups from Quinterest.org..."
    html = urllib2.urlopen(url).read()

    soup = BeautifulSoup(html)
    page = soup.findAll('p')
    tossups = []
    for tossup in page:
        tossup = str(tossup.contents)
        length = tossup.__len__() - 2
        tossup = tossup[24:length]
        tossup = tossup.translate(string.maketrans("", ""), """!"#$%&'+,./:;<=>*?@\^_`{|}~""")
        tossup = re.sub(r'\(.*?\)', '', tossup)
        tossup = re.sub(r'\[.*?\]', '', tossup)
        tossups.append(tossup)

    return tossups


def getWordRank(list, word):
    sum = 0
    docs = 0
    for tossup in list:
        if tossup.find(word) != -1:
            sum += tossup.find(word)
            docs += 1

    if sum == 0:
        sum = 1

    avg = (docs * docs * 100) / float(sum)
    return {'rank': str(avg)[:8], 'tossups': str(docs) + "/" + str(len(list)), 'earliness': str(10000 / (float(sum) / docs))[:8]}


def constructCollection(answerLines, category, difficulty):
    collection = []
    for answerLine in answerLines:
        tossupList = getTossups("http://quinterest.org/php/search.php?info=" + answerLine + "&categ=" + category + "&difficulty=" + difficulty + "&stype=Answer&tournamentyear=All", answerLine)
        collection.append(tossupList)
    return collection


def constructDocumentList(collection):
    documentList = []
    for answerLine in collection:
        document = " ".join(answerLine)
        documentList.append(document)
    return documentList


def freq(word, document):
    return document.split(None).count(word)


def wordCount(document):
    return len(document.split(None))


def numDocsContaining(word, documentList):
    count = 0
    for document in documentList:
        if freq(word, document) > 0:
            count += 1
    return count


def tf(word, document):
    return (freq(word, document) / float(wordCount(document)))


def idf(word, documentList):
    return math.log(len(documentList) / float(numDocsContaining(word, documentList)))


def tfidf(word, index, documentList, collection):
    tfidf = {'tf-idf': str(tf(word, documentList[index]) * idf(word, documentList) * 100)[:8]}
    wordRank = getWordRank(collection[index], word)
    metrics = dict(tfidf.items() + wordRank.items())
    return metrics
