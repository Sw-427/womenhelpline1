from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
	class Meta:
		model = React
		fields = ['name', 'detail']

class b(serializers.ModelSerializer):
	class Meta:
		model = helplines
		fields = ['number', 'address','description','state','city','date','orgtype','ophrs','email','cost','url','id','orgname']

class c(serializers.ModelSerializer):
	class Meta:
		model = issues
		fields = ['issue']

class Dashboard(serializers.ModelSerializer):
    class Meta:
        model = verify
        fields = ['OrganizationName','OrganizationAddress', 'PhoneNumber','City', 'State','Issues','OrganizationDescription','OrganizationType','Email','Website','OperationalHours','id','isvalid','VerificationStatus']

class Comments(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = [ 'comments','time']