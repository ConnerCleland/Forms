# forms.py
from django import forms
from .models import (
    FrontTimesChallenge,
    NoTeenSumChallenge,
    CenteredAverageChallenge,
    XYZThereChallenge,
)


class FrontTimesForm(forms.ModelForm):
    class Meta:
        model = FrontTimesChallenge
        fields = ["input_string", "n"]


class NoTeenSumForm(forms.ModelForm):
    class Meta:
        model = NoTeenSumChallenge
        fields = ["a", "b", "c"]


class XYZThereForm(forms.ModelForm):
    class Meta:
        model = XYZThereChallenge
        fields = ["input_string"]


class CenteredAverageForm(forms.ModelForm):
    class Meta:
        model = CenteredAverageChallenge
        fields = ["nums"]
