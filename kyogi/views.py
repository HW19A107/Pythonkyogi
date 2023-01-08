from django.shortcuts import render

from django.urls.base import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm

#新規登録、ログイン処理--
from django.views.generic import TemplateView # テンプレートタグ
from .forms import AccountForm # ユーザーアカウントフォーム
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#-->
from .models import total
from django.utils import timezone

from .graph import Plot_Graph_ranking

# Create your views here.
def frontpage(request):
    return render(request, "kyogi/frontpage.html")

def inquirypage(request):
    return render(request, "kyogi/inquiry.html")

def Q1page(request):
    params = {"UserID":request.user,}
    return render(request, "kyogi/question/Q1.html",context=params)

def Q2page(request):
    params = {"UserID":request.user,}
    return render(request, "kyogi/question/Q2.html",context=params)

def Q3page(request):
    params = {"UserID":request.user,}
    return render(request, "kyogi/question/Q3.html",context=params)

def Q4page(request):
    params = {"UserID":request.user,}
    return render(request, "kyogi/question/Q4.html",context=params)

def Q5page(request):
    params = {"UserID":request.user,}
    return render(request, "kyogi/question/Q5.html",context=params)

def lastpage(request):
    params = {"UserID":request.user,}
    return render(request, "kyogi/last.html",context=params)
#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["AccountCreate"] = False
        return render(request,"kyogi/register.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"kyogi/register.html",context=self.params)

#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'kyogi/login.html')

#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))


#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "kyogi/home.html",context=params)

def totals(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        number = request.POST.get('number')
        clear = request.POST.get('clear')
        clear_time = request.POST.get('clear_time')
        date = timezone.now()
    
        model = total(name=name,number=number,clear=clear,clear_time=clear_time,datetime=date)
        model.save()

        response = None
        return HttpResponse('response')
#グラフ
class graph(TemplateView):

    #テンプレートファイル連携
    template_name = "kyogi/graph.html"
    #変数としてグラフイメージをテンプレートに渡す
    def get_context_data(self, **kwargs):
        #グラフオブジェクト
        qs_clear = total.objects.filter(clear = '1')
        x = []
        y = []
        a = [1,2,3,4,5]
        b = [0,0,0,0,0]
        for i in range(len(qs_clear)):
            if qs_clear[i].name not in x:
                x.append(qs_clear[i].name)
                y.append(int(qs_clear[i].clear))   
            else : 
                index = x.index(qs_clear[i].name)
                y[index] += 1

        for j in range(len(qs_clear)):
            b[qs_clear[j].number - 1] +=1
        
        dict_from_list = dict(zip(x,y))
        sort_dict = dict(sorted(dict_from_list.items(), key = lambda i:i[1],reverse=True))
        x = list(sort_dict.keys())
        y = list(sort_dict.values())
        
        #Q1clear_time
        qs_time1 = total.objects.filter(clear = '1',number = '1')
        c = []
        d = []
        for k in range(len(qs_time1)):
            c.append(qs_time1[k].name)
            d.append(int(qs_time1[k].clear_time))

        time_from_list1 = dict(zip(c,d))
        sort_time = dict(sorted(time_from_list1.items(), key = lambda i:i[1]))
        c = list(sort_time.keys())
        d = list(sort_time.values())

        #Q2clear_time
        qs_time2 = total.objects.filter(clear = '1',number = '2')
        e = []
        f = []
        for k in range(len(qs_time2)):
            e.append(qs_time2[k].name)
            f.append(int(qs_time2[k].clear_time))

        time_from_list2 = dict(zip(e,f))
        sort_time = dict(sorted(time_from_list2.items(), key = lambda i:i[1]))
        e = list(sort_time.keys())
        f = list(sort_time.values())

        #Q3clear_time
        qs_time3 = total.objects.filter(clear = '1',number = '3')
        g = []
        h = []
        for k in range(len(qs_time3)):
            g.append(qs_time3[k].name)
            h.append(int(qs_time3[k].clear_time))

        time_from_list3 = dict(zip(g,h))
        sort_time = dict(sorted(time_from_list3.items(), key = lambda i:i[1]))
        g = list(sort_time.keys())
        h = list(sort_time.values())


        #Q4clear_time
        qs_time4 = total.objects.filter(clear = '1',number = '4')
        l = []
        m = []
        for k in range(len(qs_time4)):
            l.append(qs_time4[k].name)
            m.append(int(qs_time4[k].clear_time))

        time_from_list4 = dict(zip(l,m))
        sort_time = dict(sorted(time_from_list4.items(), key = lambda i:i[1]))
        l = list(sort_time.keys())
        m = list(sort_time.values())

        #Q5clear_time
        qs_time5 = total.objects.filter(clear = '1',number = '5')
        n = []
        o = []
        for k in range(len(qs_time5)):
            n.append(qs_time5[k].name)
            o.append(int(qs_time5[k].clear_time))

        time_from_list5 = dict(zip(n,o))
        sort_time = dict(sorted(time_from_list5.items(), key = lambda i:i[1]))
        n = list(sort_time.keys())
        o = list(sort_time.values())

        chart_clear_ranking = Plot_Graph_ranking(x,y,a,b,c,d,e,f,g,h,l,m,n,o)          #グラフ作成

        #変数を渡す
        context = super().get_context_data(**kwargs)
        context['chart_clear_ranking'] = chart_clear_ranking
        return context

    
    #get処理
    def get(self, request, *args, **kwargs): 
        return super().get(request, *args, **kwargs)


def sentakupage(request):
    clear_number = [" "," "," "," "," "," "," "," "," "," "]
    qs_clear_number = total.objects.filter(name = request.user,clear = '1')
    for i in range(len(qs_clear_number)):
        clear_number[qs_clear_number[i].number -1] = "claer"
    
    qs_clear = total.objects.filter(clear = '1')
    x = []
    y = []
    for i in range(len(qs_clear)):
        if qs_clear[i].name not in x:
            x.append(qs_clear[i].name)
            y.append(int(qs_clear[i].clear))
        else : 
            index = x.index(qs_clear[i].name)
            y[index] += 1

    dict_from_list = dict(zip(x,y))
    sort_dict = dict(sorted(dict_from_list.items(), key = lambda i:i[1],reverse=True))
    x = list(sort_dict.keys())
    if str(request.user) not in x:
        my_ranking = "順位なし"
    else:
        my_ranking = str(x.index(str(request.user))+1)+ "位"

    params = {"myranking":my_ranking,"UserID":request.user,"clear1":clear_number[0],"clear2":clear_number[1],"clear3":clear_number[2],"clear4":clear_number[3],"clear5":clear_number[4],"clear6":clear_number[5],"clear7":clear_number[6],"clear8":clear_number[7],"clear9":clear_number[8],"clear10":clear_number[9],}
    return render(request, "kyogi/sentaku.html",context=params)


def lastpage(request):
    qs_clear = total.objects.filter(clear = '1')

    x = []
    y = []
    for i in range(len(qs_clear)):
        if qs_clear[i].name not in x:
            x.append(qs_clear[i].name)
            y.append(int(qs_clear[i].clear))
        else : 
            index = x.index(qs_clear[i].name)
            y[index] += 1

    dict_from_list = dict(zip(x,y))
    sort_dict = dict(sorted(dict_from_list.items(), key = lambda i:i[1],reverse=True))
    x = list(sort_dict.keys())
    if str(request.user) not in x:
        my_ranking = "順位なし"
    else:
        my_ranking = str(x.index(str(request.user))+1)+ "位"

    last_clear = len(total.objects.filter(name = request.user,clear = '1'))
    
    params = {"myranking":my_ranking,"UserID":request.user,"myclear":last_clear}
    return render(request, "kyogi/last.html",context=params)