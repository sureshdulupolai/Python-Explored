from django.urls import path
from . import views
urlpatterns = [
    path('',views.view_cart,name="cart") ,
    path('add-to-cart/<int:productid>',views.add_to_cart,name='add-to-cart'),
    path('remove-cartitem/<int:cartitem_id>',views.remove_cartitem,name="remove-cartitem")
]
