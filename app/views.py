from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import FormView  
from app.models import menu
from django.shortcuts import render
from .forms import AddForm
from math import sqrt




# def import_sheet(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST,request.FILES)
#         if form.is_valid():
#             request.FILES['file'].save_to_database(name_columns_by_row=2,model=Question,
#                                                    mapdict=['question_text', 'pub_date', 'slug'])
#             return HttpResponse("OK")
#         else:
#             return HttpResponseBadRequest()


def add(request):
    catagoryryname=menu.objects.all()
    cname=request.POST.get('dropdownl')
    if request.method == 'GET':
        form = AddForm()
    else:
        catagory = menu.objects.get(cname=cname)
        catagory.delete()

    return render(request, 'base.html', {'form':form, 'catagoryryname': catagoryryname})



def euclidean_dist(prefs, user1, user2):
    si = {}
    for item in prefs[user1]:
        if item in prefs[user2]: si[item] = 1

    if len(si) == 0:
        return 0

    sum_of_squares = sum([pow(prefs[user1][item] - prefs[user2][item], 2)
                          for item in prefs[user1] if item in prefs[user2]])

    return 1 / (1 + sqrt(sum_of_squares))

def jacard(prefs, genre1, genre2):

    genre1_movies = prefs[genre1].keys()
    genre2_movies = prefs[genre2].keys()

    p1_intersect_p2, p1_union_p2 = len(p1_intersect_p2), len(p1_union_p2)

    if p1_intersect_p2 == 0: return 0




