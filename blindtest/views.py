from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse("BlindTest aplication")

def blind_test_question_view(request, question_id):
    question = BlindtestQuestionModel.objects.get(id=question_id)
    return render(request, 'blindtestquestion.html', {'question':question})