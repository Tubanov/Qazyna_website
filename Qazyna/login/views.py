from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from .forms import ArticleForm
from .forms import LoginUserForm

@csrf_exempt
def add(request):
    return render(request, 'login/add.html')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {'title': "Авторизация"}
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('login:add')

class CustomLoginView:
    pass

@login_required(login_url='/login')  # Перенаправляет на страницу входа, если пользователь не авторизован
def add(request):
    return render(request, 'login/add.html')

def logout_user(request):
    logout(request)
    return redirect('main:index')

@login_required(login_url='/login')  # Перенаправляет на страницу входа, если пользователь не авторизован
def add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('market:market')  # Перенаправление после успешного сохранения
        else:
            # Если форма невалидна, возвращаем её вместе с ошибками
            return render(request, 'login/add.html', {'form': form})
    else:
        # Для GET-запроса просто отображаем пустую форму
        form = ArticleForm()
        return render(request, 'login/add.html', {'form': form})



