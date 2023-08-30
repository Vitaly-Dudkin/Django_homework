from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from pytils.translit import slugify
from catalog.models import Product, Category, BlogPost


class ProductListView(ListView):
    model = Product


# def home_page(request):
#     context = {
#         'objects_list': Product.objects.all()
#     }
#     return render(request, 'catalog/product_list.html', context)


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contact_page.html')


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'is_published']
    success_url = reverse_lazy('catalog:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'is_published']
    template_name = 'catalog/blogpost_update_form.html'
    success_url = reverse_lazy('catalog:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('catalog:blogpost_list', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('catalog:blogpost_list')


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_post_detail.html'
    success_url = reverse_lazy('catalog:blogpost_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostRedactorView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_post_edit.html'
    success_url = reverse_lazy('catalog:blogpost_list')
