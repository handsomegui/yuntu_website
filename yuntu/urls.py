from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', views.index, name='index'),
    url('^index.html', views.index, name='index'),
    url('^why_choose_yuntu/', views.why_choose_yuntu, name='why_choose_yuntu'),
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT)
