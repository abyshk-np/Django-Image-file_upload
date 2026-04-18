Django Profile Image Upload System

A simple Django project that allows users to upload and view profile pictures. This project demonstrates how to handle image uploads, store them, and display them using Django.


Features

* Upload profile with name and image
* Store image in media folder
* Save image path in database
* Display all uploaded profiles
* Show success/error messages


Logic (Simple Explanation)

1. User opens the upload page and fills the form.
2. Form sends data (name + image) to the backend.
3. Django checks if the form is valid.
4. If valid:

   * Image is saved in `media/profiles/`
   * Image path and name are saved in database
5. When viewing profiles:

   * Data is fetched from database
   * Images are displayed 

**User → Form → View → Model → Database + Media → Template → User**


Tech/Tools

* Python
* Django
* SQLite (default database)
* Pillow (for image handling)
* also other DB can be used


Images
![Path Page](https://github.com/abyshk-np/Django-Image-file_upload/blob/main/IMGE/Image/Screenshot%202026-04-16%20232450.png)
![Path Page](https://github.com/abyshk-np/Django-Image-file_upload/blob/main/IMGE/Image/Screenshot%202026-04-16%20232541.png)

Setup Instructions

Clone Repository

```
git clone https://github.com/abyshk-np/Django-Image-file_upload.git
```

Create Virtual Environment

```
python -m venv env
env\Scripts\activate
```

Install
<h5>Pillow is a python library which help user to manipulate, and save various image file formats.</h5>

```
pip install django pillow
```

Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

Run Server

```
python manage.py runserver
```



URLs

* Upload Profile → `http://127.0.0.1:8000/upload/`
* View Profiles → `http://127.0.0.1:8000/profiles/`



Important Settings

Add in `settings.py`:

```
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

And in main `urls.py`:

```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```




Conclusion

This project is a beginner-friendly example to understand how Django handles image uploads and connects frontend with backend efficiently.



⭐ If you found this helpful, consider giving it a star!
