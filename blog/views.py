from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from blog.models import Account, Projects, Messages
from blog.validators import check_email


class MainPageView(ListView):
    model = Account
    template_name = "main.html"
    context_object_name = "account"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Projects.objects.all()
        return context


def SendMessageView(request):
    if request.method == 'POST':
        data = request.POST
        body = data.get('body', None)
        name = data.get('name', None)
        email = data.get('email', None)
        if check_email(email) == False:
            return HttpResponse("<h1>Hackerlik yaxshi emas, formani to'ldiring:(</h1>")
        if body and name and email:
            message = Messages(name=name, email=email, body=body)
            message.save()
            return HttpResponse("<h1>Xabaringiz yuborildi, etiboringiz uchun raxmat</h1>")
        else:
            return HttpResponse("<h1>Hackerlik yaxshi emas, formani to'ldiring:(</h1>")

    return redirect('/')


