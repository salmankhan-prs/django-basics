from django.shortcuts import render
from .models import ChaiVariety,Store
from .forms import ChaiVarietyForms
# Create your views here.

def all_chai(request):
   chais = ChaiVariety.objects.all()   
   return render(request,'chai/all_chai.html',{'chais':chais})


def get_chai_details_by_id(request,chai_id):
   
   chai = ChaiVariety.objects.get(id=chai_id)
  
   return render(request,'chai/details_chai.html',{'chai':chai})

   
   
def chai_store_view(request):
   stores = None
   if request.method == "POST":
       form = ChaiVarietyForms(request.POST)
       
       if form.is_valid():
         chai_variety =  form.cleaned_data['chai_variety']
         stores = Store.objects.filter(chai_varieties__in=chai_variety)
   else:
      form = ChaiVarietyForms()
   return render(request,'chai/chai_stores.html',{'stores':stores,'form':form})
