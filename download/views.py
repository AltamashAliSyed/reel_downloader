from django.shortcuts import render
import yt_dlp
# Create your views here.
def home(request):
    video_url = None
    error = None

    if request.method =="POST":
        video_link = request.POST.get("url")

        try:
            ydl_opts ={
                'format':'mp4',
                'outtmpl':'media/%(title)s.%(ext)s'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_link,download=True)
                video_url=info.get("title")+".mp4"
        except Exception as e:
             error = "Download Failed"
         

   
    
    return render(request,'index.html',{'video':video_url,'error':error})