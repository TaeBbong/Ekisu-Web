from django.shortcuts import render
from . import forms
from . import papago
from . import textrank


# Create your views here.
def main(request):
    inputContent = '영문을 입력하세요.'
    outputContent = '결과가 나타납니다.'
    if request.method == 'GET':
        return render(request, 'ekisu/index.html', {'inputContent': inputContent, 'outputContent': outputContent})

    elif request.method == 'POST':
        form = forms.TextForm(request.POST)
        if form.is_valid():
            engStr = str(form['inputContent'].value())
            ratio = str(form['ratio'].value())

            korStr = papago.translate(engStr)
            f = open('input.txt', 'w', encoding='utf-8')
            f.write(korStr)
            f.close()

            tr = textrank.TextRank()
            ratio = int(ratio[:2]) * 0.01
            print('Load...')
            from konlpy.tag import Komoran

            tagger = Komoran()
            stopword = set([('있', 'VV'), ('하', 'VV'), ('되', 'VV')])
            tr.loadSents(textrank.RawSentenceReader('input.txt'),
                         lambda sent: filter(lambda x: x not in stopword and x[1] in ('NNG', 'NNP', 'VV', 'VA'),
                                             tagger.pos(sent)))
            print('Build...')
            tr.build()
            ranks = tr.rank()
            for k in sorted(ranks, key=ranks.get, reverse=True)[:100]:
                print("\t".join([str(k), str(ranks[k]), str(tr.dictCount[k])]))

            resultStr = tr.summarize(ratio)

            return render(request, 'ekisu/index.html', {'inputContent': engStr, 'outputContent': resultStr})