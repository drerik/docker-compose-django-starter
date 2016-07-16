from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import serializers

from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

from members.models import Member
from members.auth import StaticTokenAuth

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        #fields = ("first_name", "last_name", "email")
        fields = '__all__'


class MemberList(APIView):

    #authentication_classes = [StaticTokenAuth,]


    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)


    def post(self, request):
        data = JSONParser().parse(BytesIO(request.body))
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            member = serializer.save()
            new_serializer = MemberSerializer(member)
            return Response(new_serializer.data)
        return Response(serializer.errors, status=401)


class MemberView(APIView):

    def get(self, request, member_id):
        try:
            member = Member.objects.get(id=member_id)
        except:
            LOG.error('Tried to get invalid member %s, exits with 404.', member_id)
            return Response(status=404)
        serializer = MemberSerializer(member)
        return Response(serializer.data)
