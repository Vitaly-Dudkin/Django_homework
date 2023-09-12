import random
import secrets

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users import services
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verify')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            verification_code = secrets.token_urlsafe(nbytes=7)
            self.object.code = verification_code
            #
            # url = reverse('users:verification', args=[verification_code])
            # total_url = self.request.build_absolute_uri(url)
            # services.send_verification_url(total_url, self.object.email)
            send_mail(
                subject='verification code',
                message=f"There's a new code {verification_code}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email]
            )
            self.object.save()

        return super().form_valid(form)

        #         instance.save()
        #     return super().form_valid(form)
        # send_mail(
        #     subject='You change your password',
        #     message=f"There's a new password {new_password}",
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[request.user.email]
        # )
        # return super().form_valid(form)


# class Verify(UpdateView):
#     model = User
#     template_name = 'users/verify.html'
#     success_url = 'catalog/home_page'
#
#     def form_valid(self, form):
#         if user.code == code:
#             user.is_active = True
#             user.save()
#
#     return render(request, 'users/verify.html')


def verify(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if user.code == code:
            user.is_active = True
            user.save()
            return redirect(reverse('users:login'))
    return render(request, 'users/verify.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    services.send_new_password(request.user.email, new_password)
    # request.user.set_password(new_password)
    print(new_password)
    # request.user.save()
    return redirect(reverse('users:login'))
