# views.py
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
from django.conf import settings
from PIL import Image
import io
import os

# 1. HttpResponse (Simple String Response)
def simple_response(request):
    return HttpResponse("Hello, this is a simple string response!")

# 2. JsonResponse (JSON Response)
def json_response(request):
    data = {'message': 'Hello, this is a JSON response!'}
    return JsonResponse(data)

# 3. StreamingHttpResponse (Stream Large Data)
def stream_response(request):
    def generate_large_data():
        yield "Line 1 of large data\n"
        yield "Line 2 of large data\n"
        yield "Line 3 of large data\n"
        # Simulate large data by repeating the same lines

    return StreamingHttpResponse(generate_large_data())

# 4. FileResponse (File Download)
def file_response(request):
    # Direct path to your static file
    file_path = settings.BASE_DIR / 'responses' / 'static' / 'helloworld.pdf'
    
    # Check if the file exists and then return the FileResponse
    try:
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='helloworld.pdf')
    except FileNotFoundError:
        return HttpResponse("File not found.", status=404)

# 5. HttpResponse with HTML Content
def html_response(request):
    html_content = "<html><body><h1>Welcome to my site!</h1></body></html>"
    return HttpResponse(html_content)

# 6. HttpResponse with XML Content
def xml_response(request):
    xml_content = "<response><message>Hello, this is XML data!</message></response>"
    return HttpResponse(xml_content, content_type="application/xml")

# 7. HttpResponse with Plain Text
def plain_text_response(request):
    text_content = "This is plain text response."
    return HttpResponse(text_content, content_type="text/plain")

# 8. JsonResponse with List Data
def json_list_response(request):
    data = {'users': ['Alice', 'Bob', 'Charlie']}
    return JsonResponse(data)

# 9. HttpResponse with Image
def image_response(request):
    img = Image.new('RGB', (100, 100), color='blue')
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return HttpResponse(buf, content_type="image/png")

# 10. HttpResponse with Video File
def video_response(request):
    video_path = settings.BASE_DIR / 'responses' / 'static' / 'video.mp4'
    return FileResponse(open(video_path, 'rb'), content_type='video/mp4')
