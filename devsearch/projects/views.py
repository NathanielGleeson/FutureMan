from django.shortcuts import render
from .models import Project, Tag, Review


def projects(request):
	page = 'projects'
	number = 9
	context = {'page': page, 'number': number}
	return render(request, 'projects/projects.html', context)

def project(request, pk):
	projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=projectObj.id)

    return render(request, 'projects/single-project.html', {'project': projectObj, 'form': form})