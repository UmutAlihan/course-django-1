from django import forms


class ReviewForm(forms.Form):
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
