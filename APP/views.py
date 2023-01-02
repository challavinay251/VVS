from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from APP.models import four_1


# Create your views here.
def timetablefour_1(request):
    sublist = four_1.objects.all()
    dict1 = {'sublist': sublist}
    return render(request, 'APP/four_1.html', context=dict1);

from django.shortcuts import render
from APP.models import three_1
# Create your views here.
def timetablethree_1(request):
    sublist = three_1.objects.all()
    dict1 = {'sublist': sublist}
    return render(request, 'APP/three_1.html', context=dict1);

from django.shortcuts import render
from APP.models import two_1
# Create your views here.
def timetabletwo_1(request):
    sublist = two_1.objects.all()
    dict1 = {'sublist': sublist}
    return render(request, 'APP/two_1.html', context=dict1);

from django.shortcuts import render
from APP.models import one_1_a
# Create your views here.
def timetableone_1_a(request):
    sublist = one_1_a.objects.all()
    dict1 = {'sublist': sublist}
    return render(request, 'APP/one_1_a.html', context=dict1);

from django.shortcuts import render
from APP.models import one_1_b
# Create your views here.
def timetableone_1_b(request):
    sublist = one_1_b.objects.all()
    dict1 = {'sublist': sublist}
    return render(request, 'APP/one_1_b.html', context=dict1);

from django.shortcuts import render
from APP.models import four_2
# Create your views here.
def timetablefour_2(request):
    sublist = four_2.objects.all()
    dict1 = {'sublist': sublist}
    return render(request, 'APP/four_2.html', context=dict1);

from django.shortcuts import render
from APP.models import three_2
# Create your views here.
def timetablethree_2(request):
    sublist = three_2.objects.all()
    dict1 = {'sublist': sublist}
    return render(request, 'APP/three_2.html', context=dict1);

from django.shortcuts import render
from APP.models import two_2
# Create your views here.
def timetabletwo_2(request):
    sublist = two_2.objects.all()
    dict1 = {'sublist': sublist}
    return render(request, 'APP/two_2.html', context=dict1);

from django.shortcuts import render
from APP.models import one_2_a
# Create your views here.
def timetableone_2_a(request):
    sublist = one_2_a.objects.all()
    dict1 = {'sublist': sublist}
    return render(request, 'APP/one_2_a.html', context=dict1);

from django.shortcuts import render
from APP.models import one_2_b
# Create your views here.
def timetableone_2_b(request):
    sublist = one_2_b.objects.all()
    dict1 = {'sublist': sublist}
    return render(request, 'APP/one_2_b.html', context=dict1);


def student(request):
    return render(request, 'App/student.html');

def select(request):
    return render(request, 'APP/select.html')

def faculty(request):
    return render(request, 'APP/faculty.html')

def saithirumal(request):
    return render(request, 'APP/saithirumal.html')

def naveen(request):
    return render(request, 'APP/naveen.html')

def narender(request):
    return render(request, 'APP/narender.html')

def babu(request):
    return render(request, 'APP/babu.html')

def subhan(request):
    return render(request, 'APP/subhan.html')

def subharao(request):
    return render(request, 'APP/subharao.html')

def santhosh(request):
    return render(request, 'APP/santhosh.html')

def sandeep(request):
    return render(request, 'APP/sandeep.html')

def zulfiquar(request):
    return render(request, 'APP/zulfiquar.html')

def cassian(request):
    return render(request, 'APP/cassian.html')

def devaraj(request):
    return render(request, 'APP/devaraj.html')

def anil(request):
    return render(request, 'APP/anil.html')

def venkat(request):
    return render(request, 'APP/venkat.html')

from django.shortcuts import render
from APP.models import Saithirumal_1_1_a
#Create your views here.
def timetableSaithirumal_1_1_a(request):
  sublist= Saithirumal_1_1_a.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/saithirumal_1_1_a.html', context=dict1);


from django.shortcuts import render
from APP.models import Saithirumal_1_1_b
#Create your views here.
def timetableSaithirumal_1_1_b(request):
  sublist= Saithirumal_1_1_b.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/saithirumal_1_1_b.html', context=dict1);

from django.shortcuts import render
from APP.models import Saithirumal_2_1
#Create your views here.
def timetableSaithirumal_2_1(request):
  sublist= Saithirumal_2_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/saithirumal_2_1.html', context=dict1);

from django.shortcuts import render
from APP.models import Saithirumal_2_2
#Create your views here.
def timetableSaithirumal_2_2(request):
  sublist= Saithirumal_2_2.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/saithirumal_2_2.html', context=dict1);



from django.shortcuts import render
from APP.models import Naveen_1_2_a
#Create your views here.
def timetableNaveen_1_2_a(request):
  sublist=Naveen_1_2_a.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/naveen_1_2_a.html', context=dict1);

from django.shortcuts import render
from APP.models import Naveen_1_2_b
#Create your views here.
def timetableNaveen_1_2_b(request):
  sublist=Naveen_1_2_b.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/naveen_1_2_b.html', context=dict1);

from django.shortcuts import render
from APP.models import Naveen_2_1
#Create your views here.
def timetableNaveen_2_1(request):
  sublist=Naveen_2_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/naveen_2_1.html', context=dict1);


from django.shortcuts import render
from APP.models import Devaraj_3_1
#Create your views here.
def timetableDevaraj_3_1(request):
  sublist=Devaraj_3_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/devaraj_3_1.html', context=dict1);

from django.shortcuts import render
from APP.models import Santhosh_3_1
#Create your views here.
def timetableSanthosh_3_1(request):
  sublist=Santhosh_3_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/santhosh_3_1.html', context=dict1);


from django.shortcuts import render
from APP.models import Santhosh_3_2
#Create your views here.
def timetableSanthosh_3_2(request):
  sublist=Santhosh_3_2.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/santhosh_3_2.html', context=dict1);


from django.shortcuts import render
from APP.models import Anil_3_1
#Create your views here.
def timetableAnil_3_1(request):
  sublist=Anil_3_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/anil_3_1.html', context=dict1);

from django.shortcuts import render
from APP.models import Anil_3_2
#Create your views here.
def timetableAnil_3_2(request):
  sublist=Anil_3_2.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/anil_3_2.html', context=dict1);

from django.shortcuts import render
from APP.models import Anil_4_1
#Create your views here.
def timetableAnil_4_1(request):
  sublist=Anil_4_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/anil_4_1.html', context=dict1);

from django.shortcuts import render
from APP.models import Subharao_1_1_a
#Create your views here.
def timetableSubharao_1_1_a(request):
  sublist=Subharao_1_1_a.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/subharao_1_1_a.html', context=dict1);

from django.shortcuts import render
from APP.models import Subharao_1_1_b
#Create your views here.
def timetableSubharao_1_1_b(request):
  sublist=Subharao_1_1_b.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/subharao_1_1_b.html', context=dict1);

from django.shortcuts import render
from APP.models import Subharao_2_1
#Create your views here.
def timetableSubharao_2_1(request):
  sublist=Subharao_2_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/subharao_2_1.html', context=dict1);

from django.shortcuts import render
from APP.models import Subharao_3_1
#Create your views here.
def timetableSubharao_3_1(request):
  sublist=Subharao_3_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/subharao_3_1.html', context=dict1);

from django.shortcuts import render
from APP.models import Subharao_3_2
#Create your views here.
def timetableSubharao_3_2(request):
  sublist=Subharao_3_2.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/subharao_3_2.html', context=dict1);

from django.shortcuts import render
from APP.models import Cassian_1_2_a
#Create your views here.
def timetableCassian_1_2_a(request):
  sublist=Cassian_1_2_a.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/cassian_1_2_a.html', context=dict1);


from django.shortcuts import render
from APP.models import Cassian_1_2_b
#Create your views here.
def timetableCassian_1_2_b(request):
  sublist=Cassian_1_2_b.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/cassian_1_2_b.html', context=dict1);


from django.shortcuts import render
from APP.models import Babu_2_1
#Create your views here.
def timetableBabu_2_1(request):
  sublist=Babu_2_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/babu_2_1.html', context=dict1);

from django.shortcuts import render
from APP.models import Babu_2_2
#Create your views here.
def timetableBabu_2_2(request):
  sublist=Babu_2_2.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/babu_2_2.html', context=dict1);


from django.shortcuts import render
from APP.models import Babu_3_1
#Create your views here.
def timetableBabu_3_1(request):
  sublist=Babu_3_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/babu_3_1.html', context=dict1);

from django.shortcuts import render
from APP.models import Babu_3_2
#Create your views here.
def timetableBabu_3_2(request):
  sublist=Babu_3_2.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/babu_3_2.html', context=dict1);

from django.shortcuts import render
from APP.models import Babu_4_1
#Create your views here.
def timetableBabu_4_1(request):
  sublist=Babu_4_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/babu_4_1.html', context=dict1);


from django.shortcuts import render
from APP.models import Zulfiquar_1_1_a
#Create your views here.
def timetableZulfiquar_1_1_a(request):
  sublist=Zulfiquar_1_1_a.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/zulfiquar_1_1_a.html', context=dict1);

from django.shortcuts import render
from APP.models import Zulfiquar_1_1_b
#Create your views here.
def timetableZulfiquar_1_1_b(request):
  sublist=Zulfiquar_1_1_b.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/zulfiquar_1_1_b.html', context=dict1);


from django.shortcuts import render
from APP.models import Zulfiquar_1_2_a
#Create your views here.
def timetableZulfiquar_1_2_a(request):
  sublist=Zulfiquar_1_2_a.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/zulfiquar_1_2_a.html', context=dict1);


from django.shortcuts import render
from APP.models import Zulfiquar_1_2_b
#Create your views here.
def timetableZulfiquar_1_2_b(request):
  sublist=Zulfiquar_1_2_b.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/zulfiquar_1_2_b.html', context=dict1);

from django.shortcuts import render
from APP.models import Zulfiquar_2_1
#Create your views here.
def timetableZulfiquar_2_1(request):
  sublist=Zulfiquar_2_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/zulfiquar_2_1.html', context=dict1);


from django.shortcuts import render
from APP.models import Venkat_1_1_a
#Create your views here.
def timetableVenkat_1_1_a(request):
  sublist=Venkat_1_1_a.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/venkat_1_1_a.html', context=dict1);

from django.shortcuts import render
from APP.models import Venkat_1_1_b
#Create your views here.
def timetableVenkat_1_1_b(request):
  sublist=Venkat_1_1_b.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/venkat_1_1_b.html', context=dict1);


from django.shortcuts import render
from APP.models import Venkat_1_2_a
#Create your views here.
def timetableVenkat_1_2_a(request):
  sublist=Venkat_1_2_a.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/venkat_1_2_a.html', context=dict1);

from django.shortcuts import render
from APP.models import Venkat_1_2_b
#Create your views here.
def timetableVenkat_1_2_b(request):
  sublist=Venkat_1_2_b.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/venkat_1_2_b.html', context=dict1);

from django.shortcuts import render
from APP.models import Narender_1_1_a
#Create your views here.
def timetableNarender_1_1_a(request):
  sublist=Narender_1_1_a.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/narender_1_1_a.html', context=dict1);


from django.shortcuts import render
from APP.models import Narender_1_1_b
#Create your views here.
def timetableNarender_1_1_b(request):
  sublist=Narender_1_1_b.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/narender_1_1_b.html', context=dict1);


from django.shortcuts import render
from APP.models import Narender_4_1
#Create your views here.
def timetableNarender_4_1(request):
  sublist=Narender_4_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/narender_4_1.html', context=dict1);



from django.shortcuts import render
from APP.models import Subhan_3_1
#Create your views here.
def timetableSubhan_3_1(request):
  sublist=Subhan_3_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/subhan_3_1.html', context=dict1);


from django.shortcuts import render
from APP.models import Subhan_3_2
#Create your views here.
def timetableSubhan_3_2(request):
  sublist=Subhan_3_2.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/subhan_3_2.html', context=dict1);



from django.shortcuts import render
from APP.models import Subhan_4_1
#Create your views here.
def timetableSubhan_4_1(request):
  sublist=Subhan_4_1.objects.all()
  dict1={'sublist':sublist}
  return render(request, 'APP/subhan_4_1.html', context=dict1);

