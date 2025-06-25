import os
import json
from django.conf import settings
from django.shortcuts import render
from django.http import Http404

file_path = os.path.join(settings.BASE_DIR, 'myproject', 'static', 'dump.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

specialties = [obj for obj in data if obj['model'] == 'data.specialty']

def spec_list(request):
    return render(request, 'myapp/spec_list.html', {'specialties': specialties})

def spec_detail(request, id):
    spec = next((item for item in specialties if item['pk'] == id), None)
    if spec is None:
        raise Http404(f"Квалификация с ID {id} не найдена.")  
    return render(request, 'myapp/spec_details.html', {'spec': spec})

def home(request):
    return render(request, 'myapp/index.html')