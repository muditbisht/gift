from django import forms


def non_empty(data):
	if len(data) == 0:
		raise forms.ValidationError("Enter username")


class RegisterForm(forms.Form):
	first_name = forms.CharField(validators=(non_empty,))
	last_name = forms.CharField(validators=(non_empty,))
	email = forms.EmailField()
	pwd = forms.CharField()


class LoginForm(forms.Form):
	email = forms.CharField()
	pwd = forms.CharField()
