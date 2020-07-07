from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'post_list.html', {
        'post_list': qs})

#
# def post_detail(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         raise Http404
#     return render(request, 'post_detail.html',
#                   {'post': post})

'''
class DetailView:
    def __init__(self, model):
        self.model = model

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        queryset = self.get_queryset()
        if pk is not None:
            queryset = queryset.filter(pk=pk)
            obj = queryset.get()
        return obj

    def get_queryset(self, *args, **kwargs):
        return self.model._default_.manager.all()

    def get_template_name(self):
        return '{}/{}_detail.html'.format(
            self.model._meta.app_label,
            self.model._meta.model_name)

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object(*args, **kwargs)
        return render(request, self.get_template_name(), {
            object._meta.model_name: object,
            })

    @classmethod
    def as_view(cls, model, pk_url_kwarg):
        def view(request, *args, **kwargs):
            self = cls(model)
            return self.dispatch(request, *args, **kwargs)
        return view


post_detail = DetailView.as_view(Post, pk_url_kwarg='id')
'''


class PostDetailView(DetailView):
    model = Post


post_detail = PostDetailView.as_view()
