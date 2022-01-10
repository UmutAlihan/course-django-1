from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    # ModelForm is ok because we want to get input via form for Model we have
    # nested Meta class is for configuration
    class Meta:
        model = Comment
        # dont wanna include all fields, user should only see specific fields
        exclude = ["post"]
        # to overwrite default labels
        # note using "User Name" instead "Your Name"
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }