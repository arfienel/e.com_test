from django.shortcuts import HttpResponse
from .models import TemplateForm, TemplateFormItem
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
import datetime
from djongo.models import DjongoManager
from json import dumps


def email_validator(email_string: str):
    try:
        validate_email(email_string)
    except ValidationError:
        return False
    else:
        return True


def phone_validator(phone_string: str):
    validate_phone_number_pattern = "^(\+?[\d]{1} [\d]{3} [\d]{3} [\d]{2} [\d]{2})$"
    if re.match(validate_phone_number_pattern, phone_string):
        return True
    else:
        return False


def date_validator(date_string: str):
    try:
        datetime.datetime.strptime(date_string, '%Y.%m.%d')
    except ValueError:
        try:
            datetime.datetime.strptime(date_string, '%d.%m.%Y')
        except ValueError:
            return False
    else:
        return True


def get_form(request):
    """
     Возвращает имя наиболее подходящей данному списку полей формы,
     при отсутствии совпадений с известными формами производит
     типизацию полей и возвращает список полей с их типами.
    """
    if request.method == 'POST':
        request_form_fields_list = str(request.body.decode('UTF-8').replace("'", "")).split('&')
        request_form_fields_dict = {}
        for item in request_form_fields_list:
            name, value = item.split('=')
            request_form_fields_dict[name] = value

        # валидация всех полученных значений и поиск их в бд
        validated_form_fields_dict = {}
        db_form_fields_list = []
        for name, value in request_form_fields_dict.items():
            if email_validator(value):
                value = 'email'
                validated_form_fields_dict[name] = value
            elif phone_validator(value):
                value = 'phone'
                validated_form_fields_dict[name] = value
            elif date_validator(value):
                value = 'date'
                validated_form_fields_dict[name] = value
            else:
                value = 'text'
                validated_form_fields_dict[name] = value
            try:
                db_form_fields_list.append(TemplateFormItem.objects.get(name=name, value=value))
            except Exception:
                return HttpResponse(dumps(validated_form_fields_dict))
        db_form_fields_name_set = set(i.name for i in db_form_fields_list)

        for template_form in TemplateForm.objects.all():
            if db_form_fields_name_set == set(i.name for i in template_form.items.all()):
                return HttpResponse(template_form.title)
        return HttpResponse(dumps(validated_form_fields_dict))
    return HttpResponse('Doesn`t support get method')
