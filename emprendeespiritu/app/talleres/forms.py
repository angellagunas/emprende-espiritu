from django import forms


class CommentTallerForm(forms.Form):
    comentario = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'required': True,
                'size': 200,
                'class':'materialize-textarea',
                'style':'height: 22px;'
            }
        )
    )
