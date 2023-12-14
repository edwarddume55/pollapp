from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
 
app_name = 'polls'
urlpatterns = [
    path('', views.index, name ='index'),
    path('<int:question_id>/', views.detail, name ='detail'),
    # path('<int:question_id>/results/', views.results, name ='results'),
    path('results/', views.results, name='results'),  # Updated URL pattern
    path('<int:question_id>/vote/', views.vote, name ='vote'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
