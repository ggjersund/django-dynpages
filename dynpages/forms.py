from django import forms
from django.conf import settings
from . models import DynPage


class DynpageForm(forms.ModelForm):
    url = forms.RegexField(
        label='URL',
        max_length=100,
        regex=r'^[-\w/\.~]+$',
        help_text="Example: '/about/contact/'. Make sure to have leading and trailing slashes.",
        error_messages={
            "invalid":
                "This value must contain only letters, numbers, dots, "
                "underscores, dashes, slashes or tildes."
            ,
        },
    )

    class Meta:
        model = DynPage
        fields = '__all__'

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url.startswith('/'):
            raise forms.ValidationError(
                "URL is missing a leading slash.",
                code='missing_leading_slash',
            )
        if (settings.APPEND_SLASH and
                'django.middleware.common.CommonMiddleware' in settings.MIDDLEWARE and
                not url.endswith('/')):
            raise forms.ValidationError(
                "URL is missing a trailing slash.",
                code='missing_trailing_slash',
            )
        return url

    def clean(self):
        url = self.cleaned_data.get('url')
        language = self.cleaned_data.get('language')

        same_url = DynPage.objects.filter(url=url)
        if self.instance.pk:
            same_url = same_url.exclude(pk=self.instance.pk)

        if same_url.filter(language=language).exists():
            raise forms.ValidationError(
                "Dynamic page with the given URL already exist for the given language",
                code='duplicate_url',
            )

        return super().clean()
