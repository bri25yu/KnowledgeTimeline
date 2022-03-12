from django.urls import path

import graph.views as views


app_name = "graph"
urlpatterns = [
    path("", views.index, name="index"),
]
