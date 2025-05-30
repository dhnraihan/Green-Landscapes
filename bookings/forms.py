from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Booking, BookingTimeSlot
from services.models import Service
import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time_slot', 'special_instructions', 'address', 'phone']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'special_instructions': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('service', css_class='form-group col-md-6 mb-3'),
                Column('date', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            'time_slot',
            'special_instructions',
            Row(
                Column('address', css_class='form-group col-md-6 mb-3'),
                Column('phone', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Submit('submit', 'Book Now', css_class='btn btn-primary mt-3')
        )
        
        # Get today's date for min date attribute
        today = datetime.date.today()
        self.fields['date'].widget.attrs['min'] = today.strftime('%Y-%m-%d')
        
        # Set required fields
        self.fields['service'].required = True
        self.fields['date'].required = True
        self.fields['time_slot'].required = True
        
        # Add helpful text
        self.fields['address'].help_text = "Only if different from your account address"
        self.fields['phone'].help_text = "Only if different from your account phone"
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        today = datetime.date.today()
        
        if date < today:
            raise forms.ValidationError("You cannot book an appointment in the past.")
        
        return date
