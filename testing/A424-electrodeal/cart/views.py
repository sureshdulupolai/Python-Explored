from django.shortcuts import render,redirect
from .models import Cart,CartItem
from products.models import Product

# Create your views here.

def view_cart(request):
    cart,created=Cart.objects.get_or_create(user=request.user)

    template_name="cart.html"
    context={
        "cartitems":cart.cartitem_set.all()
    }
    return render(request,template_name,context)

def add_to_cart(request,productid):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cartitem,cartitem_created=CartItem.objects.get_or_create(cart=cart,product=Product.objects.get(id=productid))
    if cartitem_created:
        cartitem.quantity=1
    else:
        cartitem.quantity+=1
    cartitem.save()
    return redirect("products")

def remove_cartitem(request,cartitem_id):
    cartitem=CartItem.objects.get(id=cartitem_id)
    cartitem.delete()
    return redirect("cart")

def update_cartitem(request):
    pass  

def checkout(request):
    pass