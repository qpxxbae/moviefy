from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name ='home_page'),
    path('movies/top/',views.top_movies_page,name = 'top_movies_page'),
    path('movies/all',views.all_movies_page, name ="all_movies_page"),
    path('movie/detail/<int:pk>/',views.movie_detail_page,name ="movie_detail_page"),
    path('movies/category/<slug:slug>/',views.movies_by_category_page,name = "movies_by_category_page"),
    path('movies/search/',views.movies_by_search_page,name = "movies_by_search_page"),

    path('sign-up/',views.sign_up_page,name = 'sign_up_page'),
    path('login/',views.login_page,name = 'login_page'),
    path('logout/',views.logout_action,name='logout_action'),
    

]