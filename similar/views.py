from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Questions

# Create your views here.
def index(request):
    lastest_question_list = Questions.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": lastest_question_list,
    }
    return render(request, "similar/index.html",context)

def detail(request, question_id):
    return HttpResponse("C'est la question n° %s" % question_id)

def results(request, question_id):
    response = "VOus regardez la question %s"
    return HttpResponse(response % question_id)

def answers(request, question_id):
    return HttpResponse("Voiçi la réponse  %s" % question_id)