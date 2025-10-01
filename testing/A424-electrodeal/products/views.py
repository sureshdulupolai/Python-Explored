from django.shortcuts import render
from products.models import Product,Category
from django.views.generic.detail import DetailView

# Create your views here.
def products(request):
    template_name='products/products.html'
    context={
         'products':Product.objects.all(),
         'categories':Category.objects.all()
    }
    return render(request,template_name,context)

# class Based Views

class ProductDetailView(DetailView):
     model=Product

class CategoryDetailView(DetailView):
     model=Category
     slug_field='slug'
     context_object_name='category'

     def get_context_data(self, **kwargs):
          context=super().get_context_data(**kwargs)
          context['categories']=Category.objects.all()
          return context
     
def search(request):
     # request.GET     request.POST
     search_query=request.GET.get('keyword')
     template_name='products/products.html'
     context={
          'products':Product.objects.filter(name__icontains=search_query)
     }
     return render(request,template_name,context)