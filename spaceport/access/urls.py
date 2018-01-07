from django.conf.urls import url, include
from access import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api/1/node/(?P<node>\d+)/uuid/(?P<uuid>.+)$', views.AccessRequest.as_view()),
    url(r'api/1/admin/uuid/(?P<uuid>.+)$', views.ValidateAdmin.as_view()),
    url(r'api/1/admin/register/uuid/(?P<uuid>.+)$', views.RegisterTag.as_view()),
    url(r'api/', views.ApiCatchAll.as_view()),

]
