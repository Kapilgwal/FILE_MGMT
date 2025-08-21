
from django.urls import path,include

urlpatterns = [
    path('',include('file.urls')),
    path('accounts/',include('accounts.urls'))
]
