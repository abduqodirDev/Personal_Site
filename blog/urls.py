from django.urls import path
from blog.views import MainPageView, SendMessageView


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('send-message/', SendMessageView, name='send_message'),
]
