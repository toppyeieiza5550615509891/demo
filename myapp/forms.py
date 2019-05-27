from django import forms
from myapp.models import UserModel, BlogModel, CommentModel



class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Username', 'type':'text',}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',  'placeholder':'Password', 'type':'password'}))
    givename = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sam' ,'type':'text'}))
    lastname =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Elika'}))
    tel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'0244567'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'abc@gmaiol.com'}))
    class Meta:
        model = UserModel
        fields = '__all__'


class BlogForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = CommentModel
        fields = '__all__'


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = CommentModel
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    givename = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':"givenname"}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':"lastname"}))
    tel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':"tel"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':"email"}))
    class Meta:
        model = UserModel
        fields = ['email', 'tel', 'lastname', 'givename']
        # fields = '__all__'
    
