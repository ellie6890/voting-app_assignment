from django.contrib import admin

# Register your models here.
from .models import Project, Vote  # ← models.py 에서 Project 불러오기

admin.site.register(Project)  # ← 관리자 페이지에 등록
admin.site.register(Vote)  # ← 이 줄 추가