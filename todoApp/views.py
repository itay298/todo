from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views import generic
from .models import TodoNote
from django.urls import reverse_lazy
# Create your views here.

class UpdateView(generic.UpdateView):
    template_name = 'todoApp/update.html'
    model = TodoNote
    fields = ['title']
    
class IndexView(generic.CreateView):
    model = TodoNote
    template_name = 'todoApp/index.html'
    success_url = reverse_lazy('todo:index')
    fields = ['title']
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['title'].label = ''
        form.fields['title'].widget.attrs['placeholder'] = _('add notes here...')
        return form

    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

class DeleteView(generic.DeleteView):
    template_name = 'todoApp/delete.html'
    model = TodoNote
    success_url = reverse_lazy('todo:index')
    