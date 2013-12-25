#!/usr/bin/env/python
from bottle import route, run, debug, static_file, template, request
import boreas
import urllib


@route('/search', method='GET')
def search():
    if request.query.getall('answerLine'):
        answerLines = request.query.getall('answerLine')
        for answerLine in answerLines:
            answerLines[answerLines.index(answerLine)] = urllib.quote_plus(answerLine)
        answerLines = list(set(answerLines))
        answerLines = filter(None, answerLines)
        lower = False
        upper = False
        if request.query.case == "lower":
            lower = True
        elif request.query.case == "upper":
            upper = True
        category = request.query.category
        difficulty = request.query.difficulty
        options = boreas.setupOptions(category, difficulty, answerLine, answerLines)
        collection = boreas.constructCollection(answerLines, options['category'], options['difficulty'])
        documentList = boreas.constructDocumentList(collection)
        allAnswerLines = boreas.displayAllAnswerLines(answerLines, documentList, lower, upper, collection)
        if len(answerLines) == 1:
            single = True
        else:
            single = False
        return template('complete.tpl', list=allAnswerLines, names=answerLines, difficulty=difficulty, category=category, single=single)
    else:
        return template('main.tpl')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static/')


debug(True)
run(host='192.168.1.103', port='8555', server='paste')
