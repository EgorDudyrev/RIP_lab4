from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris venenatis sem eu neque elementum semper. Aenean a quam enim. Praesent dictum, magna non tincidunt luctus, tortor tellus lobortis lorem, eu sodales felis libero sit amet nulla. Nam rhoncus faucibus fermentum. Sed nec est tellus. Vestibulum vitae volutpat sem, et ullamcorper tortor. Donec venenatis libero vel metus luctus eleifend. Praesent eleifend metus tincidunt, tempus leo a, volutpat dui." \
            "Integer mattis cursus ante, non maximus ligula pellentesque eu. Phasellus semper libero ac tortor auctor placerat. Quisque quam ipsum, gravida vitae risus at, fringilla vestibulum nibh. Donec fermentum accumsan velit vel rutrum. In imperdiet, leo nec finibus vehicula, tellus massa vehicula arcu, non feugiat leo ex ac dolor. In sagittis augue quis metus suscipit dapibus. Curabitur ultrices erat malesuada, viverra arcu ornare, accumsan est." \
            "Suspendisse dignissim odio at nibh malesuada, sit amet volutpat ante pellentesque. Ut id lorem commodo, mollis sapien sit amet, vestibulum magna. Curabitur a convallis augue, eu hendrerit ipsum. Cras semper dolor id mauris porttitor, a sagittis felis mattis. In hac habitasse platea dictumst. Curabitur eu ex vel orci ultrices commodo. Integer ac ligula massa."

    news = [{'id':i} for i in range(10)]
    for n in news:
        id = n['id']
        n['title'] = 'Title #'+str(id+1)
        n['content'] = lorem[:150]+'...'

    context = {'news_list': news[:5]}
    return render(request,'index.html',context)

def single_news(request,id):
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris venenatis sem eu neque elementum semper. Aenean a quam enim. Praesent dictum, magna non tincidunt luctus, tortor tellus lobortis lorem, eu sodales felis libero sit amet nulla. Nam rhoncus faucibus fermentum. Sed nec est tellus. Vestibulum vitae volutpat sem, et ullamcorper tortor. Donec venenatis libero vel metus luctus eleifend. Praesent eleifend metus tincidunt, tempus leo a, volutpat dui." \
            "Integer mattis cursus ante, non maximus ligula pellentesque eu. Phasellus semper libero ac tortor auctor placerat. Quisque quam ipsum, gravida vitae risus at, fringilla vestibulum nibh. Donec fermentum accumsan velit vel rutrum. In imperdiet, leo nec finibus vehicula, tellus massa vehicula arcu, non feugiat leo ex ac dolor. In sagittis augue quis metus suscipit dapibus. Curabitur ultrices erat malesuada, viverra arcu ornare, accumsan est." \
            "Suspendisse dignissim odio at nibh malesuada, sit amet volutpat ante pellentesque. Ut id lorem commodo, mollis sapien sit amet, vestibulum magna. Curabitur a convallis augue, eu hendrerit ipsum. Cras semper dolor id mauris porttitor, a sagittis felis mattis. In hac habitasse platea dictumst. Curabitur eu ex vel orci ultrices commodo. Integer ac ligula massa."

    news = [{'id':i} for i in range(10)]
    for n in news:
        idx = n['id']
        n['title'] = 'Title #'+str(idx+1)
        n['content'] = lorem
    context = {'news': news[int(id)]}
    return render(request,'single_news.html',context)
