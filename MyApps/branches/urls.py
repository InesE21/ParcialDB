from django.urls import path
from MyApps.branches.views import BranchList, BranchDetail


urlpatterns = [
    path('', BranchList.as_view()),
    path('<int:pk>', BranchDetail.as_view()),
]