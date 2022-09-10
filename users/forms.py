from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ChoiceField, DateInput


from pages.choices import account_type_choice, location_choices, gender_choices, kg_choices, ethnicity_choices
from .models import Account, Profile, DancersProfile, CompanyProfile, DancerImage



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'new-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'new-input'}))


class AccountRegisterForm(UserCreationForm):


    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'new-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'new-input'}))

    first_name = forms.CharField(
        label='Firstname', min_length=1, max_length=50, widget=forms.TextInput(
            attrs={'class': 'new-input', 'placeholder': 'Firstname', 'id': 'form_firstname'}))

    last_name = forms.CharField(
        label='Lastname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'new-input', 'placeholder': 'Lastname', 'id': 'form-lastname'}))

    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'new-input', 'placeholder': 'Email', 'id': 'form-email'}
        )
    )

    location = forms.CharField(label='Location',
                               widget=forms.Select(choices=location_choices,
                                   attrs={'class': 'new-input', 'placeholder': 'Location', 'id': 'location'}
                               )
                               )

    gender = forms.CharField(label='Gender',
                               widget=forms.Select(choices=gender_choices,
                                                   attrs={'class': 'new-input',
                                                          'id': 'gender'}
                                                   )
                               )

    date_of_birth = forms.DateField(
         widget=forms.DateInput(
            attrs={'class': 'new-input',  'type': 'date', 'id': 'date_of_birth'}
        )
    )





    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'gender', 'location', 'date_of_birth', 'password1', 'password2']




class AccountProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'mobile', 'location']



class UserUpdateForm(forms.ModelForm):


    date_of_birth = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type': 'date', 'class':'new-input__modal' }))
    # profile_image = forms.ImageField(widget=forms.FileInput(attrs={
    #     "class": "new-input__modal",}))


    class Meta:


        model = Profile
        fields = [ 'date_of_birth', 'mobile', 'location' , 'profile_image',]

        widgets = {
            'mobile': forms.TextInput(attrs={'class': 'new-input__modal', 'placeholder': 'Enter Mobile', 'required': True}),
            'location': forms.Select(attrs=({'class': 'new-input__modal'})),

        }


class DancersUpdateForm(forms.ModelForm):



    bio = forms.CharField(label='Bio',
                             widget=forms.Textarea(
                                                 attrs={'class': 'new-input__modal-textarea',
                                                        'label': 'Your Weight', 'required': True
                                                        }
                                                 )
                             )

    experience = forms.CharField(label='Experience',
                          widget=forms.Textarea(
                              attrs={'class': 'new-input__modal-textarea'

                                     }
                          )
                          )

    credits = forms.CharField(label='Credits',
                                 widget=forms.Textarea(
                                     attrs={'class': 'new-input__modal-textarea'

                                            }
                                 )
                                 )

    # 'bio': forms.Textarea(
    #     attrs={'class': 'new-input__modal', 'rows': '3', 'cols': '5', 'placeholder': 'Enter Mobile', 'required': True}),

    class Meta:
        model = DancersProfile
        fields = [ 'dancers_image', 'location', 'primary_job',  'bio', 'experience',  'credits', ]

        widgets = {

            'primary_job': forms.Select(attrs=({'class': 'new-input__modal'})),

            # 'bio': forms.Textarea(
            #     attrs={'class': 'new-input__modal', 'rows':'3', 'cols':'5', 'placeholder': 'Enter Mobile', 'required': True}),

        }




class CompanyUpdateForm(forms.ModelForm):
    company_bio = forms.CharField(label='Company Bio',
                                 widget=forms.Textarea(
                                     attrs={'class': 'new-input__modal-textarea'

                                            }
                                 )
                                 )

    class Meta:
        model = CompanyProfile
        fields = [ 'company_image', 'company_name', 'company_email', 'company_mobile', 'company_bio', 'is_active']

        widgets = {

            'company_name': forms.TextInput(attrs=({'class': 'new-input__modal'})),
            'company_email': forms.TextInput(attrs=({'class': 'new-input__modal'})),
            'company_mobile': forms.TextInput(attrs=({'class': 'new-input__modal'})),

        }


class DancerImageForm(forms.ModelForm):
    class Meta:
        model = DancerImage
        fields = ['title', 'image']


