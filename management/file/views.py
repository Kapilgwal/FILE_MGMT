from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.
def home(request):
    return JsonResponse({'msg' : 'Hello this is Initial package'})