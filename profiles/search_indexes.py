import datetime
from haystack import indexes
from profiles.models import Snippet, Project


class SnippetIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user')
    content = indexes.CharField(model_attr='content')

    def get_model(self):
        return Snippet

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(updated_at__lte=datetime.datetime.now())



class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	user = indexes.CharField(model_attr='user')
	description = indexes.CharField(model_attr='description')

	def get_model(self):
		return Project
