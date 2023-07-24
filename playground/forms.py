from django import forms


class NameForm(forms.Form):
    username = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'class': 'myfieldclass',
                                                          'placeholder' : 'Name'}))
    email = forms.EmailField(max_length=100,
                            widget=forms.TextInput(attrs={'class': 'myfieldclass',
                                                          'placeholder' : 'Email'}))
    password1 = forms.CharField(max_length=100, label= "Password",
                            widget=forms.TextInput(attrs={'class': 'myfieldclass',
                                                          'placeholder' : 'Password'}))
    password2 = forms.CharField(max_length=100, label="Confirm Password",
                            widget=forms.TextInput(attrs={'class': 'myfieldclass',
                                                          'placeholder' : 'Confirm Password'
                                                          }))


