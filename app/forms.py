from django import forms

class Registration(forms.Form):
    stu_name=forms.CharField(max_length=50)
    stu_email=forms.EmailField()
    stu_contact=forms.IntegerField()



class Login(forms.Form):
    email=forms.EmailField()
    contact=forms.Field()