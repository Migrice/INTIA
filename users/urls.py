from django.urls import path

from users.views.branch import ListCreateBranchView


urlpatterns = [
    path("/branches", ListCreateBranchView.as_view(), name="index"),
    
]
