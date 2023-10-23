from django.shortcuts import render, redirect
from .models import Class, Enrollment
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import RegistrationForm
from django.db.models import F, Subquery, OuterRef
from django.contrib import messages

@login_required
def class_list(request):
    open_classes = Class.objects.filter(class_status='open')
    return render(request, 'enrollment/class_list.html', {'open_classes': open_classes})

@login_required
def enroll_class(request, class_code):
    try:
        selected_class = Class.objects.get(class_code=class_code, class_status='open')
        enrollment_count = selected_class.enrollment_set.count()
        if enrollment_count < selected_class.class_max_enroll:
            if request.user.is_authenticated:
                user = request.user

                if Enrollment.objects.filter(student=user, enrolled_class=selected_class).exists():
                    messages.warning(request, 'You are already enrolled in this class.')
                    return redirect('enrolled_classes')

                enrollment = Enrollment.objects.create(student=request.user, enrolled_class=selected_class)
                enrollment.save()

                messages.success(request, 'You have successfully enrolled in this class.')
                return redirect('enrolled_classes')
            else:
                return redirect('login')
        else:
            return render(request, 'enrollment/class_full.html')
    except Class.DoesNotExist:
        raise Http404("Class does not exist or is closed.")
    
@login_required
def enrolled_classes(request):
    enrolled_classes = Enrollment.objects.filter(student=request.user)
    return render(request, 'enrollment/enrolled_classes.html', {'enrolled_classes': enrolled_classes})

@login_required
def unenroll_class(request, class_code):
    try:
        selected_class = Class.objects.get(class_code=class_code)
        enrollment = Enrollment.objects.get(student=request.user, enrolled_class=selected_class)
        enrollment.delete()
        messages.success(request, 'You have successfully unenrolled from this class.')
        return redirect('enrolled_classes')
    except Enrollment.DoesNotExist:
        raise Http404("You are not enrolled in this class.")
    except Class.DoesNotExist:
        raise Http404("Class does not exist.")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'enrollment/register.html', {'form': form})
