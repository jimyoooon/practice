from django.shortcuts import render
# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json

@csrf_exempt
def task_list_create(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('-created_at')
        tasks_data = [{"title": task.title, "createdAt": task.created_at} for task in tasks]
        return JsonResponse({"tasks": tasks_data})

    elif request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(title=data['title'])
        return JsonResponse({"title": task.title, "createdAt": task.created_at}, status=201)


# Create your views here.
