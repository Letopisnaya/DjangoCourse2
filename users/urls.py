from django.urls import path
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import (
    UserCreateApiView,
    UserDestroyApiView,
    UserListApiView,
    UserRetrieveApiView,
    UserUpdateApiView, PaymentViewSet,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("payment", PaymentViewSet)

urlpatterns = [
    path("", UserListApiView.as_view(), name="users_list"),
    path("<int:pk>/", UserRetrieveApiView.as_view(), name="users_retrieve"),
    path("create/", UserCreateApiView.as_view(), name="users_create"),
    path(
        "<int:pk>/delete/",
        UserDestroyApiView.as_view(),
        name="users_delete",
    ),
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="users_update"),
]
urlpatterns += router.urls