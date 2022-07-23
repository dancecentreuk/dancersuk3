from django import forms
from .models import *


class CreateCommunicationForm(forms.ModelForm):
    # content = forms.CharField(
    #     label='Message', widget=forms.TextInput(
    #         attrs={'class': 'form-control mb-3',  }))
    class Meta:
        model = Communication
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'write message'}),


        }

    def __init__(self, *args, **kwargs):
        super(CreateCommunicationForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Message"


class NewComsForm(CreateCommunicationForm):

    title = forms.CharField(widget=forms.HiddenInput())

    class Meta(CreateCommunicationForm.Meta):
        fields = CreateCommunicationForm.Meta.fields + ['title']




class HideConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = []







    # def __init__(self, *args, **kwargs):
    #     super(HideConversationForm, self).__init__(*args, **kwargs)
    #     if self.instance and self.instance.level < 3:
    #         self.fields['job'].disabled = True  # still displays the field in the template
    #         # del self.fields['job'] # removes field from form and template
    #     if self.instance and self.instance.level < 1:
    #         self.fields['avatar'].disabled = True
