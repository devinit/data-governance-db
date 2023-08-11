from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# def validate_begin_with_p(value):
#     if not str(value).startswith('P'):
#         raise ValidationError(
#             _('%(value)s does not begin with "P"'),
#             params={'value': value},
#         )


# class Project(models.Model):
#     def __str__(self):
#         return "{} - {}".format(self.id, self.title)
    
#     def get_absolute_url(self):
#         return reverse("core:project_detail", kwargs={"id": self.id})

#     id = models.CharField(
#         primary_key = True,
#         unique = True,
#         max_length = 999,
#         verbose_name = "ID",
#         validators=[validate_begin_with_p]
#     )
#     hub = models.ForeignKey(
#         'Hub',
#         blank = True,
#         null = True,
#         on_delete = models.SET_NULL,
#         related_name = "projects"
#     )
#     company = models.ForeignKey(
#         'Company',
#         blank = True,
#         null = True,
#         on_delete = models.SET_NULL,
#         related_name = "projects"
#     )
#     STATUS_PREPARATION = "P"
#     STATUS_SUBMITTED = "S"
#     STATUS_WON = "W"
#     STATUS_ACTIVE = "A"
#     STATUS_COMPLETE = "C"
#     STATUS_LOST = "L"
#     STATUS_CANCELLED = "N"
#     BID_STATUSES = [
#         STATUS_PREPARATION,
#         STATUS_SUBMITTED,
#         STATUS_WON,
#     ]
#     CURRENT_STATUSES = [STATUS_ACTIVE] + BID_STATUSES
#     STATUS_CHOICES = [
#         (STATUS_PREPARATION, "Bid Preparation"),
#         (STATUS_SUBMITTED, "Bid Submitted"),
#         (STATUS_WON, "Bid Won"),
#         (STATUS_LOST, "Bid Lost"),
#         (STATUS_ACTIVE, "Active"),
#         (STATUS_COMPLETE, "Complete"),
#         (STATUS_CANCELLED, "Cancelled"),
#     ]
#     status = models.CharField(
#         max_length = 1,
#         choices = STATUS_CHOICES,
#         default = STATUS_ACTIVE,
#         blank = True,
#         null = True
#     )
#     BID_LOW = "L"
#     BID_MEDIUM = "M"
#     BID_HIGH = "H"
#     BID_CHOICES = [
#         (BID_LOW, "Low"),
#         (BID_MEDIUM, "Medium"),
#         (BID_HIGH, "High"),
#     ]
#     bid_chance = models.CharField(
#         max_length = 1,
#         choices = BID_CHOICES,
#         default = BID_HIGH, # Optimism
#         blank = True,
#         null = True
#     )
#     TYPE_PROJECT = "P"
#     TYPE_OVERHEAD = "O"
#     TYPE_ABSENCE = "A"
#     TYPE_CHOICES = [
#         (TYPE_PROJECT, "Project"),
#         (TYPE_OVERHEAD, "Overhead"),
#         (TYPE_ABSENCE, "Absence")
#     ]
#     project_type = models.CharField(
#         max_length = 1,
#         choices = TYPE_CHOICES,
#         default = TYPE_PROJECT,
#         blank = True,
#         null = True
#     )
#     title = models.TextField(
#         blank = True,
#         null = True
#     )
#     description = models.TextField(
#         blank = True,
#         null = True
#     )
#     countries = models.ManyToManyField(
#         'Country',
#         related_name = "projects"
#     )
#     client = models.ForeignKey(
#         'Client',
#         blank = True,
#         null = True,
#         on_delete = models.SET_NULL,
#         related_name = "projects"
#     )
#     lead = models.ForeignKey(
#         'Employee',
#         blank = True,
#         null = True,
#         on_delete = models.SET_NULL,
#         related_name = "projects_led"
#     )
#     manager = models.ForeignKey(
#         'Employee',
#         blank = True,
#         null = True,
#         on_delete = models.SET_NULL,
#         related_name = "projects_managed"
#     )
#     start_date = models.DateField(
#         blank = True,
#         null = True
#     )
#     end_date = models.DateField(
#         blank = True,
#         null = True
#     )

#     def display_reports(self):
#         components = self.components.all()
#         resource_allocations = list()
#         for component in components:
#             component_resource_allocations = component.resource_allocations.all()
#             for component_resource_allocation in component_resource_allocations:
#                 resource_allocations.append(component_resource_allocation)
#         return len(resource_allocations) > 0

#     def get_bid_status_display(self):
#         status_display = self._get_FIELD_display(self._meta.get_field('status'))
#         if self.status not in self.BID_STATUSES:
#             return status_display
#         if self.bid_chance is None:
#             return status_display
#         return "{} ({})".format(status_display, self.get_bid_chance_display())
