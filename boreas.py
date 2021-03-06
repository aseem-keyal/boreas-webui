#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from multiprocessing import Pool
from textblob import TextBlob
from textblob_aptagger import PerceptronTagger
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
    ap_tagger = PerceptronTagger()
    realWords = []
    tossupsBlob = TextBlob(tossups, pos_tagger=ap_tagger)
    pos = ["NN", "VB", "JJ", "NNP"]
    if upper and not lower:
        pos = ["NNP"]
    elif lower and not upper:
        pos = ["NN", "VB", "JJ"]

    for word in tossupsBlob.tags:
        if str(word[1]) in pos:
            realWords.append(word[0])

    return realWords


def getTossups(url):
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
    length = 0
    docs = 0
    for tossup in list:
        if tossup.find(word) != -1:
            sum += tossup.find(word)
            length += len(tossup)
            docs += 1

    if sum == 0:
        sum = 1

    avg = (docs * docs * 100) / float(sum)
    return {'rank': str(avg)[:8], 'tossups': str(docs) + "/" + str(len(list)), 'earliness': str(1 / (float(sum) / length))[:8]}


def constructCollection(answerLines, category, difficulty):
    collection = []
    pool = Pool(processes=4)
    urls = []
    for answerLine in answerLines:
        urls.append("http://quinterest.org/php/search.php?info=" + answerLine + "&categ=" + category + "&difficulty=" + difficulty + "&stype=Answer&tournamentyear=All")
    collection = pool.map(getTossups, urls)
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
