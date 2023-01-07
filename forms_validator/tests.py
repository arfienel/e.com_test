from django.test import TestCase
from .models import TemplateForm, TemplateFormItem


class GetFormTests(TestCase):

    def setUp(self):
        user_name = TemplateFormItem.objects.create(name='user_name', value='text')
        user_email = TemplateFormItem.objects.create(name='user_email', value='email')
        user_phone = TemplateFormItem.objects.create(name='user_phone', value='phone')
        user_date = TemplateFormItem.objects.create(name='user_date', value='date')
        user_form = TemplateForm.objects.create(title='user registration form')
        user_name.save()
        user_email.save()
        user_phone.save()
        user_date.save()
        user_form.save()
        user_form.items.add(user_name, user_email, user_phone, user_date)

    def test_get_form_success(self):
        data = 'user_email=makek@gmail.com&user_name=kekw&user_phone=+7 950 123 45 67&user_date=2003.12.23'
        response = self.client.post('/get_form/', data, content_type='utf-8')
        self.assertEqual(response.content.decode('UTF-8'), 'user registration form')

    def test_get_form_fail(self):
        data = 'user_email=makek@gmail.com&user_name=kekw&user_phone=+7 950 123 45 67'
        response = self.client.post('/get_form/', data, content_type='utf-8')
        self.assertEqual(response.content.decode('UTF-8'), '{"user_email": "email", "user_name": "text", "user_phone": "phone"}')