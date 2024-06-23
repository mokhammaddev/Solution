from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Science, Question, Comment, Answer
from .forms import CommentForm


def index(request):
    sciences = Science.objects.all()
    questions = Question.objects.order_by('-id')
    answers = Answer.objects.all()
    ctx = {
        'sciences': sciences,
        'questions': questions,
        'answer': answers,
    }
    return render(request, 'index.html', ctx)


def detail(request, pk):
    article = get_object_or_404(Question, id=pk)
    comments = Comment.objects.filter(question_id=pk)
    comment_form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if not request.user.is_authenticated:
            return redirect('account:login')
        if form.is_valid():
            message = request.POST.get('message')
            author_id = request.user.id
            if article:
                obj = Comment(message=message, question_id=pk, author_id=author_id)
                obj.save()
            return redirect(reverse('detail', kwargs={"pk": pk}))
    ctx = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'detail.html', ctx)


