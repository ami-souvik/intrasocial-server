from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import Model, ForeignKey, CharField, DateTimeField, CASCADE

vote_choices = (
    ("U", "Up"),
    ("D", "Down")
)

class Feedback(Model):
    """Feedback model contains user feedback contents or comments"""
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        related_name="feedbacks",
        on_delete=CASCADE,
    )
    content = ForeignKey(
        'content.Content',
        null=True,
        related_name="feedbacks",
        on_delete=CASCADE,
    )
    comment = ForeignKey(
        'comment.Comment',
        null=True,
        related_name="feedbacks",
        on_delete=CASCADE,
    )
    vote = CharField(
        max_length=1,
        choices=vote_choices
    )

    created_at = DateTimeField()
    updated_at = DateTimeField()

    def validate_unique(self, exclude=None):
        if not self.id and Feedback.objects.filter(user=self.user, content=self.content, comment=self.comment)\
            .exists():
            raise ValidationError("Feedback already exist")
        super(Feedback, self).validate_unique(exclude=exclude)

    def save(self, *args, **kwargs):
        self.validate_unique()
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def to_dict(self):
        _dict = dict(
            id=self.id,
            user=self.user.id,
            vote=self.vote
        )
        if self.content:
            _dict["content"] = self.content.id
        if self.comment:
            _dict["comment"] = self.comment.id
        return _dict
