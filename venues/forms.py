from django import forms
from .models import *

class AddVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'category', 'address', 'postcode','location', 'contact', 'contact_email', 'contact_mobile',
                  'mirrors', 'wooden_floor', 'music_system', 'floor_type', 'size', 'cost', 'venue_image', 'about_venue',
                  'venue_image_1', 'venue_image_2']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter Venue', 'required': True}),
            'address': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter  Address', 'required': True}),
            'postcode': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter Postcode', 'required': True}),
            'location': forms.Select(attrs=({'class': 'new-input'})),
            'contact': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter Venue Contact', 'required': True}),
            'contact_email': forms.EmailInput(attrs={'class': 'new-input', 'placeholder': 'Enter Email', 'required': True}),
            'contact_mobile': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter mobile', 'required': True}),
            'floor_type': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter Floor type ie wooden carpet harlequin', 'required': True}),
            'about_venue': forms.Textarea(
                attrs={'class': 'description-input', 'placeholder': 'Tell us something about your Space',
                       'required': True}
            ),
            'size': forms.NumberInput(attrs={'class': 'new-input', 'placeholder': 'Enter venue size sqft', 'required': True}),
            'cost': forms.NumberInput(attrs={'class': 'new-input', 'placeholder': 'Enter cost per hour', 'required': True}),

            'category': forms.Select(attrs=({'class': 'new-input'})),


        }



class UpdateVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'category', 'address', 'postcode','location', 'contact', 'contact_email', 'contact_mobile',
                  'mirrors', 'wooden_floor', 'music_system', 'floor_type', 'cost', 'venue_image', 'venue_image_1', 'venue_image_2']

