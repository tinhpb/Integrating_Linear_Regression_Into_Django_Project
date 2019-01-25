from django import forms

class DemoForm(forms.Form):
    sophong = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'SoPhong', 'min':'1', 'max':'15', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    sophongngu = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'SoPhongNgu', 'min':'1', 'max':'15', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    sophongtam = forms.CharField(widget=forms.TextInput(attrs={'type':'number','name':'SoPhongTam', 'min':'1', 'max':'10', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    dientich = forms.CharField(widget=forms.TextInput(attrs={'type':'number','name':'DienTich', 'min':'1', 'max':'1000', 'step':'0.01', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    namxaydung = forms.CharField(widget=forms.TextInput(attrs={'type':'number','name':'NamXayDung', 'min':'1800', 'max':'2019', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    kc_trungtam = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'KCTrungTam', 'min':'1', 'max':'', 'step':'0.01','class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    kc_sanbay = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'KCSanBay', 'min':'1', 'max':'', 'step':'0.01','class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    kc_taudienngam = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'KCTauDienNgam', 'min':'1', 'max':'','step':'0.01', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    # art_expos = forms.CharField(widget=forms.TextInput(attrs={'type':'number', 'name':'Art_Expos', 'min':'1', 'max':'299', 'class':'span3 form-control', 'placeholder':'-----', 'required':''}))
    
class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    to_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
