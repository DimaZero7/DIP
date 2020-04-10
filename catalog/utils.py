from .models import Category


def menu(request):
    """Предстовление меню с категориями передаеться в контекст-процессор и подключаеться на все страницы"""
    return {
        'categories': Category.objects.all(),
    }