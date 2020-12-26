from django.core.checks import messages
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, UserProfileForm, UserRegisterForm
from django.contrib import auth, messages
from django.urls import reverse
from basketapp.models import Basket

def login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = ShopUserLoginForm()
    context = {'form': form}
    return render(request, 'authapp/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'authapp/register.html', context)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.author = request.user
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    baskets = Basket.objects.filter(user=request.user)
    context = {
        'title': 'Профиль',
        'baskets': baskets,
        'form': form,
        'total_quantity': sum(basket.quantity for basket in baskets),
        'total_sum': sum(basket.sum() for basket in baskets),

    }
    return render(request, 'authapp/profile.html', context)

