from django.contrib.auth.views import LoginView
from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from users.froms import *
from users.models import *


# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'users/login.html', context)


class LoginUserView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'


    def get_context_data(self, **kwargs):
        context = super(LoginUserView, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('products:index')


def register(request):
    return render(request, 'users/register.html')
