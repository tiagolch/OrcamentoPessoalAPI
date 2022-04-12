from django.shortcuts import render
# import user
from django.contrib.auth.models import User


def Dashboard(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'dashboard.html', {'user': user})
    return render(request, 'dashboard.html')

