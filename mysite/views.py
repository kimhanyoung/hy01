from django.views.generic.base import TemplateView
from django.views.generic import ListView

from accounts.forms import SignupForm
from django.views.generic.edit import CreateView

#from django.conf.urls import reverse_lazy
from django.urls import reverse_lazy             # 윗줄이 바뀐지몰라 구글 검색후 대체

from django.contrib.auth.decorators import login_required
from blog01.models import Post

# Create your views here.

#--- ListView
class HomeView(ListView) :
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 4

#class HomeView(TemplateView):       #위 listview로 대체
#    template_name = 'home.html'

# --- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_on.html'

# --- @login_required
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

