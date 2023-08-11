from django.urls import path, include
from .views import (
    register,
    RegisterDone,
    register_complete
)

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", register, name="register"),
    path("accounts/register/done/", RegisterDone.as_view(), name="register_done"),
    path('accounts/register/<uidb64>/<token>', register_complete, name='register_complete'),
]