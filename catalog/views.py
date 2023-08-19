from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.
def home_page(request):
    context = {
        'objects_list': Product.objects.all()
    }
    return render(request, 'catalog/home_page.html', context)


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contact_page.html')


# def product_detail(request, id):
#     product = Product.objects.filter(id=id)
#     context = {
#         'name': product.name,
#         'description': product.description
#     }
#
#     print(context)
#     return render(request, 'catalog/product_detail.html', context)
