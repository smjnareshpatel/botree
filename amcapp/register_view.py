from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate
# Create your views here.

def register_view(request):

    print(request.user.is_authenticated())


    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        # login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/login/?next=/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "authentication/register.html", context)
