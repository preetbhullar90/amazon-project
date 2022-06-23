from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe



def checkout(request):
    # stripe_public_key = settings.STRIPE_PUBLIC_KEY
    # stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = 'pk_test_51LDT5BKbsS5C0b4dtWq1EIcQ3TNCJdKuWcLUzsasoxE77YklV3c9gl1rFy9RFNWHfrDxocucnRKAeg3oQLm4mjZx00dB425pXq'
    stripe_secret_key = 'sk_test_51LDT5BKbsS5C0b4dJ1oD45nkLXIgxJ4FmRmjVhKj8qfVN27fdzVV4O7gIkgiIjMvruw977SKscPzGuPwPZBmozE700ZtNFy8R7'
    
  
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
   

    order_form = OrderForm()
    
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51LDT5BKbsS5C0b4dtWq1EIcQ3TNCJdKuWcLUzsasoxE77YklV3c9gl1rFy9RFNWHfrDxocucnRKAeg3oQLm4mjZx00dB425pXq', 
        'client_secret': 'test client secret',
    }


    return render(request, template, context)
