from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib import auth

class LoginForm(forms.Form):
    username = forms.CharField(label="帳號", max_length=25, required=True)
    password = forms.CharField(label="密碼", widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        _user = auth.authenticate(username=username, password=password)

        if _user is None or not _user.is_active:
           raise forms.ValidationError("請確認使用者名稱與密碼是否正確，或是您帳號尚未啟用")
        
        self.user = _user
        return self.cleaned_data
