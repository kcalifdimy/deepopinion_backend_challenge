from django.urls import include, path

urlpatterns = [
    path('datas/', include('deepopinion_backend_challenge.data_app.api.urls', namespace="data_app")),
]