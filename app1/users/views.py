from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import RegisterForm

from django.contrib.auth import authenticate
from django.contrib.auth import login as lg 
from orders.models import Order
from catalog.models import Catalog
from catalog.models import Rating
from users.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email1')
        password1 = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password1)
        
        if user is not None:
            lg(request, user)
            if request.user.role == 'Cook':
                return redirect('application_c')
            elif request.user.role == 'Administrator':
                return redirect('application')
            else:
                return redirect('index')
    context = {
        'title':'Вход',
    }

    return render(request,'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'title':'Регистрация',
        'form':form,
    }

    return render(request,'users/register.html', context)


def recovery(request):
    context = {
        'title':'Users',
        'content':'Вы находитесь на странице recovery'
    }
    return render(request,'users/recovery.html', context)

@login_required
def Profile(request):
    context = {
        'title':'Профиль',
    }
    return render(request,'users/profile.html', context)
@login_required
def Your_orders(request):
    order = Order.objects.filter(user_name = request.user)
    check = []
    for order1 in order:
        check.append(Rating.objects.filter(user = request.user, order = order1).exists())
    check1 = zip(order,check)
    context = {
        'title':'Заказы',
        'order':check1,
    }
    return render(request,'users/order_user.html', context)

@login_required
def Get_order(request,id_ord):
    order = Order.objects.get(id = id_ord)
    order.take_order = True
    order.save()
    return redirect('add_to_comment', id_ord)

@login_required
def Add_to_comment(request,id_ord):
    order1 = Order.objects.get(id = id_ord)
    rat = False
    if Rating.objects.filter(user=request.user, order=order1).exists():
        rat = False
    else:
        rat = True
    context = {
        'title':'Оценка заказа',
        'order':order1,
        'rating1':rat,
    }
    return render(request,'users/view_comment.html', context)

def Add_to_comment2(request,id_ord):
    order1 = Order.objects.get(id = id_ord)
    if not(Rating.objects.filter(user=request.user, order=order1).exists()):
        catalog = Catalog.objects.get(name = order1.structure)
        comment = Rating.objects.create(
            user = request.user,
            catalog = catalog,
            order = order1,
            rating = request.POST.get('estimation'),
            created_at = timezone.now(),
        )
        comment.save()
    context = {
        'title':'Оценка заказа',
        'order':order1,
    }
    return render(request,'users/view_comment.html', context)

@login_required
def Comment(request):
    rating = Rating.objects.filter(user = request.user)
    context = {
        'title':'Мои оценки за заказы',
        'rating':rating,
    }

    return render(request,'users/comment.html', context)

@login_required
def Delete_comment(request, id_comment):
    Rating.objects.get(id = id_comment).delete()
    return redirect('comment')

@login_required
def Personal_data(request):
    userData = User.objects.get(email = request.user.email)
    context = {
        'title':'Users',
        'content':'Вы находитесь на странице userData',
        'userData':userData,
    }

    return render(request,'users/personal_data.html', context)

@login_required
def Allergens(request):
    context = {
        'title':'Выбор аллергенов',
    }
    return render(request,'users/preferences.html', context)

@login_required
def Change_allergens(request):
    fish = bool(request.POST.get('option1'))
    chicken = bool(request.POST.get('option2'))
    lactose = bool(request.POST.get('option3'))
    user1 = User.objects.get(id = request.user.id)
    user1.fish = fish
    user1.chicken = chicken
    user1.lactose = lactose
    user1.save()
    return redirect('allergens')