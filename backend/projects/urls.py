from django.urls import path
from .views import project_list, project_detail, project_vote

urlpatterns = [
    path('', project_list, name='project_list'),
    path('<int:project_id>/', project_detail, name='project_detail'),
    path('<int:project_id>/vote/', project_vote, name='project_vote'),
]
