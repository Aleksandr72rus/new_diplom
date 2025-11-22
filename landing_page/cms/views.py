from django.shortcuts import render
from .models import CmsSlider
from price.models import PriceCard, PriceTable
from crm.models import Order
from crm.forms import OrderForm


def first_page(request):
    slider = CmsSlider.objects.all()
    price_card = PriceCard.objects.all()
    price_table = PriceTable.objects.all()
    form = OrderForm()
    context = {
        'slider': slider,
        'price_card': price_card,
        'price_table': price_table,
        'form': form,
    }
    return render(request, 'cms/index.html', context)


def thanks_page(request):
    if request.POST:
        theme = request.POST['theme']
        short = request.POST['short']
        name = request.POST['name']
        phone = request.POST['phone']
        order_el = Order(order_theme=theme, order_name=name, order_phone=phone)
        order_el.save()
        return render(request, 'cms/thanks.html', {'name': name})
    else:
        return render(request, 'cms/thanks.html')

