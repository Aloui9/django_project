from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name='blog' #define application namespace
#domain.com/blog/...
urlpatterns=[

path('',views.post_list, name='list'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
path('<int:post_id>/comment/',views.post_comment, name='post_comment')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)