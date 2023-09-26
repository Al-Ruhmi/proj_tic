from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterStudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','name','surename','address','city','country','birth_date','std_pic','std_pic_pass_fro','std_pic_pass_bac']



class UpdateStudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','surename','address','city','country','birth_date','std_pic','std_pic_pass_fro','std_pic_pass_bac']