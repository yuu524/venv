from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from google.cloud import vision
import os

def mainmenu_views(request):
    return render(request, 'certification/mainmenu.html')

def upload(request):
    return render(request, 'certification/upload.html')

def history(request):
    return render(request, 'certification/history.html')

def settings_view(request):
    return render(request, 'certification/settings.html')

def result(request):
    return render(request, 'certification/result.html')

def language_selection(request):
    return render(request, 'languageSelection.html')

def history_views(request):
    return render(request,'certification/history.html')

# Google Cloud Vision API のクライアントを設定
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/y_nakazawa/Desktop/venv/vision-travel-project-448601-24017b05a971.json"

@csrf_exempt
def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        # アップロードされた画像を保存
        image = request.FILES["image"]
        fs = FileSystemStorage()
        saved_file_path = fs.save(image.name, image)
        saved_file_url = fs.url(saved_file_path)
        file_full_path = fs.path(saved_file_path)

        # Google Vision APIを使用して画像を解析
        client = vision.ImageAnnotatorClient()
        with open(file_full_path, "rb") as image_file:
            content = image_file.read()
        image_vision = vision.Image(content=content)
        response = client.landmark_detection(image=image_vision)
        landmarks = response.landmark_annotations

        # ランドマークデータを整形
        results = []
        if landmarks:
            for landmark in landmarks:
                results.append({
                    "name": landmark.description,
                    "latitude": landmark.locations[0].lat_lng.latitude,
                    "longitude": landmark.locations[0].lat_lng.longitude,
                })

        # ランドマーク情報を `result.html` に渡す
        return render(request, "certification/result.html", {
            "landmarks": results,
            "file_url": saved_file_url,  # アップロードされた画像のURL
        })
    
    return render(request, "certification/upload.html")

from django.core.files.storage import FileSystemStorage

def history(request):
    fs = FileSystemStorage(location='media')  # media フォルダに画像が保存されている場合
    images = fs.listdir('uploaded_images/')[1]  # uploaded_images ディレクトリ内のすべてのファイル名を取得
    image_objects = [{'url': fs.url(img), 'name': img} for img in images]  # 各画像に URL と名前を設定

    return render(request, 'certification/history.html', {'images': image_objects})
