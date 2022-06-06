from dashboard.models import admin_profile
from django import forms

# class productForm(forms.Form):
#     name=forms.CharField()
#     email= forms.EmailField()
#     mobile= forms.IntegerField()
#     dob= forms.DateField()
#     address= forms.Textarea()
#     img= forms.ImageField()

#     def save(self):
#         print(self.cleaned_data)

class ProductForm(forms.ModelForm):
    class Meta:
        model = admin_profile
        fields = ['name','email','mobile','dob','address','img']
        widgets = { 
            'img' : forms.FileInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            
        }




    
    
  
            
  

     

