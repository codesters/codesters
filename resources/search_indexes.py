import datetime
from haystack import indexes
from resources.models import Resource

class ResourceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created_by = indexes.CharField(model_attr='created_by')
    help_text = indexes.CharField(model_attr='help_text')

    def get_model(self):
        return Resource

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(show=True).filter(updated_at__lte=datetime.datetime.now())
