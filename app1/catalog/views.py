from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from catalog.models import Catalog, Box, BuyBox, Rating
from django.db.models import Q
# Create your views here.
@login_required
def Menu(request):
    catalog_test = Q()
    if request.GET.get('option1'):
        test = False
        catalog_test |= Q(fish = True)
    else:
        test = True
    if request.GET.get('option2'):
        test2 = False
        catalog_test |= Q(chicken = True)
    else:
        test2 = True
    if request.GET.get('option3'):
        test3 = False
        catalog_test |= Q(lactose = True)
    else:
        test3 = True
    
    catalog1 = Catalog.objects.all()
    if catalog_test:
        catalog1 = catalog1.exclude(catalog_test)



    if request.GET.get('apply_profile_filters'):
        catalog_test1 = Q()
        if request.user.fish:
            catalog_test1 |= Q(fish = True)
        if request.user.chicken:
            catalog_test1 |= Q(chicken = True)
        if request.user.lactose:
            catalog_test1 |= Q(lactose = True)
        if catalog_test1:
            catalog1 = catalog1.exclude(catalog_test1)
    
    
    rating_in_html = []
    for check in catalog1:
        check1 = Rating.objects.filter(catalog = check)
        total = 0
        sch = 0
        for comment in check1:
            total += comment.rating
            sch+=1
        if sch == 0:
            rating_in_html.append('Оценок пока нет')
        else:
            rating_in_html.append(round(total/sch, 1))
    catalog2 = zip(catalog1,rating_in_html)

    context = {
        'title':'Меню',
        'catalog':catalog2,
        'op':test,
        'op2':test2,
        'op3':test3,
    }

    return render(request,'catalog/catalog.html', context)



@login_required
def Box_(request):
    box = Box.objects.all()
    box1 = ''
    if request.user.is_authenticated:
        box2 = BuyBox.objects.filter(user_name = request.user)
        for boxx in box2:
            if boxx.user_name == request.user:
                box1 = 'No, but'
        if box1 == '':
            box1 = 'Yes'
    context = {
        'title':'Наборы',
        'box':box,
        'box2':box1,
    }

    return render(request,'catalog/box.html', context)


from datetime import date, timedelta
@login_required
def buybox(request,id_box):
    box = Box.objects.get(id = id_box)
    BuyBox.objects.create(
        name = box.name,
        count1 = box.count1,
        price = box.price,
        user_name = request.user,
        created_at = date.today(),
        end_box = date.today() + timedelta(days=box.count1),
    )
    return redirect('box')
@login_required
def Detail(request,id_card):
    card = Catalog.objects.get(id = id_card)
    rating1 = Rating.objects.filter(catalog = card)
    context = {
        'title':'Menu',
        'content':'Вы находитесь на странице подробности товара',
        'card':card,
        'rating_from_views':rating1,
    }

    return render(request,'catalog/detail.html', context)