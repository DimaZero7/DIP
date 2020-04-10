from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse


from .forms import CommentForm, Comment


def comment_processing(request):
    """Обрабатуем запрос на созранение коментария"""

    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form.cleaned_data)

        # if form.is_valid():
        #     new_comment = form.save()
        #     return redirect(new_comment)

        return HttpResponse('asd')




