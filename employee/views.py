from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import EmployeeForm
from .models import Employee


def employee_list(request):
       employees = Employee.objects.all()
       return render(request, 'employee/employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('employee_list')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form})
