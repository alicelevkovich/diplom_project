from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate, login, logout


from scientific_blog.models import User, Post
from scientific_blog.forms import CreateUser, LogInUser, CommentForm, UserProfile, CreatePost, ContactInfoForm


class HomeView(View):
    def get(self, request):
        users_list = User.objects.all()
        context = {'users': users_list}
        return render(request, 'start_page.html', context=context)


class CreateUserView(View):

    def get(self, request):
        context = {
            'form': CreateUser(),
        }
        return render(request, 'create_user.html', context=context)

    def post(self, request):
        auth_user = AuthUser.objects.create(password=request.POST.get('password'),
                                            username=request.POST.get('user_name'),
                                            email=request.POST.get('email'))
        user = User.objects.create(
            user_name=request.POST.get('user_name'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            auth_user_id=auth_user.id,
            lab_id=request.POST.get('lab')
        )
        return render(request, 'user_profile.html')


class LogInUserView(View):

    def __default_context(self):
        return {
            'form': LogInUser(),
        }

    def get(self, request):
        return render(request, 'LogIn.html', context=self.__default_context())

    def post(self, request):
        auth_user = authenticate(username=request.POST.get('user_name'),
                                 password=request.POST.get('password'))
        context = self.__default_context()
        if auth_user is not None:
            login(request, auth_user)
            user_obj = User.objects.get(auth_user_id=auth_user.id)
            user_post = Post.objects.filter(user_id=user_obj.id)

            context['user'] = user_obj
            context['user_post'] = user_post
            context['form'] = UserProfile(initial={'name': user_obj.name,
                                         'last_name': user_obj.last_name,
                                         'email': user_obj.email,
                                         'bio': user_obj.bio,
                                         'password': user_obj.password,
                                         'lab': user_obj.lab,
                                         'position': user_obj.position})
            return render(request, 'user_profile.html', context=context)
        else:
            # context['wrong_credentials_text'] = f'Wong username or password'
            return render(request, 'LogIn.html', context=self.__default_context())


def logout_view(request):
    context = {
        'form': LogInUser(),
    }
    logout(request)
    return render(request, 'LogIn.html', context=context)


class CreatePostView(View):

    def get(self, request):
        context = {
            'form': CreatePost(),
        }
        return render(request, 'user_profile.html', context=context)

    def post(self, request):
        user = User.objects.get(auth_user_id=request.user.id)
        post = Post.objects.create(
            content=request.POST.get('content'),
            user_id=user.id
        )
        return render(request, 'user_profile.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'home_page.html'
    paginate_by = 3


def post_detail(request, slug):
    template_name = 'post_page.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = User.objects.get(auth_user_id=request.user.id)
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
         'post': post,
         'comments': comments,
         'new_comment': new_comment,
         'comment_form': comment_form
        })


class UserProfileView(View):

    def get(self, request):
        user_obj = User.objects.get(auth_user_id=request.user.id)
        user_post = Post.objects.filter(user_id=user_obj.id)
        context = {
            'form': UserProfile(initial={'name': user_obj.name,
                                         'last_name': user_obj.last_name,
                                         'email': user_obj.email,
                                         'bio': user_obj.bio,
                                         'password': user_obj.password,
                                         'lab': user_obj.lab,
                                         'position': user_obj.position}),
            'user': user_obj,
            'user_post': user_post,
        }
        return render(request, 'user_profile.html', context=context)

    def post(self, request):
        user = User.objects.get(auth_user_id=request.user.id)
        form = UserProfile(request.POST, request.FILES)
        if form.is_valid():
            user.name = form.cleaned_data.get("name")
            user.avatar = form.cleaned_data.get("avatar")
            user.last_name = form.cleaned_data.get("last_name")
            user.email = form.cleaned_data.get("email")
            user.bio = form.cleaned_data.get("bio")
            user.password = form.cleaned_data.get("password")
            user.lab = form.cleaned_data.get("lab")
            user.position = form.cleaned_data.get("position")

            user.save()

            return render(request, 'user_profile.html', context={'form': form, 'user': User.objects.get(id=user.id)})
        else:
            return render(request, 'LogIn.html')


class ContactView(View):
    def get(self, request):
        context = {
            'form': ContactInfoForm(),
        }
        return render(request, 'contact_info.html', context=context)


