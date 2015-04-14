from django.shortcuts import render
from student.models import Member
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
	title="Index"
	return render(request,'layout/index.html',{'pagename':title})

def home(request):
	title="Home"
	myname="kk"
	return render(request,'layout/home.html',{'title':title,'name':myname})

def addstudent(request):
	title="Add student"
	return render(request,'site/addstudent.html',{'title':title})


def register(request):
	if request.method=="POST":
		sname=request.POST.get("sname",False)
		rno=request.POST.get("rno",False)
		branch=request.POST.get("branch",False)
		email=request.POST.get("email",False)
		m = Member()
		m.name=sname
		m.rno=rno
		m.branch=branch
		m.email=email
		m.save()
		print "Member has been recorded"
		return HttpResponseRedirect('/addstudent/')

def search(request):
	return render(request,'site/search.html')

def searchStudent(request):
	if request.method=="POST":
		roll_no=request.POST.get("rno",False)
		m=Member()
		m=Member.objects.all().filter(rno=roll_no)
		t=[]
		for item in m:
			t=item
		return render(request,'site/showStudentInfo.html',{'member':t})