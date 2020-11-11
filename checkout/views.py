from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your cart yet")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HHVgnEZk9FUg55goCy94YQ38XKcfCaA7KQkHiyrcSMFjh0sc1s5Vbp4g0DnVvjVynwsKHkgbsluw5QmmnpHrd8s00V6eGwkmy'
    }

    return render(request, template, context)
