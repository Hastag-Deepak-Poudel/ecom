from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ListItems(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "object_list"
    paginate_by = 6


class DeleteListView(LoginRequiredMixin, DeleteView):
    login_url = 'user:login'
    model = Product
    success_url = "/"
    template_name = "shop/delete_confirm.html"



class UpdateListView(LoginRequiredMixin, UpdateView):
    login_url = 'user:login'
    model = Product
    success_url = "/"
    fields = "__all__"
    template_name = "shop/update_list.html"

@login_required(login_url="user:login")
def show_details(request, pk):
    item = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/detail.html', {'item': item})


@login_required(login_url="user:login")
def post_search(request):

    # Search Items Code

    query = request.GET.get('q')

    object_list = Product.objects.all()

    if query:
        object_list = object_list.filter(title__icontains=query)

    return render(request, 'shop/index.html', {
        'object_list': object_list
    })

@login_required(login_url="user:login")
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required(login_url="user:login")
def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product, user = request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:show_details',pk)


@login_required(login_url="user:login")
def remove_from_cart(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    cart_item.delete()
    return redirect('shop:listitem')


@login_required(login_url='user:login')
def contactus(request):
    return render(request, 'shop/contactus.html')