from django.views.generic.detail import SingleObjectMixin
from .models import Contact


class ContactDetailMixin(SingleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context