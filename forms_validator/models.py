from djongo import models
import uuid


class TemplateFormItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, db_index=True)
    value_choices = [
        ('text', 'text'),
        ('email', 'email'),
        ('phone', 'phone'),
        ('date', 'date')]
    value = models.CharField(
        max_length=5,
        choices=value_choices,
        default=('text', 'text'),
    )
    objects = models.DjongoManager()

    def __str__(self):
        return f'menu item {self.name} {self.value}'

    def __repr__(self):
        return f'menu item {self.name} {self.value}'


class TemplateForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, db_index=True, unique=True)
    items = models.ManyToManyField(TemplateFormItem, blank=True)
    objects = models.DjongoManager()

    def __str__(self):
        return f'TemplateForm {self.title}'
