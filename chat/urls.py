from django.urls import path
from chat.views.chat import lobby

urlpatterns = [
    path('', lobby)
]
