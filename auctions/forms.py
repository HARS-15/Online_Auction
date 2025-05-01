from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator


class CreateListingForm(forms.Form):
    title = forms.CharField(
        label="",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name of the Product",
                "class": "form-control",
                "aria-describedby": "basic-addon1",
            }
        ),
    )

    CATAGORY_CHOICES = [
        ("Unspecified", "Unspecified"),
        ("Vehicles", "Vehicles"),
        ("Electronics", "Electronics"),
        ("Fashion", "Fashion"),
        ("Home", "Home"),
        ("Antiques", "Antiques"),
        ('Jewellery','Jewellery'),
        ('Paintings','Paintings'),
        ('Books','Books'),
    ]

    category = forms.ChoiceField(
        label="",
        choices=CATAGORY_CHOICES,
        initial="Unspecified",
        widget=forms.Select(
            attrs={"class": "form-control", "id": "inputGroupSelect01"}
        ),
    )

    discription = forms.CharField(
        max_length=255,
        widget=forms.Textarea(
            attrs={
                "rows": "5",
                "placeholder": "About an Item",
                "class": "form-control",
            }
        ),
    )

    starting_bid = forms.IntegerField(
        validators=[MinValueValidator(10)],
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Starting bid price",
                "class": "form-control",
                "aria-describedby": "basic-addon1",
            }
        ),
    )

    image_url = forms.URLField(
        label="",
        max_length=255,
        widget=forms.URLInput(
            attrs={
                "placeholder": "Image URL",
                "class": "form-control",
                "aria-describedby": "basic-addon1",
            }
        ),
    )
    discount = forms.IntegerField(
        label="",
        required=False,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Discount (%)",
                "class": "form-control",
                "aria-describedby": "basic-addon1",
            }
        ),
    )


class BidForm(forms.Form):
    bid = forms.IntegerField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Bid amount",
                "class": "form-control",
                "aria-describedby": "basic-addon1",
            }
        ),
    )

    comment = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.Textarea(
            attrs={
                "rows": "3",
                "placeholder": "Write a comment...",
                "class": "form-control",
                "aria-describedby": "button-addon1",
            }
        ),
    )
