from catalog.models import Category
from products.models import Product
from manufacture.models import Manufacture
from django.shortcuts import render

#Фильтрация товаров в производителях
def filter(request):
    data = request.POST
    filter = data.get("filter")
    slug = data.get("slug")
    

    #Категории
    if data.get("categories"):
        if filter == 'nameAZ':
            filters = Product.objects.filter(categories__slug=slug).order_by('name')
            context = {"filter_name":"Название A-Z",
                      'filters':filters,
                      }

        if filter == 'nameZA':
            filters = Product.objects.filter(categories__slug=slug).order_by('-name')
            context = {"filter_name":"Название Z-A",
                      'filters':filters,
                      }

        if filter == 'priceIncrement':
            filters = Product.objects.filter(categories__slug=slug).order_by('price')
            context = {"filter_name":"Цена по возрасанию",
                      'filters':filters,
                      }

        if filter == 'priceDeincrement':
            filters = Product.objects.filter(categories__slug=slug).order_by('-price')
            context = {"filter_name":"Цена по убыванию",
                      'filters':filters,
                       }

        if filter == 'dataIncrement':
            filters = Product.objects.filter(categories__slug=slug).order_by('date')
            context = {"filter_name":"Дата по возрастанию",
                      'filters':filters,
                       }

        if filter == 'dataDeincrement':
            filters = Product.objects.filter(categories__slug=slug).order_by('-date')
            context = {"filter_name":"Дата по убыванию",
                      'filters':filters,
                        }
    #Производители
    if data.get("manufacture"):
        if filter == 'nameAZ':
            filters = Product.objects.filter(manufacture__slug=slug).order_by('name')
            context = {"filter_name":"Название A-Z",
                      'filters':filters,
                      }

        if filter == 'nameZA':
            filters = Product.objects.filter(manufacture__slug=slug).order_by('-name')
            context = {"filter_name":"Название Z-A",
                      'filters':filters,
                      }

        if filter == 'priceIncrement':
            filters = Product.objects.filter(manufacture__slug=slug).order_by('price')
            context = {"filter_name":"Цена по возрасанию",
                      'filters':filters,
                      }

        if filter == 'priceDeincrement':
            filters = Product.objects.filter(manufacture__slug=slug).order_by('-price')
            context = {"filter_name":"Цена по убыванию",
                      'filters':filters,
                       }

        if filter == 'dataIncrement':
            filters = Product.objects.filter(manufacture__slug=slug).order_by('date')
            context = {"filter_name":"Дата по возрастанию",
                      'filters':filters,
                       }

        if filter == 'dataDeincrement':
            filters = Product.objects.filter(manufacture__slug=slug).order_by('-date')
            context = {"filter_name":"Дата по убыванию",
                      'filters':filters,
                        }
        
    return render(request, 'filter/result_filter.html', context)
