from django import forms


class SuggestWidget(forms.SelectMultiple):
    template_name = 'app/widgets/suggest.html'

    class Media:
        js = ['app/js/suggest.js']
        css = {
            'all': ['app/css/suggest.css']
        }

    def __init__(self, form_instance, attrs=None):
        super().__init__(attrs)
        self.form_instance = form_instance
        if 'class' in self.attrs:
            self.attrs['class'] += ' suggest'
        else:
            self.attrs['class'] = 'suggest'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['form_instance'] = self.form_instance
        return context