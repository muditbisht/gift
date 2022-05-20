from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

from django.views import View

# Create your views here.
from .forms import RegisterForm, LoginForm

class Auth(View):
	template_name = "auth.html"

	def get(self, request):
		if request.user.is_authenticated:
			return redirect('/')
		login_form = LoginForm(request.GET)
		register_form = RegisterForm(request.GET)
		print('LoginForm: ', login_form)
		print('RegisterForm: ', register_form)
		# if not login_form.is_valid():
		# 	return redirect('/auth/')
		# context = {'mobile': login_form.cleaned_data['mobile']}
		return render(request, self.template_name)

auth = Auth.as_view()

class Login(View):
	template_name = "auth.html"
	def post(self, request):
		redirect_url = '/'
		if request.user.is_authenticated:
			return redirect(redirect_url)
		email = request.POST.get('email')
		passwd = request.POST.get('pwd')
		print(email, passwd)
		user = authenticate(username=email, password=passwd)
		print(user)
		if user:
			login(self.request, user)
			return redirect(redirect_url)
		context = {
			'email': email,
			'error': 'Invalid Credentials',
			'next': self.request.GET.get('next'),
		}
		return render(request, self.template_name, context)

auth_login = Login.as_view()


class Register(View):
	def post(self, request):
		redirect_url = '/'
		if request.user.is_authenticated:
			return redirect(redirect_url)

		f_name = request.POST.get('first_name')
		l_name = request.POST.get('last_name')
		email = request.POST.get('email')
		pwd = request.POST.get('pwd')
		print(f_name, l_name, email, pwd)
		user = User.objects.create_user(email, email, pwd, first_name=f_name, last_name=l_name)
		user.save()
		return redirect('index')

auth_register = Register.as_view()


class Logout(View):
	@method_decorator(login_required)
	def get(self, request):
		logout(request)
		return redirect('/')

auth_logout = Logout.as_view()


