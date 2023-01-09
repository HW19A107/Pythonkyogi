from django.contrib import admin
from django.urls import path, include

from kyogi.views import (
    frontpage,
    home,
    sentakupage,
    expage,
    Q1page,
    Q2page,
    Q3page,
    Q4page,
    Q5page,
    lastpage,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",frontpage),
    path('',include('kyogi.urls')),
    path("home",home),
    path("sentaku",sentakupage),
    path("ex",expage),
    path("Q1",Q1page),
    path("Q1",Q1page),
    path("Q2",Q2page),
    path("Q3",Q3page),
    path("Q4",Q4page),
    path("Q5",Q5page),
    path("last",lastpage),
]
