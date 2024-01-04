from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['mobile']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['mobile']


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'price', 'description', 'product_image', 'product_image1', 'product_image2', 'product_image3',
                  'product_image4']


# address of shipment
class AddressForm(forms.Form):
    Mobile = forms.IntegerField()


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ['name', 'feedback']

class orderCreateForm(forms.ModelForm):
    class Meta:
        model = models.Orders
        fields = ['name','mobile']


# for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
