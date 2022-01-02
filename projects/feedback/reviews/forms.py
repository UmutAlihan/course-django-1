from django import forms

class ReviewForm(forms.Form):
# "XForm" postfix is a naming convention
# not defining any database model
# justifying shape of the form with a different input fields in maight offer
# no impact on the database
# automatically generate html content when sent as response & rendered in browser
# similarity to models definiton
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages= {
        "required": "your name must not be empty!",
        "max_length": "please enter a shorter name!"
    })