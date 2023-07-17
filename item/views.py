from django.shortcuts import render
from .models import Items
from django.contrib.admin.views.decorators import user_passes_test


@user_passes_test(lambda u: u.is_staff, login_url='/admin/login/')
def show_items_admin(request):
    items = Items.objects.all()

    return render(request, 'showitems.html', {'items': items})


def show_items(request):
    items = Items.objects.all()

    return render(request, 'showitems.html', {'items': items})
