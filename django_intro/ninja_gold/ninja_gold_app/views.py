from warnings import WarningMessage
from django.shortcuts import render, redirect
import random
from datetime import datetime

Gold_Dict = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (0,50)
}

# Create your views here.
def index(request):
    if 'total_gold' not in request.session or 'activities' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render(request, "index.html")

def process_money(request):
    if request.method == 'GET':
        return redirect('/')
    building_name = request.POST['building']
    building = Gold_Dict[building_name]
    # .upper() puts text in UPPERCASAE
    building_name_upper = building_name[0].upper() + building_name[1:]
    curr_gold = random.randint(building[0], building[1])
    formatted_time = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    message = f"Earned {curr_gold} from the {building_name_upper}! ({formatted_time})"
    if building_name == 'casino':
            if random.randint(0,1) > 0:
                message = f"Entered a {building_name_upper} and lost {curr_gold} golds... Ouch... ({formatted_time})"
                curr_gold = curr_gold * -1
    request.session['total_gold'] += curr_gold
    request.session['activities'].append({"message": message})
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')

