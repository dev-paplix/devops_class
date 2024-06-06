from django.shortcuts import render
from DockerDevops.models import Staffs
from rest_framework.views import APIView
from rest_framework import views, permissions, status
from rest_framework.response import Response
from django.http import JsonResponse


class add_name(views.APIView):

    def post(self, request, *args, **kwargs):

        data = request.data
        name = data.get("name")

        new_name = Staffs(name=name)
        new_name.save()
        return Response({'message': 'Name Saved'}, status=200)
    
class saved_names(views.APIView):

    def get(self, request):

        all = Staffs.objects.all()
        savedNames = []

        for name in all:
            n_id = name.id
            p_name = name.name

            

            p_data = {
                "id": n_id,
                "saved_names": "The New Student Name is: " + p_name,
                
            }
            savedNames.append(p_data)

        response_data = {
            "data": savedNames
            }
        return JsonResponse(response_data, status=200)