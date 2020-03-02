from django.views.generic import View
from django.shortcuts import render
from .models import Category, Product, Comment
from .utils import ObjectDetailMixin, CommentCreateView

def category_list(request):
    context = {

    }
    return render(request, 'catalog/categorys/category_list.html', context)


class CategoryDetail(ObjectDetailMixin, View):
    model = Category
    template = 'catalog/categorys/category_detail.html'


class ProductDetail(ObjectDetailMixin, View):
    model = Product;
    template = 'catalog/categorys/products/products_detail.html'

# **********************************
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['comment'] = Comment.objects. all()
        context['form'] = CommentForm()
        return context
# **********************************
class CommentDetail(CommentCreateView, View):
    model = Comment;
    template = 'catalog/categorys/products/products_detail.html'

