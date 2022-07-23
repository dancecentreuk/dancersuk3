from django import forms
from .models import *

class CreateListingForm(forms.ModelForm):

    # rehearsal_date = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type': 'date', 'class':'new-input' }))
    listing_image = forms.ImageField(required=False)



    class Meta:
        model = Listing
        fields = ['title', 'description', 'category', 'location',  'fee', 'listing_image']


        widgets = {
            'title': forms.TextInput(attrs={'class':'new-input', 'placeholder':'Enter Job Title', 'required':True }),
            'description': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'Enter Job Description'}),
            'category': forms.Select(attrs=({'class': 'new-input'})),
            'location': forms.Select(attrs=({'class': 'new-input'})),
            'fee': forms.TextInput(attrs={'class':'new-input', 'placeholder':'Fee'}),

        }




class UpdateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'category', 'location',  'fee', 'listing_image']
        labels = {'location': 'Choose a  Location'}

        listing_image = forms.ImageField(required=False)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter Job Title', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'Enter Job Description'}),
            'category': forms.Select(attrs=({'class': 'new-input'})),
            'location': forms.Select(attrs=({'class': 'new-input'})),
            'fee': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Fee', 'type':'number'}),

        }


class CreatePostingForm(forms.ModelForm):

    # date = forms.CharField(max_length=20, widget=forms.DateInput(
    #     attrs={'class': 'form-control', 'type':'date', 'placeholder':'Enter Job Date'}
    # ))

    date = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type': 'date', 'class':'new-input' }))



    start_time = forms.CharField(max_length=20, widget=forms.TimeInput(
        attrs={'class': 'new-input', 'type': 'time', 'placeholder': 'Enter Job Date'}
    ))
    end_time = forms.CharField(max_length=20, widget=forms.TimeInput(
        attrs={'class': 'new-input', 'type': 'time', 'placeholder': 'Enter Job Date'}
    ))

    class Meta:
        model = Listing
        fields = ['title', 'description',  'date', 'start_time', 'end_time', 'category', 'location',  'fee', 'listing_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter Job Title', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'Enter Job Description'}),
            'category': forms.Select(attrs=({'class': 'new-input'})),
            'location': forms.Select(attrs=({'class': 'new-input'})),
            'fee': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Fee', 'type':'number'}),

        }


class UpdatePostingForm(forms.ModelForm):

    date = forms.CharField(max_length=20, widget=forms.DateInput(
        attrs={'class': 'new-input', 'type': 'date', 'placeholder': 'Enter Job Date'}
    ))

    start_time = forms.CharField(max_length=20, widget=forms.TimeInput(
        attrs={'class': 'new-input', 'type': 'time', 'placeholder': 'Enter Job Date'}
    ))
    end_time = forms.CharField(max_length=20, widget=forms.TimeInput(
        attrs={'class': 'new-input', 'type': 'time', 'placeholder': 'Enter Job Date'}
    ))

    listing_image = forms.ImageField(label='Image',
                             widget=forms.ClearableFileInput(attrs={'class': 'image-input'}))

    # listing_image = forms.CharField(widget=forms.ImageField(
    #     attrs={'class': 'new-input'  }
    # ))
    class Meta:
        model = Listing
        fields = ['title', 'description', 'date', 'start_time', 'end_time', 'category', 'location',
                   'fee', 'listing_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter Job Title', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'Enter Job Description'}),
            'category': forms.Select(attrs=({'class': 'new-input'})),
            'location': forms.Select(attrs=({'class': 'new-input'})),
            'fee': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Fee', 'type':'number'}),

        }




