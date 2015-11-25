import json

from django import forms
from django.test.utils import override_settings
from django_webtest import WebTest
from . import build_test_urls


class SelectmultipleForm(forms.Form):
    test_field = forms.MultipleChoiceField(
        choices=(('V', 'Visa'), ('M', 'MasterCard'), ('P', 'Paypal')),
        widget=forms.SelectMultiple(attrs={'data-test': 'Test Attr'}))
    data_field = forms.BooleanField(required=False, widget=forms.HiddenInput, initial=True,
                                    help_text='To produce non empty POST for empty test_field')


@override_settings(ROOT_URLCONF=__name__)
class Test(WebTest):
    default_form = SelectmultipleForm

    def test_default_usecase(self):
        page = self.app.get(self.test_default_usecase.url)

        self.assertIn('id="id_test_field_container"', page.body.decode('utf-8'))
        self.assertIn('id="id_test_field"', page.body.decode('utf-8'))
        self.assertIn('data-test="Test Attr"', page.body.decode('utf-8'))

        form = page.form
        self.assertIn('test_field', form.fields)

        form['test_field'] = ['V', 'P']
        response = json.loads(form.submit().body.decode('utf-8'))

        self.assertIn('cleaned_data', response)
        self.assertIn('test_field', response['cleaned_data'])
        self.assertEquals(['V', 'P'], response['cleaned_data']['test_field'])

    def test_missing_value_error(self):
        form = self.app.get(self.test_missing_value_error.url).form
        response = form.submit()

        self.assertIn('has-error', response.body.decode('utf-8'))
        self.assertIn('This field is required.', response.body.decode('utf-8'))

    def test_part_group_class(self):
        page = self.app.get(self.test_part_group_class.url)

        self.assertIn('class="selectmultiple-field col s12 yellow"', page.body.decode('utf-8'))

    test_part_group_class.template = '''
        {% form %}
             {% part form.test_field group_class %}selectmultiple-field col s12 yellow{% endpart %}
        {% endform %}
    '''

    def test_part_add_group_class(self):
        page = self.app.get(self.test_part_add_group_class.url)

        self.assertIn('class="select-field col s12 required orange"', page.body.decode('utf-8'))

    test_part_add_group_class.template = '''
        {% form %}
             {% part form.test_field add_group_class %}orange{% endpart %}
        {% endform %}
    '''

    def test_part_prefix(self):
        response = self.app.get(self.test_part_prefix.url)
        self.assertIn('<i class="mdi-communication-email prefix"></i>', response.body.decode('utf-8'))

    test_part_prefix.template = '''
        {% form %}
             {% part form.test_field prefix %}<i class="mdi-communication-email prefix"></i>{% endpart %}
        {% endform %}
    '''

    def test_part_add_control_class(self):
        response = self.app.get(self.test_part_add_control_class.url)
        self.assertIn('class="orange"', response.body.decode('utf-8'))

    test_part_add_control_class.template = '''
        {% form %}
             {% part form.test_field add_control_class %}orange{% endpart %}
        {% endform %}
    '''

    def test_part_label(self):
        response = self.app.get(self.test_part_label.url)
        self.assertIn('<label for="id_test_field">My label</label>', response.body.decode('utf-8'))

    test_part_label.template = '''
        {% form %}
             {% part form.test_field label %}<label for="id_test_field">My label</label>{% endpart %}
        {% endform %}
    '''

    def test_part_add_label_class(self):
        response = self.app.get(self.test_part_add_label_class.url)
        self.assertIn('<label for="id_test_field" class="green-text">Test field</label>', response.body.decode('utf-8'))

    test_part_add_label_class.template = '''
        {% form %}
             {% part form.test_field add_label_class %}green-text{% endpart %}
        {% endform %}
    '''

    def test_part_help_text(self):
        response = self.app.get(self.test_part_help_text.url)
        self.assertIn('<small class="help-block">My help</small>', response.body.decode('utf-8'))

    test_part_help_text.template = '''
        {% form %}
             {% part form.test_field help_text %}<small class="help-block">My help</small>{% endpart %}
        {% endform %}
    '''

    def test_part_errors(self):
        response = self.app.get(self.test_part_errors.url)
        self.assertIn('<div class="errors"><small class="error">My Error</small></div>', response.body.decode('utf-8'))

    test_part_errors.template = '''
        {% form %}
             {% part form.test_field  errors%}<div class="errors"><small class="error">My Error</small></div>{% endpart %}
        {% endform %}
    '''

urlpatterns = build_test_urls(Test)