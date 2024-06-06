"""
URL configuration for dairy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views as v1
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from myapp.forms import LoginForm, PasswordChangeForm, MyPasswordResetForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',v1.home),
    path('about/',v1.about,name='about'),
    path('contact/',v1.contact,name='contact'),
    path('category/<slug:val>', v1.CategoryView.as_view(),name='category'),
    path('category-title/<val>', v1.CategoryTitle.as_view(),name='category-title'),
    path('product-detail/<int:pk>', v1.ProductDetail.as_view(),name='product-detail'),
    path('profile/', v1.ProfileView.as_view(), name='profile'),
    path('address/', v1.address, name='address'),
    path('updateAddress/<int:pk>', v1.updateAddress.as_view(),name='updateAddress'),
    path('add-to-cart/', v1.add_to_cart, name='add-to-cart'),
    path('cart/', v1.show_cart, name='showcart'),
    path('checkout/', v1.checkout.as_view(), name='checkout'),

    path('pluscart/', v1.plus_cart),
    path('minuscart/', v1.minus_cart),
    path('removecart/', v1.remove_cart),

    path('registration/', v1.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='myapp/login.html', authentication_form=LoginForm) , name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='myapp/password_reset.html', form_class=MyPasswordResetForm) , name='password_reset'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='myapp/changepassword.html', form_class=PasswordChangeForm, success_url='/passwordchangedone') , name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='myapp/passwordchangedone.html') , name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login') , name='logout'),
    # path('password-reset/, auth_view.PasswordResetView.as_view(template_name='myapp/password_reset.html', form_class=MyPasswordResetForm), name="password_reset'),
    # path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html') name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/ password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    # path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/ password_reset_complete.html'), name='password_reset_complete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
