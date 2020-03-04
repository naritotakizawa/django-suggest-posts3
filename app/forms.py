from django import forms
from django.urls import reverse_lazy
from .models import Post
from .widgets import SuggestWidget


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs = {'data-url': reverse_lazy('app:api_posts_get')}
        if self.instance.pk:
            attrs['data-instancepk'] = self.instance.pk
        self.fields['relation_posts'].widget = SuggestWidget(attrs=attrs)
