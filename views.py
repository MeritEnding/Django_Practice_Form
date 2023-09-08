from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm


def question_create(request):
    form=QuestionForm()
    return render(request,'pybo/question_form.html',{'form':form})

