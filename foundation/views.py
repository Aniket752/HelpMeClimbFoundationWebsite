from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import donation,volunteer,donationMade,massage,recipt
from . import forms
from django.core.mail import send_mail
import json
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
from django.core import mail
from django.template.loader import render_to_string,get_template
from xhtml2pdf import pisa
from django.utils.html import strip_tags
from django.views.generic import View
from .utils import render_to_pdf

def GeneratePdf(View):
    form=View.POST
    date=form['TXNDATE']
    name=form['ORDERID']
    print(name)
    for p in donation.objects.raw('SELECT * FROM foundation_donation WHERE orderid=%s',[name]):
        name1=p.Name
        contact=p.Contact
        email=p.Email
        pan=p.Pan_no
        #print(p.Contact)
    Amount=form['TXNAMOUNT']
    T_id=form['BANKTXNID']
    recipt_dict={
        'r_no' : name,
        'Name' : name1,
        'Date' : date,
        'amount' : Amount,
        't_id' : T_id,
        'email' : email
    }
    pdf = render_to_pdf('foundation/mail.html',recipt_dict)
    respons_dict={}
    for i in form.keys():
        respons_dict[i]=form[i]
    return render(View,'foundation/paymentstatus.html',{'RESPCODE':respons_dict})
def index(request):
    return render(request,'foundation/index.html')
def ret(request):
    return redirect('/')
def devloper(request):
    return render(request,'foundation/donate.html')
def dev(request):
    return redirect('/donate')
def covid(request):
    return render(request,'foundation/covid-19.html')
def case(request):
    return render(request,'foundation/case1.html')
def case3(request):
    return render(request,'foundation/case3.html')
def case2(request):
    return render(request,'foundation/case2.html')
def bank(request):
    return render(request,'foundation/bank.html')
def ban(request):
    return redirect('/bank')
def eve(request):
    return redirect('/event')
def event(request):
    return render(request,'foundation/event.html')
def submit(request):
    form=forms.donate()
    if request.method=="GET":
        name=request.GET['name']
        email=request.GET['email']
        contact=request.GET['number']
        address=request.GET['address']
        amount=request.GET['amount']
        who=request.GET['select']
        massage=request.GET['message']
        t_id=request.GET['pan']
        id=request.GET['orderid']
        print(id)
        donate=donation(Name=name,Email=email,orderid=id,Contact=contact,address=address,amount=amount,Pan_no=t_id,who=who,massage=massage)
        donate.save()
        param_dict={
          'MID':'yPZMcc10641886315792',
            'ORDER_ID':str(id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	    'CALLBACK_URL':' http://127.0.0.1:8000/donate/submit/handlerequest/',
        }
        MID='OujsI_6hXzbFcag@'
        param_dict['CHECKSUMHASH']= Checksum.generate_checksum(param_dict,MID)
        return render(request,'foundation/paytm.html',{'param_dict':param_dict})
    return render(request,'foundation/index.html')
@csrf_exempt
def handlerequest(request):
    form=request.POST
    print(form)
    respons_dict={}
    MID='OujsI_6hXzbFcag@'
    name=form['ORDERID']
    print(name)
    for p in donation.objects.raw('SELECT * FROM foundation_donation WHERE orderid=%s',[name]):
        name1=p.Name
        contact=p.Contact
        email=p.Email
        pan=p.Pan_no
        #print(p.Contact)
    Amount=form['TXNAMOUNT']
    T_id=form['BANKTXNID']
    for i in form.keys():
        respons_dict[i]=form[i]
        if i=='CHECKSUMHASH':
            checksum=form[i]
    verify=Checksum.verify_checksum(respons_dict,MID,checksum)
    if verify:
        if respons_dict['RESPCODE']=='01':
            date=form['TXNDATE']
            recipt_dict={
                'r_no' : name,
                'Name' : name1,
                'Date' : date,
                'amount' : Amount,
                't_id' : T_id,
            }
            donateMade=donationMade(orderid=name,Pan_no=pan,Name=name1,Email=email,Contact=contact,amount=Amount,t_id=T_id,date=date)
            donateMade.save()
            subject='Doner recipt'

        #    if not paisa_status.err:
        #        return HttpResponse('error <pre>'+html+'</pre>')

            print('done')
            '''from_email='moversandpackers230@gmail.com'
            to=email
            html_message=render_to_string('foundation/mail.html',{'values':recipt_dict})
            plain=strip_tags(html_message)
            mail.send_mail(subject,plain,from_email,[to],html_message=html_message)
            print('mail')'''
            reciptno=recipt(r_no=name,name=name1,amount=Amount,date=date)
            reciptno.save()
            #return render_pdf_view(request)
        else:
            print("fail")
    return GeneratePdf(request)
def sendmessage(request):
        if request.method=="GET":
            name=request.GET['name']
            email=request.GET['email']
            contact=request.GET['subject']
            address=request.GET['message']
            mass=massage(Name=name,Email=email,subject=contact,messages=address)
            mass.save()
        return redirect('/')
