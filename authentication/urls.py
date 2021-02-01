from django.urls import path
from .views import RegisterView, LoginView, ProfileView, MembersView, MemberView


urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('me', ProfileView.as_view(), name="profile"),
    path('members', MembersView.as_view(), name="members"),
    path('members/<int:pk>', MemberView.as_view(), name="member-details")
]
