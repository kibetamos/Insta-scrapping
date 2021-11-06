from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    if request.method == 'POST':
        github_user = request.POST['github_user']
        user = request.POST['user']
        url = 'https://www.instagram.com/' + github_user
        r = requests.get(url)
        soup = bs(r.content)
        profile = soup.find('img', {'alt': 'Avatar'})['src']

        new_github = Github(
            githubuser=github_user,
            imagelink=profile,
            username=user
        )
        new_github.save()
        messages.info(request, 'User ' + github_user + ' Image Saved')
        return redirect('/')

    return render(request, 'index.html')
def images(request):
    username = request.user
    git_hub = Github.objects.filter(username=username)

    return render(request, 'images.html', {'git_hub': git_hub})