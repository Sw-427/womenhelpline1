from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from django.views.generic.edit import CreateView
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializer import *
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.contrib.sessions.models import Session
import json
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from django.middleware.csrf import get_token


# Create your views here.

class ReactView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        detail = {}
        iss2 = issues.objects.all()
        detail['issues'] = []
        for a in iss2:
            detail['issues'].append(a.issue)
        states1 = helplines.objects.values_list('state', flat=True)
        states = {}
        for s in states1:
            states[s] = []
        for s in states.keys():
            for ale in helplines.objects.raw('SELECT id,city from core_helplines where state=%s',[s]):
                states[s].append(ale.city)
        detail['location'] = states
        return Response(detail)
    def post(self, request):
        data = request.data
        test = []
        if len(data['issues']) == 0:
            iss222 = issues.objects.all()
            for a in iss222:
                data['issues'].append(a.issue)
       
        if data['location'][0] == 'All States' and data['location'][1] == 'All Cities':
            test.clear()
            for isselp in avail.objects.all():
                if isselp.iss.issue in data['issues'] and isselp.helpline not in test:
                    test.append(isselp.helpline)
            l = []
            issu = []
            # if len(test) == 0:
            #     for a in helplines.objects.all():
            #         test.append(a)
            for a in test:
                issu.clear()
                for ap in avail.objects.filter(helpline=a):
                    issu.append(ap.iss.issue)
                serializer = b(a)
                data1 = json.dumps(serializer.data)
                data2 = json.loads(data1)
                data2['number'] = data2['number'].split(",")
                data2['issues'] = list(issu)
                l.append(data2)
            
            return Response(l)
        elif data['location'][0] != 'All States' and data['location'][1] == 'All Cities':
            test.clear()
            for isselp in avail.objects.all():
                if isselp.iss.issue in data['issues'] and isselp.helpline not in test:
                    test.append(isselp.helpline)
            l = []
            issu = []
            if len(test) == 0:
                    for a in helplines.objects.all():
                        test.append(a)
            helpline = helplines.objects.filter(state = data['location'][0])
            lst3 = [value for value in helpline if value in test]
            for a in lst3:
                issu.clear()
                for ap in avail.objects.filter(helpline=a):
                    issu.append(ap.iss.issue)
                serializer = b(a)
                data1 = json.dumps(serializer.data)
                data2 = json.loads(data1)
                data2['number'] = data2['number'].split(",")
                data2['issues'] = list(issu)
                l.append(data2)
            return Response(l)
        else:
            test.clear()
            for isselp in avail.objects.all():
                if isselp.iss.issue in data['issues'] and isselp.helpline not in test:
                    test.append(isselp.helpline)
            l = []
            issu = []
            if len(test) == 0:
                    for a in helplines.objects.all():
                        test.append(a)
            helpline = helplines.objects.filter(city = data['location'][1])
            lst3 = [value for value in helpline if value in test]
            for a in lst3:
                issu.clear()
                for ap in avail.objects.filter(helpline=a):
                    issu.append(ap.iss.issue)
                serializer = b(a)
                data1 = json.dumps(serializer.data)
                data2 = json.loads(data1)
                data2['number'] = data2['number'].split(",")
                data2['issues'] = list(issu)
                l.append(data2)
            return Response(l)

class ReactView2(APIView):
    def post(self, request):
        data =  request.data
        l = []
        issu = []
        lst3 = []
        test = []
        if len(data['issues']) == 0:
            iss222 = issues.objects.all()
            for a in iss222:
                data['issues'].append(a.issue)
        if data['location'][0] == 'All States' and data['location'][1] == 'All Cities':
            test.clear()
            for isselp in avail.objects.all():
                if isselp.iss.issue in data['issues'] and isselp.helpline not in test:
                    test.append(isselp.helpline)
            l = l + test 
        elif data['location'][0] != 'All States' and data['location'][1] == 'All Cities':
            test.clear()
            for isselp in avail.objects.all():
                if isselp.iss.issue in data['issues'] and isselp.helpline not in test:
                    test.append(isselp.helpline)
            helpline = helplines.objects.filter(state = data['location'][0])
            l = [value for value in helpline if value in test]
        else:
            test.clear()
            for isselp in avail.objects.all():
                if isselp.iss.issue in data['issues'] and isselp.helpline not in test:
                    test.append(isselp.helpline)
            helpline = helplines.objects.filter(city = data['location'][1])
            l = [value for value in helpline if value in test]
        
        if data['price'] != "All":
            test.clear()
            ref = []
            price = "None"
            for a in  helplines.objects.filter(cost = price):
                ref.append(a)
            if data['price'] == "Free":
                test = test + ref
            else:
                for a in helplines.objects.all():
                    if a.cost != price and a not in test:
                        test.append(a)
            l = [value for value in l if value in test]

        if data['orgtype'] != "All":
            test.clear()
            for a in  helplines.objects.filter(orgtype = data['orgtype']):
                test.append(a)
            l = [value for value in l if value in test]
        for a in l:
            issu.clear()
            for ap in avail.objects.filter(helpline=a):
                issu.append(ap.iss.issue)
            serializer = b(a)
            data1 = json.dumps(serializer.data)
            data2 = json.loads(data1)
            data2['number'] = data2['number'].split(",")
            data2['issues'] = list(issu)
            lst3.append(data2)
        return Response(lst3)        

class ReactView3(APIView):
    def post(self, request):
        data=request.data
        data['issues'] = ",".join(data['issues'])
        body = f"Name : {data['name']}\nPhone No. : {data['number']}\nEmail ID : {data['email']}\nIssues : {data['issues']}\nProblem Description : {data['aoi']}\nAnthing else : {data['anything']}"
        res = send_mail("Hello WIfi", body, "sidkakela@gmail.com", [data['email']])
        return Response(True)

class ReactView4(APIView):
    def post(self, request):
        data=request.data
        some = data['id']
        hl = helplines.objects.get(id = some)
        newfeed = feedback(rating = data['rating'],comment = data['comment'],frel = hl) 
        newfeed.save()
        return Response(True)

class ReactView5(APIView):
    def post(self, request):
        data=request.data
        issue7=""
        for a in data['issues']:
            issue7 += a+", "
        newfeed = verify(Issues=issue7,State=data['state'],City=data['city'],OrganizationAddress =data['add'],OrganizationName=data['name'],PhoneNumber=data['phone']) 
        newfeed.save()
        return Response(True)

'''intern stuff'''

class login_view(APIView):
    def post(self, request):
        data=request.data
        sid = User.objects.filter(username=data['name'])
        if len(sid) != 1:
            return Response(False)

        if not check_password(data["pass"], sid[0].password):
            return Response(False)
        else:
            l=[]
            request.session['name']=sid[0].id
            object = User.objects.get(id = sid[0].id)
            helplines = assignhelpline.objects.filter(intern = object)
            for a in helplines:
                Serializer = Dashboard(a.helpline)
                data = json.dumps(Serializer.data)
                data1 = json.loads(data)
                data1['PhoneNumber'] = data1['PhoneNumber'].split(',')
                if data1['VerificationStatus'] == True:
                    data1['VerificationStatus'] = "green"
                else:
                    data1['VerificationStatus'] = "red"
                l.append(data1)
            return Response(l)

class dashboard_internview(APIView):
    def post(self,request):
        l=[]
        data = request.data
        helplines = verify.objects.filter(id = data['id'])
        for a in helplines:
            Serializer = Dashboard(a)
            data = json.dumps(Serializer.data)
            data1 = json.loads(data)
            data1['PhoneNumber'] = data1['PhoneNumber'].split(',')
            if data1['VerificationStatus'] == True:
                data1['VerificationStatus'] = "green"
            else:
                data1['VerificationStatus'] = "red"
            l.append(data1)
        return Response(l[0])

class commentview(APIView):
    def get(self,request):
        C=[]
        data = request.data
        object = User.objects.get(id=request.session['name'] )
        object1 = comment.objects.get(id=1)
        commentsadimn = comment.objects.filter(intern = object)
        for a in commentsadimn:
            Serializer = Comments(a)
            data = json.dumps(Serializer.data)
            data1 = json.loads(data)
            C.append(data1)
        return Response(C)


class data_update_view(APIView):
    def post(self,request):
        data = request.data    
        if data['valid']!="True":
            data['valid'] = False
        verify.objects.filter(id=data['id']).update(OrganizationName=data['OrgName'], OrganizationAddress=data['orgadd'], PhoneNumber=data['phone'],City=data['city'], State=data['state'],Issues=data['issues'],OrganizationDescription=data['dis'],OrganizationType=data['type'],Email=data['email'],Website=data['web'],OperationalHours=data['hours'],isvalid=bool(data['valid']))
        return Response(True)

class logout1(APIView):
    def post(self,request):
        del request.session['name']
        return Response(True)

