from django import forms
from django.contrib.auth.models import User

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

#　お問い合わせ
class ContactForm(forms.Form):

    email = forms.CharField(
        label="メールアドレス",
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "メールアドレス",
            }
        )
    )
    subject = forms.CharField(
        label="件名",
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "件名",
            }
        )
    )

    message = forms.CharField(
        label="問い合わせ内容",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "問い合わせ内容"
            }
        )
    )

    def send_email(self):
        subject = "【お問い合わせ" + self.cleaned_data["subject"]
        message = self.cleaned_data["message"]
        email = self.cleaned_data["email"]
        recipient_list = ["hw19a107@oecu.jp"]   ### 送信先
        try:
            send_mail(subject, message, email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")