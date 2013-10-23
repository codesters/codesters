import datetime
from haystack import indexes
from .models import Project


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
            return Project
