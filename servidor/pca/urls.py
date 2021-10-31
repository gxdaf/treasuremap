"""pca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from treasuremap import views as tmv
from usuario import views as uv
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('treasuremap', include('treasuremap.urls')),
    path('perfil', uv.perfil, name = 'perfil'),
    path('', RedirectView.as_view(url='treasuremap'), name = 'treasuremap'),
    path('cadastro', uv.registrar, name='cadastro'),
    path('cadperfil', uv.dadosperfil, name='cadperfil'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    re_path(r'^%artigo/(?P<nome>.*)%$', tmv.artigo),
    re_path(r'(?P<nome>.*)$', tmv.redirecionador),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
