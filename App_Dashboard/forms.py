from django import forms
from App_Dashboard.models import DesignerInfo, Post, Reply, DesignerMessage


class DesignerInfoForm(forms.ModelForm):
    class Meta:
        model = DesignerInfo
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description',]


class ReplyFrom(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'


class DesignerMessageFrom(forms.ModelForm):
    class Meta:
        model = DesignerMessage
        fields = ['reply_message',]
