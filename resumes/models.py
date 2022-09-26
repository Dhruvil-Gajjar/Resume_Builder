import uuid
from django.db import models
from core.models import Base, User


class Skills(Base):
    skill_id = models.CharField(
        primary_key=True,
        max_length=36,
        default=uuid.uuid4
    )
    profile = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_skills',
        db_column='profile_id',
        null=True,
        blank=True
    )
    skill_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    class Meta:
        managed = False
        db_table = 'skills'
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.skill_name or self.skill_id
