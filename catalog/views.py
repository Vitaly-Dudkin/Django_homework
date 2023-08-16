from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.
def home_page(request):
    return render(request, 'catalog/home_page.html')


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contact_page.html')




def product(request):
    context = {
        'object_list': Category.objects.all()
    }
    return render(request, 'catalog/product.html', context)
