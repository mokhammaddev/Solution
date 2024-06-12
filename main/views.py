from django.shortcuts import render
from .models import Science, Question


def index(request):
    sciences = Science.objects.all()
    questions = Question.objects.order_by('-id')
    ctx = {
        'sciences': sciences,
        'questions': questions,
    }
    return render(request, 'index.html', ctx)


