from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.views.generic.edit import FormView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mysite.views import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import reverse

from django.db.models import Q

from django.http import HttpResponseRedirect
#from .forms import UploadFileForm
from blog01.models import Post

# Create your views here.

#--- ListView
class PostLV(ListView) :
    model = Post
    template_name = 'blog01/post_all.html'
    context_object_name = 'posts'
    paginate_by = 8


#--- DetailView
class PostDV(DetailView) :
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('blog01:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)

#def upload_file(request):
#    if request.method == 'POST':
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.instance.owner = request.user
#            form.save()
#            return HttpResponseRedirect(reverse('blog:index'))
#    else:
#        form = UploadFileForm()
#    return render(request, 'blog/post_form.html', {'form': form})


class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog01/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostUpdateView(LoginRequiredMixin, UpdateView) :
    model = Post
    fields = ['title','content']
    success_url = reverse_lazy('blog01:index')

class PostDeleteView(LoginRequiredMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('blog01:index')


