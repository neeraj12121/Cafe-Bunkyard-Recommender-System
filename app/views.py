from .models import UserProfile, Menu, Ratings, UserRating
from django.shortcuts import render, redirect
from django.db.models import Max
from math import sqrt


def login(request):
    if request.method=='POST':
        username = request.POST['uname']
        password = request.POST['psw']
        user= UserProfile.objects.filter(username=username)
        if user is not None:
            print("exist")
            request.session['uname']=user[0].username
            request.session['userid']=user[0].userid
            userdict={'username':username, 'userid':1}
            print(userdict)
            return redirect('reco')
        else:
            print("doesnot exist")

    return render(request,"login.html")

def euclidean_dist(prefs, user1, user2):
    si = {}
    for item in prefs[user1]:
        if item in prefs[user2]: si[item] = 1

    if len(si) == 0:
        return 0

    sum_of_squares = sum([pow(prefs[user1][item] - prefs[user2][item], 2)
                          for item in prefs[user1] if item in prefs[user2]])

    return 1 / (1 + sqrt(sum_of_squares))

def jaccard(prefs, genre1, genre2):

    genre1_movies = prefs[genre1].keys()
    genre2_movies = prefs[genre2].keys()

    p1, p2 = set(genre1_movies), set(genre2_movies)
    p1_intersect_p2 = p1.intersection(p2)
    p1_union_p2 = p1.union(p2)

    p1_intersect_p2, p1_union_p2 = len(p1_intersect_p2), len(p1_union_p2)

    if p1_intersect_p2 == 0: return 0



def register(request):
    if request.method=='POST':
        name = request.POST['uname']
        passw = request.POST['psw']
        passw_rpt = request.POST['psw_repeat']
        print (name,passw,passw_rpt)
        if passw==passw_rpt:
            test = UserProfile.objects.filter(username=name)
            if UserProfile.objects.all():
                maxid = UserProfile.objects.all().aggregate(Max('userid'))
            else:
                maxid = Ratings.objects.all().aggregate(Max('userid'))
            if test:
                message = {'msg':"Already a user please try another username"}
                print ("already a user")
                return render(request,"register.html",message)
            else:
                print (maxid['userid__max'])
                user = UserProfile(userid=maxid['userid__max']+1,username=name,password=passw)
                user.save()
                return redirect('login')
        else:
            message = {'msg':"One of the passwords does not match"}
            return render(request,"register.html",message)

    return render(request,"register.html")

