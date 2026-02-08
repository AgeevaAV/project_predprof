from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from administrator.models import Applications
from orders.models import Order
from cook.models import Food
# Create your views here.
def Create_application(request):
    application = request.POST.get('urgency')
    product_name = request.POST.get('product_name1')
    product_weight = request.POST.get('product_weight','0')
    if application == 'urgent':
        Applications.objects.create(
            product = product_name,
            weight = product_weight,
            fast = True
        )
    if application == 'normal':
        Applications.objects.create(
            product = product_name,
            weight = product_weight,
            fast = False
        )
    return redirect('application_c')
def Application_C(request):
    context = {
        'title':'Заявки на продукты',
    }
    return render(request,'cook/application.html', context)

def Food_change(request):
    for product in Food.objects.all():
        weight_field = f"product_weight1_{product.id}"
        new_weight = request.POST.get(weight_field)
        if new_weight:
            product.weight = new_weight
            product.save()
    return redirect('remaining')

def Remaining_C(request):
    food = Food.objects.all()
    order = Order.objects.filter(take_order=False, ready = True)
    name_arr = []
    remaining_arr = []
    for ord in order:
        name_arr.append(ord.structure)
    name_arr = set(name_arr)
    for name in name_arr:
        dop = Order.objects.filter(take_order=False, structure = name, ready = True)
        remaining = 0
        for dop1 in dop:
            remaining += dop1.count1
        remaining_arr.append(remaining)
    onswer = zip(name_arr,remaining_arr)
    context = {
        'title':'Остаток',
        'food':food,
        'order': onswer,
    }

    return render(request,'cook/remaining.html', context)


def Ready_change(request, id_order):
    order = Order.objects.get(id = id_order)
    order.ready = True
    order.save()
    return redirect('control')
def Control_C(request):
    order = Order.objects.filter(ready = False)

    context = {
        'title':'Контроль',
        'Order':order,
    }

    return render(request,'cook/control.html', context)

def Accounting_C(request):
    lunch = Order.objects.filter(breakfast_or_lunch = 'обед')
    lunch_arr = []
    for lunch_1 in lunch:
        lunch_arr.append(lunch_1.structure)
    lunch_arr = set(lunch_arr)

    breakfast = Order.objects.filter(breakfast_or_lunch = 'завтрак')
    breakfast_arr = []
    for breakfast_1 in breakfast:
        breakfast_arr.append(breakfast_1.structure)
    breakfast_arr = set(breakfast_arr)

    lunch_ready_arr = []
    breakfast_ready_arr = []
    lunch_not_ready_arr = []
    breakfast_not_ready_arr = []

    for lunch_name in lunch_arr:
        lunch_arr2 = Order.objects.filter(breakfast_or_lunch = 'обед', structure = lunch_name)
        lunch_ready = 0
        lunch_not_ready = 0
        for name in lunch_arr2:
            if name.ready == True:
                lunch_ready +=1
            if name.ready == False:
                lunch_not_ready +=1
        lunch_ready_arr.append(lunch_ready)
        lunch_not_ready_arr.append(lunch_not_ready)
    for breakfast_name in breakfast_arr:
        breakfast_arr2 = Order.objects.filter(breakfast_or_lunch = 'завтрак', structure = breakfast_name)
        breakfast_ready = 0
        breakfast_not_ready = 0
        for name2 in breakfast_arr2:
            if name2.ready == True:
                breakfast_ready +=1
            if name2.ready == False:
                breakfast_not_ready +=1
        breakfast_ready_arr.append(breakfast_ready)
        breakfast_not_ready_arr.append(breakfast_not_ready)


    lunch1 = zip(lunch_arr,lunch_ready_arr,lunch_not_ready_arr)
    breakfast1 = zip(breakfast_arr,breakfast_ready_arr,breakfast_not_ready_arr)
    context = {
        'title':'Учет',
        'lunch':lunch1,
        'breakfast':breakfast1,
    }

    return render(request,'cook/accounting.html', context)