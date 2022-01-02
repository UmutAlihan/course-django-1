from django import forms

class ReviewForm(forms.Form):
# "XForm" postfix is a naming convention
# not defining any database model
# justifying shape of the form with a different input fields in maight offer
# no impact on the database
# automatically generate html content when sent as response & rendered in browser
    user_name = forms.CharField() # similarity to models