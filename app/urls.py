from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='registration'),
    path('login/',views.login_user,name='login_user'),
    path('profile/',views.profile,name='profile'),
    path('coach/',views.all_coaches,name='coach')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)