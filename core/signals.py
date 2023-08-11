from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
# from .models import (
#     Project,
#     Client
# )
from .get_request_middleware import current_request

# @receiver(pre_save, sender=Project)
# def autofill_project_id(sender, instance, **kwargs):
#     if instance.id is None:
#         max_project_number = 0
#         siblings = Project.objects.all()
#         for sibling in siblings:
#             try:
#                 sibling_number = int(sibling.id[1:])
#                 if sibling_number > max_project_number:
#                     max_project_number = sibling_number
#             except ValueError:
#                 pass
#         next_project_number = max_project_number + 1
#         if next_project_number < 10000:
#             next_project_number_str = str(next_project_number).zfill(4)
#         else:
#             next_project_number_str = str(next_project_number)
#         instance.id = 'P{}'.format(next_project_number_str)


# @receiver(post_save, sender=Client)
# def log_everything_addition_change(sender, instance, created, **kwargs):
#     if created:
#         action = ADDITION
#     else:
#         action = CHANGE

#     obj_id = None
#     if hasattr(instance, "id"):
#         obj_id = instance.id
#     elif hasattr(instance, "code"):
#         obj_id = instance.code

#     user_id = None
#     if current_request() is not None:
#         current_user = current_request().user
#         if current_user:
#             user_id = current_user.id

#     if obj_id is not None and user_id is not None:
#         LogEntry.objects.log_action(
#             user_id=user_id,
#             content_type_id=ContentType.objects.get_for_model(sender).pk,
#             object_repr=str(instance),
#             object_id=obj_id,
#             action_flag=action
#         )


# @receiver(pre_delete, sender=Client)
# def log_everything_deletion(sender, instance, **kwargs):
#     obj_id = None
#     if hasattr(instance, "id"):
#         obj_id = instance.id
#     elif hasattr(instance, "code"):
#         obj_id = instance.code

#     user_id = None
#     if current_request() is not None:
#         current_user = current_request().user
#         if current_user:
#             user_id = current_user.id

#     if obj_id is not None and user_id is not None:
#         LogEntry.objects.log_action(
#             user_id=user_id,
#             content_type_id=ContentType.objects.get_for_model(sender).pk,
#             object_repr=str(instance),
#             object_id=obj_id,
#             action_flag=DELETION
#         )
