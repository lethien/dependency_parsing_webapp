from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from vncorenlp import VnCoreNLP
import phonlp
from jPTDP.jPTDP import jPTDP_model

vncorenlp_model = VnCoreNLP(os.path.join(settings.BASE_DIR, 'dependency_api/vncorenlp/VnCoreNLP-1.1.1.jar'))
phonlp_model = phonlp.load(save_dir=os.path.join(settings.BASE_DIR, 'dependency_api/pretrained_phonlp'))
jptdp_model = jPTDP_model()

def home_page(request):
    return render(request, 'vue_templates/home_page.html')

@api_view(['POST'])
@parser_classes([JSONParser])
def parse_dependency(request):
    """
    List all code snippets, or create a new snippet.
    """
    sentence = request.data['sentence']
    parsemodel = request.data['parsemodel']

    parse_result = None

    try:
        if parsemodel == 'vncorenlp':
            parse_result = vncorenlp_model.annotate(sentence)
            parse_result = parse_result['sentences']
            ss = []
            for s in parse_result:
                ws = [] 
                for w in s:
                    ws.append({'index': w['index'], 'form': w['form'], 'pos': w['posTag'], 'head': w['head'], 'label': w['depLabel']}) 
                ss.append(ws)               
            parse_result = ss
        elif parsemodel == 'phonlp':
            sentences = vncorenlp_model.tokenize(sentence)                   

            ss = []
            for sentence in sentences:
                parse_result = phonlp_model.annotate(text=' '.join(sentence))
                ws = [] 
                wforms = parse_result[0][0]
                ids = [i for i in range(1, len(wforms)+1)]
                poses = [','.join(ps) for ps in parse_result[1][0]]
                ners = parse_result[2][0]
                head_deplabels = parse_result[3][0]          
                heads, deplabels = [], []
                for hd in head_deplabels:
                    heads.append(hd[0])
                    deplabels.append(hd[1])
                for i in range(len(wforms)):
                    ws.append({'index': ids[i], 'form': wforms[i], 'pos': poses[i], 'head': heads[i], 'label': deplabels[i]})
                ss.append(ws)
            parse_result = ss
        elif parsemodel == 'jptdp':
            sentences = vncorenlp_model.tokenize(sentence)
            sentences = [' '.join(s) for s in sentences]
            parse_result = jptdp_model.annotate(sentences)
            
            ss = []
            for s in parse_result:
                ws = []
                for w in s:
                    ws.append({'index': w.id, 'form': w.form, 'pos': w.pred_pos, 'head': str(w.pred_parent_id) if w.pred_parent_id is not None else None, 'label': w.pred_relation})
                ss.append(ws)
            parse_result = ss
        else:
            raise Exception("Invalid Parse Model: " + parsemodel)
        print(parse_result)
        return Response(parse_result)
    except Exception as e:
        print(e)
        return Response(e, status.HTTP_500_INTERNAL_SERVER_ERROR)
