"""VVS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timetable/', views.select),
    path('student/', views.student),
	path('faculty/', views.faculty),
	path('four_1/',views.timetablefour_1),
	path('three_1/',views.timetablethree_1),
	path('two_1/',views.timetabletwo_1),
	path('one_1_a/',views.timetableone_1_a),
	path('one_1_b/',views.timetableone_1_b),
	path('four_2/',views.timetablefour_2),
	path('three_2/',views.timetablethree_2),
	path('two_2/',views.timetabletwo_2),
	path('one_2_a/',views.timetableone_2_a),
	path('one_2_b/',views.timetableone_2_b),
	path('saithirumal/',views.saithirumal),
    path('naveen/',views.naveen),
    path('narender/',views.narender),
	path('babu/', views.babu),
    path('subhan/', views.subhan),
    path('subharao/', views.subharao),
    path('santhosh/', views.santhosh),
    path('sandeep/', views.sandeep),
    path('cassian/', views.cassian),
    path('devaraj/', views.devaraj),
    path('anil/', views.anil),
    path('zulfiquar/', views.zulfiquar),
    path('venkat/', views.venkat),
    path('saithirumal_1_1_a/',views.timetableSaithirumal_1_1_a),
    path('saithirumal_1_1_b/',views.timetableSaithirumal_1_1_b),
    path('saithirumal_2_1/',views.timetableSaithirumal_2_1),
    path('saithirumal_2_2/',views.timetableSaithirumal_2_2),
    path('subharao_1_1_a/', views.timetableSubharao_1_1_a),
    path('subharao_1_1_b/', views.timetableSubharao_1_1_b),
    path('subharao_2_1/', views.timetableSubharao_2_1),
    path('subharao_3_2/', views.timetableSubharao_3_2),
    path('subharao_3_1/', views.timetableSubharao_3_1),
    path('cassian_1_2_a/',views.timetableCassian_1_2_a),
    path('cassian_1_2_b/',views.timetableCassian_1_2_b),
    path('narender_1_1_a/', views.timetableNarender_1_1_a),
    path('narender_1_1_b/', views.timetableNarender_1_1_b),
    path('narender_4_1/', views.timetableNarender_4_1),
    path('babu_2_1/', views.timetableBabu_2_1),
    path('babu_2_2/', views.timetableBabu_2_2),
    path('babu_3_1/', views.timetableBabu_3_1),
    path('babu_3_2/', views.timetableBabu_3_2),
    path('babu_4_1/', views.timetableBabu_4_1),
    path('anil_3_1/', views.timetableAnil_3_1),
    path('anil_3_2/', views.timetableAnil_3_2),
    path('anil_4_1/', views.timetableAnil_4_1),
    path('devaraj_3_1/', views.timetableDevaraj_3_1),
    path('naveen_1_2_a/', views.timetableNaveen_1_2_a),
    path('naveen_1_2_b/', views.timetableNaveen_1_2_b),
    path('naveen_2_1/', views.timetableNaveen_2_1),
    path('santhosh_3_1/', views.timetableSanthosh_3_1),
    path('santhosh_3_2/', views.timetableSanthosh_3_2),
    path('subhan_3_1/', views.timetableSubhan_3_1),
    path('subhan_3_2/', views.timetableSubhan_3_2),
    path('subhan_4_1/', views.timetableSubhan_4_1),
    path('venkat_1_1_a/', views.timetableVenkat_1_1_a),
    path('venkat_1_1_b/', views.timetableVenkat_1_1_b),
    path('venkat_1_2_a/', views.timetableVenkat_1_2_a),
    path('venkat_1_2_b/', views.timetableVenkat_1_2_b),
    path('zulfiquar_2_1/', views.timetableZulfiquar_2_1),
    path('zulfiquar_1_1_a/', views.timetableZulfiquar_1_1_a),
    path('zulfiquar_1_1_b/', views.timetableZulfiquar_1_1_b),
    path('zulfiquar_1_2_a/', views.timetableZulfiquar_1_2_a),
    path('zulfiquar_1_2_b/', views.timetableZulfiquar_1_2_b),
    re_path('^.*$', views.select),

]
