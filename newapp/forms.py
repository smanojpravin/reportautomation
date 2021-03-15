from .models import *
from django import forms
from django.forms import ModelChoiceField
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ChartSelectionForm(forms.ModelForm):
    ReportYear = forms.ModelChoiceField(queryset=activeusers.objects.values_list('ReportYear',flat=True).distinct().order_by('ReportYear'))
    org = forms.ModelChoiceField(queryset=organization.objects.values_list('org',flat=True).distinct())
    # org = forms.ModelChoiceField(queryset=activeusers.objects.values_list('OrganizationName',flat=True).distinct())
    ReportWeek = forms.ModelChoiceField(queryset=activeusers.objects.none())

    class Meta:
        model = activeusers
        fields = ('ReportYear','ReportWeek','org') 

            
#form for chart data deletion
class ChartDeletionForm(forms.ModelForm):
    ReportYear = forms.ModelChoiceField(queryset=activeusers.objects.values_list('ReportYear',flat=True).distinct().order_by('ReportYear'))
    ReportWeek = forms.ModelChoiceField(queryset=activeusers.objects.none())
    class Meta:
        model = activeusers
        fields = ('ReportYear','ReportWeek') 

        
#form for file upload
class fileform(forms.ModelForm):
    Before = forms.FileField(widget=forms.FileInput(attrs={'accept': ".csv"}))
    From = forms.FileField(widget=forms.FileInput(attrs={'accept': ".csv"}))
    AuditReport = forms.FileField(widget=forms.FileInput(attrs={'accept': ".csv"}))
    ReportYear = forms.ModelChoiceField(queryset=activeusers.objects.none(),to_field_name="name")
    ReportWeek = forms.ModelChoiceField(queryset=activeusers.objects.none())
  
    class Meta:
        model= activeusers
        fields={'Before','From','AuditReport','ReportYear','ReportWeek'}



