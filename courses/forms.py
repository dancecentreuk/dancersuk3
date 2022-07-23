from django import forms
from .models import *

class CreateCoursesForm(forms.ModelForm):


    start_time = forms.CharField(max_length=20, widget=forms.TimeInput(
        attrs={'class': 'new-input', 'type': 'time', }
    ))

    end_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'class': 'new-input', 'type': 'time', 'id': 'end_time'}
        )
    )

    class Meta:
        model = WeeklyDanceClass
        fields = ['title', 'location', 'dance_style', 'course_level',  'age_group', 'day', 'start_time', 'end_time', 'address',
                  'postcode', 'price', 'teacher', 'faq', 'clothes', 'experience', 'average_age', 'drop_in',
                  'about_dance_class', 'dance_class_image', 'dance_class_image_1', 'dance_class_image_2', 'dance_class_image_3']


        widgets = {
            'title': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter Class Title', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'Enter Job Description'}),
            'category': forms.Select(attrs=({'class': 'new-input'})),
            'location': forms.Select(attrs=({'class': 'new-input'})),
            'dance_style': forms.Select(attrs=({'class': 'new-input'})),
            'course_level': forms.Select(attrs=({'class': 'new-input'})),
            'address': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter  Address', 'required': True}),
            'postcode': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter  Postcode', 'required': True}),
            'price': forms.NumberInput(attrs={'min': '0', 'class': 'new-input', 'placeholder': 'Enter  Cost'}),
            'teacher': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter instructors name', 'required': True}),
            'faq': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'Enter frequently asked questions and answers', 'required': True}),
            'clothes': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'What to wear to class', 'required': True}),
            'experience': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'How much experience is required', 'required': True}),
            'average_age': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'What is average age in class', 'required': True}),
            'drop_in': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Is this a drop in class or course', 'required': True}),
            'about_dance_class': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'About the dance class', 'required': True}),

            'age_group': forms.Select(attrs=({'class': 'new-input'})),
            'day': forms.Select(attrs=({'class': 'new-input'})),
            'fee': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Fee'}),

        }







class UpdateCourseForm(forms.ModelForm):
    class Meta:
        model = WeeklyDanceClass
        fields = ['title', 'location', 'dance_style', 'course_level', 'age_group', 'day', 'start_time', 'end_time', 'address',
                  'postcode', 'price', 'teacher', 'faq', 'clothes', 'experience', 'average_age', 'drop_in',
                  'about_dance_class', 'dance_class_image', 'dance_class_image_1', 'dance_class_image_2', 'dance_class_image_3']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'new-input', 'placeholder': 'Enter Class Title', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'Enter Job Description'}),
            'category': forms.Select(attrs=({'class': 'new-input'})),
            'location': forms.Select(attrs=({'class': 'new-input'})),
            'dance_style': forms.Select(attrs=({'class': 'new-input'})),
            'course_level': forms.Select(attrs=({'class': 'new-input'})),
            'address': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Enter  Address', 'required': True}),
            'postcode': forms.TextInput(
                attrs={'class': 'new-input', 'placeholder': 'Enter  Postcode', 'required': True}),
            'price': forms.NumberInput(attrs={'min': '0', 'class': 'new-input', 'placeholder': 'Enter  Cost'}),
            'teacher': forms.TextInput(
                attrs={'class': 'new-input', 'placeholder': 'Enter instructors name', 'required': True}),
            'faq': forms.Textarea(
                attrs={'class': 'description-input', 'placeholder': 'Enter frequently asked questions and answers',
                       'required': True}),
            'clothes': forms.TextInput(
                attrs={'class': 'new-input', 'placeholder': 'What to wear to class', 'required': True}),
            'experience': forms.TextInput(
                attrs={'class': 'new-input', 'placeholder': 'How much experience is required', 'required': True}),
            'average_age': forms.TextInput(
                attrs={'class': 'new-input', 'placeholder': 'What is average age in class', 'required': True}),
            'drop_in': forms.TextInput(
                attrs={'class': 'new-input', 'placeholder': 'Is this a drop in class or course', 'required': True}),
            'about_dance_class': forms.Textarea(
                attrs={'class': 'description-input', 'placeholder': 'About the dance class', 'required': True}),

            'age_group': forms.Select(attrs=({'class': 'new-input'})),
            'day': forms.Select(attrs=({'class': 'new-input'})),
            'fee': forms.TextInput(attrs={'class': 'new-input', 'placeholder': 'Fee'}),

        }




class CourseReviewForm(forms.ModelForm):
    class Meta:
        model = CourseReview
        fields = ['comment', 'rating']

        labels = {
            'comment': ('Review'),
            'rating': ('Rating out of 10'),
        }

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'label': 'review'}),
            'rating': forms.TextInput(attrs={ 'type':'range', 'id' :'rangeInput',
                                             'min':'0', 'max':'10', 'step':'0.5', 'oninput': 'amount.value=rangeInput.value',
                                             }),

        }






