from django.shortcuts import render
from django.http import HttpResponse
from .models import BlindtestQuestionModel

import random

# Create your views here.
def index():
    return HttpResponse("Blindtest aplication")

def displayblindtest(request):
    return render(request, 'blindtestquestion.html') 

def blind_test_general_view(request, question_id, pk):
    list_answers = BlindtestQuestionModel.objects.get(pk=pk)
    choices = list_answers.choices[:]
    random.shuffle(choices)
    question = BlindtestQuestionModel.objects.get(id=question_id)
    context = {
        'question':question, 
        'choices': choices
    }
    return render(request, 'blindtestquestion.html', context)

def blind_test_settings(request):
    context = {'question_types': BlindtestQuestionModel}
    return render(request, 'blindtestsetup.html', context)