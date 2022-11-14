from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class AuthorListView(ListView):
    """"""


class AuthorDetailView(DetailView):
    """"""


class AuthorCreateView(LoginRequiredMixin,CreateView):
    """"""
    def form_valid(self, form):
        object = form.save(commit=False)
        object.author = self.request.user
        object.save()
        return super(AuthorCreateView, self).form_valid(form)


class AuthorUpateView(LoginRequiredMixin,UpdateView):
    """"""
    def get_queryset(self):
        qs = super(AuthorUpateView, self).get_queryset()
        return qs.filter(author=self.request.user)


class AuthorDeleteView(LoginRequiredMixin,DeleteView):
    """"""
    def get_queryset(self):
        qs = super(AuthorDeleteView, self).get_queryset()
        return qs.filter(author=self.request.user)
