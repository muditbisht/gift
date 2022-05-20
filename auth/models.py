from django.db import models
from django.contrib.auth.models import User

import random
#All Tables in Objects format -->


# class OTP(models.Model):
# 	mobile = models.CharField(unique=True, max_length=10,db_index=True)
# 	otp = models.CharField(max_length=5)
# 	generate_time = models.DateTimeField(auto_now=True)
#
# 	def generate_otp(self):
# 		otp = random.randint(1,9)
# 		for _ in range(3):
# 			otp = otp*10 + random.randint(0,9)
# 		self.otp = str(otp)
# 		self.save()
#
# 	def __str__(self):
# 		return 'OTP for '+self.mobile
#
# def checkOTP(mobile,otp):
# 	try:
# 		O = OTP.objects.get(mobile = mobile)
# 		result = (O.otp==otp)
# 		if result:
# 			O.delete()
# 		return result
# 	except:
# 		return False
#
# def OTP_Authenticate(mobile=None,otp=None):
# 	if checkOTP(mobile,otp):
# 		try:
# 			auth = User.objects.get(username=mobile)
# 			return auth
# 		except User.DoesNotExist:
# 			pass
#
#
# # data of users  -->
# class UserData(models.Model):
# 	marritial_status = (
# 		(False, 'Un-Married'),
# 		(True, 'Married'),
# 	)
# # Columns of Table --->
# 	auth = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True)
# 	is_email_verified = models.BinaryField(default=False)
# 	married_status = models.BinaryField(verbose_name="Is auth married ", max_length=1,default=False)
# 	unread_messages = models.IntegerField(verbose_name="Unread messages", default=0)
#
# 	class Meta:
# 		verbose_name = 'User Data'
# 		verbose_name_plural = 'Users Data'
#
# 	def update_marritialStatus(self,status):
# 		self.married_status = status
# 		self.save()
#
# 	def get_notifications(self):
# 		return Notification.objects.filter(auth=self.id)
#
#
# # messages & notification stored --->
# class Notification(models.Model):
# 	auth = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
# 	is_readed = models.BinaryField(verbose_name="Is message read", default=0)
# 	subject = models.CharField(max_length=200, blank=True)
# 	text = models.TextField(blank=True)
# 	# order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
# 	time_sent = models.DateTimeField(verbose_name="Message sent", auto_now=True)
# 	time_read = models.DateTimeField(verbose_name="Message recieved", auto_now=False,null=True)
#
# 	class Meta:
# 		verbose_name = 'Message'
# 		verbose_name_plural = 'Messages'
# 		get_latest_by = ('-time_sent', 'time_read')
# 		order_with_respect_to = 'auth'

