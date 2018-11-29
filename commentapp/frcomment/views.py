# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Comment, Question
from .forms import CommentForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        new_comment = Comment(name=request.POST['name'], email=request.POST['email'], comment=request.POST['comment'], question_id=request.POST['question_id'])
        new_comment.save()

        return redirect('index')

    else:
        form = CommentForm()

    comment = Comment.objects.order_by('-date_created')

    question = Question.objects.order_by('-date_created')
    context = {'comments': comment, 'question': question, 'form': form}
    return render(request, 'frcomment/index.html', context)
