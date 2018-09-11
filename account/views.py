from django.shortcuts import render
from account.models import File
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
# Create your views here.


"""
Method:             userProfile
Developer:          Anoop
Created Date:       11-09-2018
Purpose:            Show other user's dashboard
Params:             user_id
Return:             [user data]
"""
# @login_required
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    # return HttpResponse("Hello")
    return render(request, 'index.html', {})
"""end function userProfile"""

def userLogin(request):
    # return HttpResponse("Hello")
    # return render(request, 'login.html', {})
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        # rememberMe = request.POST.get('remember_me')
        try:
           newUser = User.objects.get(username = username)
        except User.DoesNotExist:
           newUser = None
        print('============================')
        print(newUser)
        print('============================')
        if newUser is not None:
            user = authenticate(username = newUser.username, password = password)
            print(" Heree")
            print(user)
            print("=================")
            if user is not None:
                print('dhjsdh')
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            else:
                print('User')
                return HttpResponseRedirect('/')
        # messages.warning(request, 'Invalid email or password')
        return HttpResponseRedirect('/')
    else:
        return render(request, 'login.html', {})


def dashboard(request):
    return HttpResponse("dashboard")
    # return render(request, 'index.html', {})

"""end function userProfile"""
@csrf_exempt
def fileUpload(request):
    if request.method == "POST":
        print("=============================")
        # print("Here ==>> "  )
        print(request.user.id)
        filename = request.POST.get('file_name')
        media = request.FILES.get('file_media', False)
        mediaName = media.name
        print("mediaName " +str(mediaName))
        mediaTpye = media.content_type.split('/')[0]
        print(mediaTpye)
        if mediaName.endswith('.wav'):
            print ('File is a mp3')
            try:
                fileData = File.objects.filter(file_name=mediaName)
            except File.DoesNotExist:
                fileData = None
            print("Now we are here")
            print(fileData)
            if not fileData:
                print(' Here there ')
                fs = FileSystemStorage()
                filename = fs.save(media.name, media)
                print("fullname  "+str(filename))
                fileContent = File()
                fileContent.file_name = filename
                fileContent.file_media = mediaName
                # fileContent.user_id = request.user.id
                fileContent.parent_id = ""
                fileContent.save()
            else:
                protocol = request.scheme
                print(' Here ' +str(protocol))
                host = request.get_host()
                print('host  ' +str(host))
                print("name is ====  " +str(mediaName))
                import wave
                # path = protocol+'://'+host+'/media/'+mediaName
                path = '/home/shiv/Desktop/wav/wav/media/'
                print('Duplicate. Appending to previous file - ')
                print(path)
                print(mediaName)
                w = wave.open(path+mediaName, 'rb')
                print (w)
                print(fileData)

        else:
            print ('File is NOT a mp3')
        # size = media._size
        # print("size == " +str(size))
        # if 'image' == mediaTpye or 'video' == mediaTpye:
        #     fs = FileSystemStorage()
        return HttpResponse("fileupload")
