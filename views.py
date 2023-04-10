from django.shortcuts import render, redirect
from .forms import Booklogform
from .models import Booklog

def index(request):
    booklog=Booklog.objects.all().order_by('name')
    if request.method == 'POST':
        form = Booklogform(request.POST)
        if form.is_valid():
            form.save()
            form =Booklogform()
            return render(request, 'booklog/index.html', {'memo':'رديف افزوده شد', 'form': form , 'booklog': booklog , 'var1' : 2 })
        else:
            form =Booklogform()
            return render(request, 'booklog/index.html', {'memo':'خطا در ساخت رديف جديد', 'form': form , 'booklog': booklog , 'var1': 2 })
    else:
        form = Booklogform()
        return render(request, 'booklog/index.html', {'form': form , 'booklog': booklog ,  'var1' : 2  })

def editlog(request):
    booklog=Booklog.objects.all().order_by('name')
    if request.method == 'POST':
        idx = request.POST['idnum']
        ins1=Booklog.objects.get(id = idx)
        form =Booklogform(request.POST ,instance = ins1  )
        if form.is_valid():            
            form.save()
            form =Booklogform()
            return render(request, 'booklog/index.html', {'memo': 'ویرایش انجام شد' , 'form': form , 'booklog': booklog , 'var1' : 2 })
        else:
            form =Booklogform()
            return render(request, 'booklog/index.html', {'memo': 'خطا در ویرایش کاربر', 'form': form , 'booklog': booklog , 'var1': 2 })
    else:
        idx = request.GET['id']
        ins1=Booklog.objects.get(id = idx)
        form =Booklogform(instance = ins1)
        return render(request, 'booklog/index.html', {'form': form , 'idx': idx ,'booklog': booklog  , 'var1' : 3  })

def deletelog(request):
    try:
        if request.method == 'GET':
            idx = request.GET['id']
            Booklog.objects.get(id=request.GET['id']).delete()
    except:
        pass
    return redirect("/booklog")
    
