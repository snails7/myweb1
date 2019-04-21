from django.shortcuts import render, redirect, reverse
from django.db import connection


# Create your views here.

def get_corsor():
    return connection.cursor()

def index(request):

    cursor = get_corsor()
    cursor.execute("select id, name, author from pet")
    books = cursor.fetchall()
    print(books)


    return render(request, 'index.html', context={"books":books})