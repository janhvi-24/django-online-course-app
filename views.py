from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Logic to extract selected choices and create Submission
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=new_sub.id)
    return render(request, 'onlinecourse/exam_registration.html', {'course': course})

def show_exam_result(request, course_id, submission_id):
    context = {}
    # Logic to calculate score and determine 'Congratulations' status
    return render(request, 'onlinecourse/exam_result.html', context)
