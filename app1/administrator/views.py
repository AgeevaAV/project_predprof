from django.shortcuts import render, redirect
from django.http import HttpResponse
from administrator.models import Applications,Income
from orders.models import Order
from django.utils import timezone
from datetime import date, timedelta
from catalog.models import BuyBox
# Create your views here.

def Approve_application(request,id_application):
    application = Applications.objects.get(id = id_application)
    application.aggre_or_disagree = True
    application.save()
    return redirect('application')

def Reject_application(request,id_application):
    application = Applications.objects.get(id = id_application)
    application.aggre_or_disagree = False
    application.save()
    return redirect('application')

def Application_A(request):
    application = Applications.objects.filter(aggre_or_disagree = None)
    applicationT = Applications.objects.filter(aggre_or_disagree = True)
    applicationF = Applications.objects.filter(aggre_or_disagree = False)
    application2 = applicationT | applicationF
    context = {
        'title':'Заявки',
        'application':application,
        'application2':application2,
    }

    return render(request,'administrator/application.html', context)

def Statistics_A(request):
    day_order = 0
    week_orders = 0
    month_orders = 0
    today = date.today()
    daily = Order.objects.filter(created_at__date = today)
    for day in daily:
        day_order += day.count1
    weekly = Order.objects.filter(created_at__date__gte = today - timedelta(days=7))
    for week in weekly:
        week_orders += week.count1
    monthly = Order.objects.filter(created_at__date__gte = today - timedelta(days=30))
    for month in monthly:
        month_orders += month.count1

    daily_people = Order.objects.filter(created_at__date = today, take_order = True).count

    weekly_people = Order.objects.filter(created_at__date__gte = today - timedelta(days=7), take_order = True).count

    monthly_people = Order.objects.filter(created_at__date__gte = today - timedelta(days=30), take_order = True).count

    context = {
        'title':'Статистика',
        'day_orders':day_order,
        'week_orders':week_orders,
        'month_orders':month_orders,
        'day_orders_people':daily_people,
        'week_orders_people':weekly_people,
        'month_orders_people':monthly_people,
    }

    return render(request,'administrator/statistics.html', context)

def Reports_A(request):
    income = Income.objects.get(id = 1)
    if request.GET.get('option1'):
        inc = int(request.GET.get('option1'))
        income.expenses = inc
        income.save()
    orders = Order.objects.all()
    total = 0
    for ord in orders:
        total += ord.priceAll
    box = BuyBox.objects.all()
    for box1 in box:
        total+=box1.price
    get = 0
    dont_get = 0
    getO = Order.objects.filter(take_order = True)
    dont_getO = Order.objects.filter(take_order = False)
    for get1 in getO:
        get+=get1.count1
    for get2 in dont_getO:
        dont_get+=get2.count1
    income.purchases = total
    income.income = income.purchases - income.expenses
    context = {
        'title':'Учет',
        'gett':get,
        'dont_get':dont_get,
        'income':income,
    }

    return render(request,'administrator/reports.html', context)