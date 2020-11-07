from django import forms

measurements =( 
    ("1", "1/2"), 
    ("2", "1/3"), 
    ("3", "1/4"), 
) 

class CreateNewRecipe(forms.Form):
    name = forms.CharField(label="Food Name", required=False, max_length=200)
    ingredients = forms.CharField(widget=forms.Textarea, label="Ingredients", required=False, max_length=200)
    prep = forms.CharField(widget=forms.Textarea, label="Preparations", required=False, max_length=200)
    image = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea, required=True, max_length=500)
    #sizes = forms.ChoiceField(choices = measurements) 
