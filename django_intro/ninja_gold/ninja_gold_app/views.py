from django.shortcuts import render, redirect
import random

gold_fund_dict = {
        'farm': (10,20),
        'cave': (5,10),
        'house': (2,5),
        'casino': (-50,50)
    }

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, "index.html")

def process_money(request):
    building_range = gold_fund_dict[request.POST['building']]
    amount_of_gold = random.randint(building_range[0], building_range[1])
    request.session['gold'] += amount_of_gold
