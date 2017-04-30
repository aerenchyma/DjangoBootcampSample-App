from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('samplepolls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context,request))
# Check out the docs for more explanation of this



#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#
def detail(request, question_id):
    return HttpResponse("You're looking at question {}".format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {}"
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))
#
