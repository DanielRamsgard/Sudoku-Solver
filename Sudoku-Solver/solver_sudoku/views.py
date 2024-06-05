from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import copy
# from django.contrib.auth.decorators import login_required
from .sudoku import solve_and_check
from .models import Solutions

# Create your views here.
# 
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def solve(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            array = data.get('array', [])
            copy_array = copy.deepcopy(array)
            obj = Solutions.objects.filter(input_sudoku=array).first()
            # if we do not get a valid board from the PostgreSQL DB
            if obj is None:
                ret, board = solve_and_check(array)
                if ret:
                    Solutions(input_sudoku=copy_array, solution_sudoku=board).save()
                    
            # if we get a valid board from DB
            elif obj is not None:
                board = obj.solution_sudoku
                ret = True
                return JsonResponse({'board': board, 'ret': ret})
            
            # check ret
            if ret:
                return JsonResponse({'board': board, 'ret': ret})
            
            # return initial board if not solution
            else:
                return JsonResponse({'board': board, 'ret': ret})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'})
    return JsonResponse({'error': 'Invalid Method'})
