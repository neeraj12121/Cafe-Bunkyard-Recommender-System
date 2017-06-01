from .models import UserProfile, Menu, Ratings, UserRating
from django.shortcuts import render, redirect
from django.db.models import Max
from math import sqrt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Service




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
def pearson_correlation(data, person1, person2):

    shared_items = {}
    for item in data[person1]:
        if item in data[person2]:
            shared_items[item] = 1

    # number of elements
    n = len(shared_items)

    # no ratings in common
    if n == 0:
        return 0

    n = float(n)

    # adding up all preferences
    sum1 = sum([data[person1][item] for item in shared_items])
    sum2 = sum([data[person2][item] for item in shared_items])

    # summing up squares
    sum_sq1 = sum([pow(data[person1][item], 2) for item in shared_items])
    sum_sq2 = sum([pow(data[person2][item], 2) for item in shared_items])

    # summing products
    p_sum = sum([data[person1][item] * data[person2][item] for item in shared_items])

    # Pearson
    num = p_sum - (sum1 * sum2 / n)
    den = sqrt((sum_sq1 - pow(sum1, 2) / n) * (sum_sq2 - pow(sum2, 2) / n))

    # avoid dividing by 0
    if den == 0:
        return 0

    ret_val = num/den

    return ret_val


def get_default_recommendations(data, person, similarity):
    totals = {}
    similarity_sums = {}
    for other in data:
        # skip myself
        if other == person:
            continue

        sim = similarity(data, person, other)
        # ignore zero or negative correlations
        if sim <= 0:
            continue

        for item in data[other]:
            # score movies person hasn't seen yet
            if item not in data[person] or data[person][item] == 0:
                # similarity * score
                totals.setdefault(item, 0)
                totals[item] += data[other][item] * sim
                # sum of similarities
                similarity_sums.setdefault(item, 0)
                similarity_sums[item] += sim

        # normalised list
        rankings = [(total / similarity_sums[item], item) for item, total in totals.items()]
        rankings.sort()
        rankings.reverse()
        return rankings

def jaccard(prefs, genre1, genre2):

    genre1_movies = prefs[genre1].keys()
    genre2_movies = prefs[genre2].keys()

    p1, p2 = set(genre1_movies), set(genre2_movies)
    p1_intersect_p2 = p1.intersection(p2)
    p1_union_p2 = p1.union(p2)

    p1_intersect_p2, p1_union_p2 = len(p1_intersect_p2), len(p1_union_p2)

    if p1_intersect_p2 == 0: return 0

def pearson_default_recommendation(data, person):
    return get_default_recommendations(data, person, similarity=pearson_correlation)


def euclid_default_recommendation(data, person):
    return get_default_recommendations(data, person, similarity=similarity_distance)

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

def profile(request, user_id):
    if request.method == 'GET':
        response = {}
        message = 'no'
        user = get_object_or_404(User, pk=user_id)
        if user is not None:
            message = 'ok'
            list_of_services = []
            services = Service.objects.filter(user=user)
            for service in services:
                serializer = ServiceSerializer(service)
                list_of_services.append(serializer.data)

            response['services'] = list_of_services

        response['message'] = message
        return JsonResponse(response)