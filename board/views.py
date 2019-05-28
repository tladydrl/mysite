from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from board.models import Board


def index(request):
    return render(request, 'board/list.html')


def create(request):
    board = Board()
    board.title = 'test'
    board.content = 'test'
    board.user_id = 1

    board.save()

    return HttpResponse('ok')


def read(request):
    board_list = Board.objects.all()
    for board in board_list:
        print(board.id, board.title, board.user)

    return HttpResponse('ok')
