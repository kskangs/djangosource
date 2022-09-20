from django.shortcuts import render
from django.http import HttpResponse

from photo import photo
from .models import Photo

# HttpResponse : 응답 객체
    # 1) 문자열을 담아서 리턴
    # 2) 특정 페이지를 리턴
    # return HttpResponse(template.render(템플릿, 전달해 줄 객체))

#함수형 뷰
def home(request):
    return HttpResponse("INDEX")
    

def photo_list(request):
    
    # 사진목록 추출한 후 목록을 보내야 함
    # select * from photo_photo;
    # QuerySet 결과로 나옴
    photos = Photo.objects.all()

    return render(request, "photo_list.html",("photos":photos))
