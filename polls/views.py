from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import AuthorSerializer, BookSerializer
from .models import authorModel, bookModel
from django.http import JsonResponse

# Create your views here.


class getallAuthor(APIView):
    def get(self, request):
        all=authorModel.objects.all()
        serializer = AuthorSerializer(all, many=True)
        return Response(serializer.data)
    
class getallbooks(APIView):
    def get(self, request, *args, **kwargs):
        all=bookModel.objects.all()
        serializer = BookSerializer(all, many=True)
        return Response(serializer.data)
    

    # authorni ID sini yuborganda kitoblarini chiqarib berish uchun buyam bitta usul :)
# class getallBook(APIView):
#     def get(self, request, *args, **kwargs):
#         all=bookModel.objects.all()
#         fornow=[]
#         print("x")
#         for i in all:
#             if i.author.id==kwargs['forid']:
#                 fornow.append({
#                 "name":i.name,
#                 "page":i.page,
#                 "year_of_invented":i.year_of_invented
#             })
#         return JsonResponse(fornow, safe=False)

class getAuthorID(APIView):
    def get(self, request, *args, **kwargs):
        all=bookModel.objects.filter(author=kwargs['forid'])
        serializer = BookSerializer(all, many=True)
        return Response(serializer.data)
    

class postBook(APIView):
    def post(self, request):
        serializer=bookModel(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    
class patchBook(APIView):
    def patch(self, request, *args, **kwargs):
        x=get_object_or_404(bookModel, id=kwargs['forid'])
        serializer=BookSerializer(x, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class putBook(APIView):
    def put(self, request, *args, **kwargs):
        x=get_object_or_404(bookModel, id=kwargs['forid'])
        serializer=BookSerializer(x, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class deleteBook(APIView):
    def delete(self, request, *args, **kwargs):
        x=get_object_or_404(bookModel, id=kwargs['forid'])
        x.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class postAuthor(APIView):
    def post(self, request):
        serializer=AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    
class patchAuthor(APIView):
    def patch(self, request, *args, **kwargs):
        x=get_object_or_404(authorModel, id=kwargs['forid'])
        serializer=AuthorSerializer(x, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class putAuthor(APIView):
    def put(self, request, *args, **kwargs):
        x=get_object_or_404(authorModel, id=kwargs['forid'])
        serializer=AuthorSerializer(x, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class deleteAuthor(APIView):
    def delete(self, request, *args, **kwargs):
        x=get_object_or_404(authorModel, id=kwargs['forid'])
        x.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    


    
