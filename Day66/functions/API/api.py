from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.views.generic import TemplateView
import requests
import json


class testApi(APIView):
	permissions_classes = [IsAuthenticated]
	authentication_class = [TokenAuthentication]

	self.data = {
		0: 'Bogdan',
		1: 'Claudia',
		2: 'Andra',
		3: 'xD'
	}

	def get(self, request, slug=None)
		if sluf != None:
			data = self.data[slug]
		else:
			data = self.data
		return Response(json(data))

	def put(self, request, slug)
		if slug not in self.data:
			self.data[slug] = request.data
			message = 200
		else:
			message = 404

		return Response(status=message)

	def delete(self, request, slug):
		try:
			self.data.remove[slug]
		except:
			return Response(status=404)
