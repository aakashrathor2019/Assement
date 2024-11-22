from django.shortcuts import render, redirect
from django.views import View
from .models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class Login(View):
    def get(self, request):
        # Render the login page for GET requests
        return render(request, "login.html")

    def post(self, request):
        # Handle login logic for POST requests
        username = request.POST.get("emp_name")
        password = request.POST.get("emp_pass")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("show_emp")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

class Add_Emp(View):
    def get(self, request):
        return render(request, 'add_emp.html')

    def post(self, request):
        emp_img = request.FILES.get("emp_img")
        emp_name = request.POST.get("emp_name")
        emp_email = request.POST.get("emp_email")
        emp_dept = request.POST.get("emp_dept")
        emp_add = request.POST.get("emp_add")
        emp_pass =request.POST.get("emp_pass")
        emp=Employee.objects.filter(emp_email=emp_email)
        print('DATA IS-->>',emp_name,emp_add,emp_dept,emp_email,emp_img)
        if emp_add and emp_dept and emp_email and emp_img and emp_name:
             
                user = User.objects.create(
                    username=emp_name,
                    email=emp_email
                )
                if user:
                    user.set_password(emp_pass)
                    user.save()
                emp_data = Employee.objects.create(
                    emp_img=emp_img,
                    emp_name=emp_name,
                    emp_email=emp_email,
                    emp_dept=emp_dept,
                    emp_add=emp_add,
                )
                if emp_data:
                    return redirect('show_emp')
        return render(request, 'add_emp.html', {'errors': 'Invalid Credentials'})


class Show_Emp(View,LoginRequiredMixin):
    login_url='login/'
    def get(self, request):
        emp_data = Employee.objects.all()
        print('ALL Data:',emp_data)
        return render(request, 'show_emp.html', {'emp_data': emp_data})


class Do_Update(View,LoginRequiredMixin):
    login_url='login/'
    def get(self, request, emp_id):
        try:
            emp = Employee.objects.get(pk=emp_id)
            print('DATA:',emp.id)
            return render(request, "update.html", {"emp": emp})
        except Employee.DoesNotExist:
            return render(request, "show_emp.html", {"error": "Invalid Employee ID"})

    def post(self, request, emp_id):
        emp_img = request.FILES.get("emp_img")
        emp_name = request.POST.get("emp_name")
        emp_email = request.POST.get("emp_email")
        emp_dept = request.POST.get("emp_dept")
        emp_add = request.POST.get("emp_add")
        print('DATA IS-->>',emp_name,emp_add,emp_dept,emp_email,emp_img)
        try:
            emp = Employee.objects.get(id=emp_id)
            if emp_img:
                emp_img=emp_img
            else:
                emp_img=emp.emp_img
                
            emp.emp_img = emp_img
            emp.emp_name = emp_name
            emp.emp_email = emp_email
            emp.emp_add = emp_add
            emp.emp_dept = emp_dept
            emp.save()
            return redirect("show_emp")
        except Employee.DoesNotExist:
            return render(request, "show_emp.html", {"error": "Invalid Employee ID"})



class Delete_Emp(View,LoginRequiredMixin):
    login_url='login/'
    def get(self, request, emp_id):
        try:            
            del_emp = Employee.objects.get(pk=emp_id)     
            del_emp.delete()
            print('Deleted employee:', del_emp)
            return redirect('show_emp')  
            
        except Employee.DoesNotExist:
            return render(request, "show_emp.html", {"error": "Employee not found."})
        except Exception as e:
            print(f"Error: {e}")
            return render(request, "show_emp.html", {"error": "An error occurred while deleting the employee."})

         

class Logout(View,LoginRequiredMixin):
    login_url='login/'
    def get(self,request):
        logout(request)
        return redirect('login')
