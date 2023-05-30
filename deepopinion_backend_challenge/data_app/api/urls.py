from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import EXCELUploadView, CSVUploadView,CSVEXCELViewSet


app_name = "data_app"


router = SimpleRouter()
router.register(r'data', CSVEXCELViewSet)

urlpatterns = router.urls
urlpatterns = [
    path('upload-excel/', EXCELUploadView.as_view()),
    path('upload-csv/', CSVUploadView.as_view()),

 ]
urlpatterns += router.urls


 
