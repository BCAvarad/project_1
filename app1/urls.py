from django.urls import path
from app1.views import *
urlpatterns = [
    path('',demo,name='demo'),
    path("regi/",regi,name="regi"),
    path("register/",register,name="rform"),
    path("login/",login,name="login"),
    path("stdlogin/",std_login,name="std_login"),
    path("logout/",s_logout,name="s_logout"),
    path("tlogout/",tlogout,name="t_logout"),
    path("sdashbord/",sdashbord,name="sdashbord"),
    path("result/",showresult,name="showresult"),
    path("tdashbord/",tdashbord,name="tdashbord"),
    path("tclass/",tclass,name="tclass"),
    path("tstudent/",tstudent,name="tstudent"),
    path("tresult/",tresult,name="tresult"),
    path("tregister/",tregister,name="tregister"),
    path("tfregister/",tfregister,name="tfregister"),
    path("addresult/",addresultpage,name="addresult"),
    path("stdsearch/",stdsearch,name="stdsearch"),
    path("clear/",clrear,name="clear"),
    path("taddresult/",taddresult,name="taddresult"),
    path("addstudentpage/",addstudentpage,name="addstudentpage"),
    path("showresultstd/",show_individual_result,name="showresultstd"),
]
