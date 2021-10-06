from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="index-page"),
    path("posts",views.posts, name="post-page"),
    path("posts/<slug:slug>",views.post_details, name="post-details-page")

]
