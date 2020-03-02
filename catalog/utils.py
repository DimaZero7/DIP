from django.shortcuts import render, get_object_or_404
from .models import Category, Comment
from .forms import CommentForm


def menu(request):  # Функция для работы списка категорий
    return {
        'categorys': Category.objects.all(),
    }


class ObjectDetailMixin:  # Общий шаблон для карточек чего либо
    model = None  # Модель обекта которого хотим найти
    template = None  # Шаблон для обекта

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)  # Текущая обект (категория, продукт)
        context = {
            self.model.__name__.lower(): obj,

        }
        return render(request, self.template, context)


# **********************************
class CommentCreateView:
    model = Comment
    form_class = CommentForm

    def get_success_URL(self):
        return reverse ('detail', kwargs = {'slug':self.object.post.slug})

    def form_valid(self, form):
        post = get_object_or_404(Product, slug = self.kwargs ['slug'])
        Form.instance.post = Product
        return super().form_valid(form)