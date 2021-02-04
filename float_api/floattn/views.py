from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the float index.")


def users(request):
    data = {
        "user": "fake user data"
    }
    return JsonResponse(data)
