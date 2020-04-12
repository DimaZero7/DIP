from django.shortcuts import render, redirect
from django.urls import reverse


from .forms import CommentForm, Comment
from products.models import Product


def comment_processing(request):
    """Обрабатуем запрос на созданение коментария"""

    if request.method == 'POST':

        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            this_product = Product.objects.get(pk=request.POST['product'])
            new_comment.product = this_product
            new_comment.save()
            return redirect(reverse('product:detail', kwargs={'slug': this_product.slug}))

