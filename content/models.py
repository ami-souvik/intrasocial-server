from django.conf import settings
from django.utils import timezone
from django.db.models.query import QuerySet
from django.db.models import Model, ForeignKey, CharField, DateTimeField, TextField, CASCADE

class ContentQuerySet(QuerySet):
    """Personalized queryset created to improve model usability"""
    pass

class Content(Model):
    """Content model contains user posted content"""
    owner = ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        related_name="contents",
        on_delete=CASCADE,
    )
    title = CharField(max_length=255, null=False)
    body = TextField(null=False)

    created_at = DateTimeField()
    updated_at = DateTimeField()

    objects = ContentQuerySet.as_manager()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def to_dict(self):
        return dict(
            id=self.id,
            owner=self.owner.id,
            title=self.title,
            body=self.body
        )
