from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("settings", views.blind_test_settings, name="blindtest_settings"),
    path("<int:question_id>/question/<int:pk>", views.blind_test_general_view, name="question" )
]