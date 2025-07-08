from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Vote

# 1. 프로젝트 리스트 (평균 점수 높은 순 정렬)
def project_list(request):
    projects = Project.objects.all()
    projects = sorted(projects, key=lambda p: p.average_score(), reverse=True)
    return render(request, 'projects/project_list.html', {'projects': projects})

# 2. 프로젝트 상세 페이지
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})

# 3. 투표 처리 뷰
def project_vote(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        score = int(request.POST['score'])
        Vote.objects.create(project=project, score=score)
    return redirect('project_detail', project_id=project.id)
