from django.http import HttpResponse
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from CHATBOT_NLP_FINAL_CORE_V4.predict import predict
# Create your views here.


def index(request):
    return render(request, 'pages/home.html')


@csrf_exempt
def question(request):
    optx = json.loads(request.body)
    try:
        result = predict(optx['question'])
    except:
        print("result erol:*********")
        result = "tôi không biết"
    data = {
        'reply': result,
        'hit': 'hit',
    }
    return HttpResponse(json.dumps(data), content_type='application/json')