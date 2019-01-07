from django import forms

class DemoForm(forms.Form):
    tongsophong = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'TongSoPhong', 'min':'1', 'max':'15', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    sophongngu = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'SoPhongNgu', 'min':'1', 'max':'15', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    sophongtam = forms.CharField(widget=forms.TextInput(attrs={'type':'number','name':'SoPhongTam', 'min':'1', 'max':'10', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    dientich = forms.CharField(widget=forms.TextInput(attrs={'type':'number','name':'DienTich', 'min':'1', 'max':'1000', 'step':'0.01', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    namxaydung = forms.CharField(widget=forms.TextInput(attrs={'type':'number','name':'NamXayDung', 'min':'1800', 'max':'2018', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    num_parking = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Num_Parking', 'min':'1', 'max':'2', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    accessible_buildings = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Accessible_Buildings', 'min':'1', 'max':'9', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    family_quality = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Family_Quality', 'min':'1', 'max':'199', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    art_expos = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Art_Expos', 'min':'1', 'max':'299', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    emergency_shelters = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Emergency_Shelters', 'min':'1', 'max':'99', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    emergency_water = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Emergency_Water', 'min':'1', 'max':'299', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    Facilities = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Facilities', 'min':'1', 'max':'299', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    fire_stations = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Fire_Stations', 'min':'1', 'max':'99', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    Cultural = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Cultural', 'min':'1', 'max':'99', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    Monuments = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Monuments', 'min':'1', 'max':'99', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    police_stations = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Police_Stations', 'min':'1', 'max':'99', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    Vacant = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Vacant', 'min':'1', 'max':'99', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    Free_Parking = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Free_Parking', 'min':'1', 'max':'99', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    to_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
