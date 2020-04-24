from django import forms


class DemoForm(forms.Form):
    room_number_total = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number', 'name': 'SoPhong', 'min': '1', 'max': '15', 'class': 'span3 form-control',
               'placeholder': '-----', 'required': ''}))
    bathroom_number = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number', 'name': 'SoPhongNgu', 'min': '1', 'max': '15', 'class': 'span3 form-control',
               'placeholder': '-----', 'required': ''}))
    bedroom_number = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number', 'name': 'SoPhongTam', 'min': '1', 'max': '10', 'class': 'span3 form-control',
               'placeholder': '-----', 'required': ''}))
    acreage = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number', 'name': 'DienTich', 'min': '1', 'max': '1000', 'step': '0.01',
               'class': 'span3 form-control', 'placeholder': '-----', 'required': ''}))
    build_year = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number', 'name': 'NamXayDung', 'min': '1800', 'max': '2019', 'class': 'span3 form-control',
               'placeholder': '-----', 'required': ''}))
    dist_to_center = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number', 'name': 'KCTrungTam', 'min': '1', 'max': '', 'step': '0.01',
               'class': 'span3 form-control', 'placeholder': '-----', 'required': ''}))
    dist_to_airport = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number', 'name': 'KCSanBay', 'min': '1', 'max': '', 'step': '0.01',
               'class': 'span3 form-control', 'placeholder': '-----', 'required': ''}))
    dist_to_station = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'number', 'name': 'KCTauDienNgam', 'min': '1', 'max': '', 'step': '0.01',
               'class': 'span3 form-control', 'placeholder': '-----', 'required': ''}))


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    to_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
