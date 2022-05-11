from django.forms import ModelForm

from .models import SearchCriteria


class SearchCriteriaForm(ModelForm):
    class Meta:
        model = SearchCriteria
        fields = '__all__'
