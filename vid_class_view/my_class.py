'''
Leveraging a class-based view can help scale
production since the views needed for implementation
can be reused by instantiating a class.

Django has built-in views which are classes: 

django.views.generic.list.ListView
django.views.generic.list.DetailView

these built-in classes hide what is going
on onder the hood so the following is
created to create our own 'ListView' and/or
'DetailView' to understand what is going
on under the hood.
'''
import django
import django.shortcuts
from models import Poll
class ListView():
    def get(self, request):
        model_list_name = self.model.__name.lower() + '_list'
        context = {model_list_name: self.model.objects.all()}
        return django.shortcuts.render(request, self.template_name, context)

class PollListView(ListView):
    model = Poll
    template_name = 'polling/list.html'




