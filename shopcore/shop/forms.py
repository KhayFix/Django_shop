from django import forms


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': r'Recipient\'s username',
        'aria-describedby': 'basic-addon2',
    }))
