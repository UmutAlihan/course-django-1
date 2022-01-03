from django import forms

from .models import Review


"""class ReviewForm(forms.Form):
# "XForm" postfix is a naming convention
# not defining any database model
# justifying shape of the form with a different input fields in maight offer
# no impact on the database
# automatically generate html content when sent as response & rendered in browser
# similarity to models definiton
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "your name must not be empty!",
        "max_length": "please enter a shorter name!"
    })
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
    #  detaylı bilgi almak için official django Docs'da Form fields reference'a gidebilirsin
"""

class ReviewForm(forms.ModelForm):
    # returns pre-deterined form fields based on model
    class Meta:
        model = Review
        #fields = ['user_name', 'review_text', 'rating']
        fields = "__all__"  # except for id uses all properties in given model
        #exclude = ["ownder_comment"] # exclude some fields from form
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating",
        }
        error_messages ={
            "user_name": {
                "required": "your name must not be empty!",
                "max_length": "please enter a shorter name!"
            }
        }
