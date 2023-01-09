from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import auth, messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import *
from users.models import *
from products.models import Basket


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


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_message = 'Thanks for authorisation!'

    def get_context_data(self, **kwargs):
        context = super(LoginUserView, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('products:index')


class RegisterUserView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = "%(username)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super(RegisterUserView, self).get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            username=self.object,
        )


@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST,
                               files=request.FILES)  # for saving files and updating user information
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserProfileForm(
            instance=request.user)  # When making a get request, we pass an instance of the user to the form
    baskets = Basket.objects.filter(user=request.user)
    context = {
        'title': 'Store - Profile',
        'form': form,
        'baskets': baskets,
    }
    return render(request, 'users/profile.html', context)


@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
