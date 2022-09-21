from email.mime import image
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from photo.photo.forms import Photoform

from .models import Photo
from .formsPhotoform,  importPhotoform, 



# HttpResponse : 응답 객체
    # 1) 문자열을 담아서 리턴
    # 2) 특정 페이지를 리턴
    # return HttpResponse(template.render(템플릿, 전달해 줄 객체))

#함수형 뷰
def photo_list(request):

    photos = Photo.objects.all()

    return render(request,"photo_list.html",{"photos":photos})

def photo_post(request):
# Photoform 사용하는 방식
    if request.method == "POST":
#        "사용자 입력값 가져와서 Photoform에 바인딩 시켜 줌"
form = Photoform(request.POST)



if form.is_valid(): # 유효성 검사
# 입력값 데이터 베이스에 저장(모델 폼인 경우 form.save() 하게 되면 모델에 변화를 주게 됨)
form.save()

#성공 시 리스트 보여주기
            return redirect("photo_list")
        else:
            form = Photoform()

        return render(request,"photo_post2.html",{"form":form})

# def photo_detail(request, pk):
#     # pk에 해당하는 게시물 가져오기
#     # get_object_or_404() 특정조건에 맞는 코드가 존재한다면 객체 생성 or 존재하지 않는다면 404
#     photo = get_object_or_404(Photo, pk=pk)

#     #템플릿을 보여줄 때 게시물 딸려 보내기

#     return render(request,"photo_detail.html":{"photo":photo})

def photo_remove(request,pk):
    print("삭제",pk)
    
    # pk 해당하는 게시물 가져오기
    photo = get_object_or_404(Photo, pk=pk)

    # 찾은 게시물 삭제
    photo.delete()

    # 사진 목록 보기로 이동
    return redirect("photo_list")

def photo_edit(request,pk):

    # Photoform 사용하는 방식




    # post 요청
    if request.method == "POST":
        pass
    # 수정 내용 가져오기

    form = Photoform(instance=object)

    if form.is_value():
        photo = form.save()
    
    # 상세보기 이동
    return redirect("photo_detail".pk=photo.pk)
    else:
            # pk 해당하는 게시물 가져오기

    object = get_object_or_404(Photo, pk=pk)
    photo = Photoform(instance=object)

    # get 요청
    # 템플릿을 보여줄 때 게시물 딸려 보내기
    return render(request,"photo_edit.html",{"photo":photo})