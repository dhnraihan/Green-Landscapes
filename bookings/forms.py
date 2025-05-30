from django import forms
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
        # Add Tailwind classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-green-500 focus:border-green-500',
                'placeholder': field.label
            })
        
        # Style specific fields
        self.fields['special_instructions'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-green-500 focus:border-green-500 h-32',
            'placeholder': 'Any special instructions for our team...'
        })
        
        # Style the submit button
        self.fields['service'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-green-500 focus:border-green-500 bg-white'
        })
        
        # Style the date input
        self.fields['date'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-green-500 focus:border-green-500',
            'type': 'date'
        })
        
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
