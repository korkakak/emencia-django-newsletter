from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import get_model

from emencia.django.newsletter.models import Contact
from emencia.django.newsletter.utils import export_csv


@staff_member_required
def generate_csv(request, model=Contact, data=None):
    """
    Wrap all users in emencia.django.newsletter.Contact and send them to export_csv

    This should export all registered contacts to a csv.
    http://www.djangosnippets.org/snippets/1151/
    """
    if not data:
        data = model._default_manager.filter(subscriber=True)

    if len(data) == 0:
        data = [["no subscriptions"],]
    return export_csv.ExcelResponse(data)
