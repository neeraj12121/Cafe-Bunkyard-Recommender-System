from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import FormView  
from app.models import menu
from django.shortcuts import render
from .forms import AddForm

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