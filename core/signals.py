from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from .models import (
    Document,
    Institution,
    InstitutionType,
    Category,
    DocumentType
)
from .get_request_middleware import current_request


@receiver(post_save, sender=Document)
@receiver(post_save, sender=Institution)
@receiver(post_save, sender=InstitutionType)
@receiver(post_save, sender=Category)
@receiver(post_save, sender=DocumentType)
def log_everything_addition_change(sender, instance, created, **kwargs):
    if created:
        action = ADDITION
    else:
        action = CHANGE

    obj_id = None
    if hasattr(instance, "id"):
        obj_id = instance.id

    user_id = None
    if current_request() is not None:
        current_user = current_request().user
        if current_user:
            user_id = current_user.id

    if obj_id is not None and user_id is not None:
        LogEntry.objects.log_action(
            user_id=user_id,
            content_type_id=ContentType.objects.get_for_model(sender).pk,
            object_repr=str(instance),
            object_id=obj_id,
            action_flag=action
        )


@receiver(pre_delete, sender=Document)
@receiver(pre_delete, sender=Institution)
@receiver(pre_delete, sender=InstitutionType)
@receiver(pre_delete, sender=Category)
@receiver(pre_delete, sender=DocumentType)
def log_everything_deletion(sender, instance, **kwargs):
    obj_id = None
    if hasattr(instance, "id"):
        obj_id = instance.id

    user_id = None
    if current_request() is not None:
        current_user = current_request().user
        if current_user:
            user_id = current_user.id

    if obj_id is not None and user_id is not None:
        LogEntry.objects.log_action(
            user_id=user_id,
            content_type_id=ContentType.objects.get_for_model(sender).pk,
            object_repr=str(instance),
            object_id=obj_id,
            action_flag=DELETION
        )
