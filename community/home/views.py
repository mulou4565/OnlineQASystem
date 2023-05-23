from django.shortcuts import redirect

# Create your views here.
def home(request):
    """网站首页
    问题列表页
    """
    return redirect('questions:questions_list')