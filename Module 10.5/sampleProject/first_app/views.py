from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
  data = {
    'SL' : 1, 'Name' : 'rahim', 'description': "I'm Rahim" ,'age' : 20, 'joining_date' : datetime.datetime.now(), 'about' : '',

    'lst' : [
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
    ],

    'book_size' : '123456789',
    'list' : ['a', 'b', 'c', 'd', 'e'],

    'num_list' : [
      'one',
      'two',
      'three'
    ],

  }

  return render(request, 'index.html', {'data' : data},)
