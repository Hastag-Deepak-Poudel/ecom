from django.urls import path
from . import views
from .views import *

app_name = "shop"

urlpatterns = [
    # show the dashboard
    path('', ListItems.as_view(), name="listitem"),
    # To delete items
    path('<pk>/delete/', DeleteListView.as_view(), name="delete_confirm"),
    # To update an item
    path('<pk>/update', UpdateListView.as_view(), name="update_list"), 
    # Show details of the seleced item
    path('<pk>/detail', views.show_details, name="show_details"), 
    # To search items 
    path('search/', views.post_search, name='post_search'),

    path('contact/', views.contactus, name='contactus'),

    # Related to Cart

    path('cart/', views.view_cart, name='view_cart'),

    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),

    path('delete/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
]