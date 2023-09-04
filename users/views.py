from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test

from django.shortcuts import render
from noticeboard.models import NoticeBoard
# from users.models import CustomUser



def user_not_authenticated(user):
    print(user.is_authenticated)
    return not user.is_authenticated

@login_required
def logout(request):
    return render(request,'registration/logout.html')



@user_passes_test(user_not_authenticated, login_url='login/')
def login(request):
    if request.method == 'POST':
        # pdb.set_trace()
        return redirect('/')
    if user_not_authenticated() == True :
        return redirect('/')
    return render(request,'registration/login.html')



@login_required
def noticeboard(request):
    user = request.user
    if user.user_type == 'student':
        noticeboard_entries = NoticeBoard.objects.filter(user=user)
    elif user.user_type in ['student', 'teacher']:
        # For teachers and students
        noticeboard_entries = NoticeBoard.objects.filter(user__user_type__in=['student', 'teacher'])
    else:
        # For principal
        noticeboard_entries = NoticeBoard.objects.all()
    
    return render(request, 'noticeboard.html', {'noticeboard_entries': noticeboard_entries})







# def student_noticeboard(request):
#     students = CustomUser.objects.filter(user_type='student')
#     noticeboard_entries = NoticeBoard.objects.filter(user__in=students)
#     return render(request, 'student_noticeboard.html', {'noticeboard_entries': noticeboard_entries})

# def teacher_principal_noticeboard(request):
#     teachers_and_principals = CustomUser.objects.filter(user_type__in=['teacher', 'principal'])
#     noticeboard_entries = NoticeBoard.objects.filter(user__in=teachers_and_principals)
#     return render(request, 'teacher_principal_noticeboard.html', {'noticeboard_entries': noticeboard_entries})

