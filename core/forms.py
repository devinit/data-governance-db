from django import forms
# from .models import (
#      Project
# )


# class ProjectAddForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = [
#             'id',
#             'hub',
#             'company',
#             'status',
#             'bid_chance',
#             'project_type',
#             'title',
#             'description',
#             'countries',
#             'client',
#             'lead',
#             'manager',
#             'start_date',
#             'end_date'
#         ]
#         widgets = {
#             'title': forms.Textarea(
#                 attrs={'rows': 3, 'required': True}
#             ),
#             'description': forms.Textarea(
#                 attrs={'rows': 3, 'required': False}
#             ),
#             'start_date': forms.DateInput(
#                 attrs={'type': 'date', 'class': 'form-control', 'required': False}
#             ),
#             'end_date': forms.DateInput(
#                 attrs={'type': 'date', 'class': 'form-control', 'required': False}
#             ),
#         }

#     def __init__(self, *args, **kwargs):
#         super(ProjectAddForm, self).__init__(*args, **kwargs)

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

#         self.fields['id'].initial = 'P{}'.format(next_project_number_str)
#         self.fields['countries'].required = False
#         self.fields['lead'].queryset = Employee.objects.filter(active=True)
#         self.fields['manager'].queryset = Employee.objects.filter(active=True)


# class ProjectEditForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = [
#             'id',
#             'hub',
#             'company',
#             'status',
#             'bid_chance',
#             'project_type',
#             'title',
#             'description',
#             'countries',
#             'client',
#             'lead',
#             'manager',
#             'start_date',
#             'end_date'
#         ]
#         widgets = {
#             'id': forms.HiddenInput(),
#             'title': forms.Textarea(
#                 attrs={'rows': 3, 'required': True}
#             ),
#             'description': forms.Textarea(
#                 attrs={'rows': 3, 'required': False}
#             ),
#             'start_date': forms.DateInput(
#                 attrs={'type': 'date', 'class': 'form-control', 'required': False}
#             ),
#             'end_date': forms.DateInput(
#                 attrs={'type': 'date', 'class': 'form-control', 'required': False}
#             ),
#         }

#     def __init__(self, *args, **kwargs):
#         super(ProjectEditForm, self).__init__(*args, **kwargs)

#         self.fields['countries'].required = False
#         self.fields['lead'].queryset = Employee.objects.filter(active=True)
#         self.fields['manager'].queryset = Employee.objects.filter(active=True)