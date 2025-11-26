from django.urls import path

from users.views.branch import ListCreateBranchView
from users.views.customer import (
    ListCreateCustomerView,
    RetrieveUpdateDeleteCustomerView,
)
from users.views.user import ListCreateUserView, RetrieveUpdateDeleteUserView


urlpatterns = [
    path("branches/", ListCreateBranchView.as_view(), name="branches"),
    path("customers/", ListCreateCustomerView.as_view(), name="customers"),
    path(
        "customers/<int:customer_id>/",
        RetrieveUpdateDeleteCustomerView.as_view(),
        name="retrieve-update-delete",
    ),
    path("users/", ListCreateUserView.as_view(), name="users"),
    path(
        "users/<int:user_id>/",
        RetrieveUpdateDeleteUserView.as_view(),
        name="retrieve-update-delete",
    ),
]
