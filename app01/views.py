from django.shortcuts import render,HttpResponse

# Create your views here.
from app01 import tasks
from celery.result import AsyncResult


def index(request):
    res = tasks.add.delay(5,6)
    print(res)
    return HttpResponse(res.task_id)


# def result(request):
#     id = request.GET.get('id')
#     result = AsyncResult(id)
#     print(result)
#     HttpResponse(result.state)


