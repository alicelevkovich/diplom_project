from django.urls import path
from django.contrib.auth.decorators import login_required
from scientific_blog.views import CreateUserView, HomeView, LogInUserView, PostList,\
    post_detail, UserProfileView, logout_view, ContactView, CreatePostView


urlpatterns = [
    path('add/', CreateUserView.as_view(), name='user'),
    path('login/', LogInUserView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='start_page'),
    path('home_page/', login_required(PostList.as_view()), name='home_page'),
    path('profile/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', logout_view, name='logout'),
    path('contact_info/', ContactView.as_view(), name='contact_info'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    # path('upload/', image_upload_view, name='acc_image'),
    path('<slug:slug>/', post_detail, name='post'),



]
