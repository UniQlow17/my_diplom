from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserForm

User = get_user_model()


@login_required
def user_edit(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:detail')
    else:
        form = UserForm(instance=user)

    return render(
        request,
        'users/users_edit.html',
        {'form': form, 'image': user.image}
    )


@login_required
def user_detail(request):
    user = User.objects.get(id=request.user.id)
    context = {'user': user}
    return render(request, 'users/users_detail.html', context)
