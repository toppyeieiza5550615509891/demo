import random

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView, RedirectView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.views import LogoutView

from .forms import SignupForm, BlogForm, CommentForm, ProfileForm
from .models import UserModel, BlogModel, CommentModel
# Create your views here.

class test(FormView):
    form_class = CommentForm
    template_name = 'hello.html'

class signout(LogoutView):
    success_url_allowed_hosts = set('/')
    template_name='signout.html'

    def post(self, request, *args, **kwargs):
        
        return redirect('auth')


class blog(ListView):
    model = BlogModel
    context_object_name = 'blogs'
    template_name='blog.html'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        print(user)
        if str(user) == 'AnonymousUser':
            raise Http404
        queryset = BlogModel.objects.order_by('-created_on')
        return queryset
        
    

class addblog(CreateView):
    model = BlogModel
    template_name = 'addblog.html'
    # fields = ['text']
    success_url = ('blog')
    form_class = BlogForm


class blog_item(DetailView):
    template_name = 'blog_item.html'
    model = BlogModel

    def get_context_data(self, **kwargs):
        user = self.request.user
        if str(user) == 'AnonymousUser':
            raise Http404
        
        context = super().get_context_data(**kwargs)
        blog = context['object'].pk
        context['comment'] = CommentModel.objects.filter(blog_id=blog).all()
        return context


class profile(UpdateView):
    template_name = 'profile.html'
    form_class = ProfileForm
    success_url = 'profile'
    # fields = ['tel', 'givename', 'lastname', 'email']

    def get_object(self, queryset=None):
        user = self.request.user
        if user is not None:
            usermodel = UserModel.objects.get(username=user.username)
            return usermodel
        return redirect('auth')


class signup(TemplateView):
    template_name = 'singup.html'

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        usermodel = UserModel(username=username)
        if user is not None:
            usermodel.save()
            return redirect('auth')
        return redirect('signup')


class auth(TemplateView):

    def get(self, request):
        return render(request, 'auth.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # request.session['session'] = username
            login(request, user)
            return redirect('blog')
        else:
            return render(request, 'auth.html')

    # def post(self, request, *args, **kwargs):
    #     # form = BlogForm()
    #     form = BlogForm()
    #     if form.is_valid():
    #         text = form.cleaned_data['text']
    #         form.save()
    #         return redirect('addblog')
    #     return 'Heelo'
        # form.save()
            # return super().post(request, *args, **kwargs)
            



# class blog_item(DetailView):
#     model = BlogModel
#     template_name='blog_item.html'
#     # pk_url_kwarg = 'pk'
#     # context_object_name = 'blogs'
#     # pk_url_kwarg = 'aa'
    

#     # def get_queryset(self, **kwargs):
#     #     return BlogModel.objects.filter(created_on__gte='2019-05-23 09:30')
    

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         blog = context['object']
#         blog_id = blog.pk
#         ### ***&******
#         # context['comment'] = blog.commentmodel_set.all()
#         context['comment'] = CommentModel.objects.filter(blog_id=blog_id).all()
#         # context['comment'] = CommentModel.objects.filter(blog_id_id=blog_id).all()
#         return context






    # def get_context_data(self, **kwargs):
        
    #     if self.request.user.is_authenticated:
    #         print('sucessful')
    #         username = self.request.user.username
    #         usermodel = UserModel.objects.get(username=username)
    #         context = super().get_context_data(**kwargs)
    #         context['profile'] = usermodel
    #         return context

    #     print('unsucessful')

    #     return redirect('signin')
    
    # def post(self, request):
    #     username = self.request.user.username
    #     # name = request.session['session']
    #     firstname = request.POST.get('firstname')
    #     lastname = request.POST.get('lastname')
    #     tel = request.POST.get('tel')
    #     email = request.POST.get('email')
    #     user = UserModel.objects.get(username=username)
        
        
    #     return redirect('signup')
    






        
# def profile(request):
#     name = request.session['session']
#     user = UserModel.objects.filter(username=name).first()
#     print(user)
#     if request.method == 'POST':
#         forms = ProfileForm(request.POST, instance=user)
#         # tel = forms.cleaned_data['tel']
#         # email = forms.cleaned_data['email']
#         # tel = request.cleaned_data['']
#         # givename = forms.cleaned_data['givename']
#         # lastname = forms.cleaned_data['lastname']
#         # objects = UserModel.objects.filter(username=name).update(tel='011111')

#         if forms.is_valid():
#             print('tes')
#             forms.save()
#             tel = forms.cleaned_data['tel']
#             email = forms.cleaned_data['email']
#             givename = forms.cleaned_data['givename']
#             lastname = forms.cleaned_data['lastname']
#             # objects = UserModel.objects.filter(username=name).update(tel=tel, email=email, givename=givename, lastname=lastname)
#             return redirect('profile')
#         elif forms.errors:
#             error = forms.errors.as_json()
#             print(error)
            
#         print('not vllid')
#     forms = ProfileForm(instance=user)
#     context = {
#         'forms' : forms
#     } 
#     return render(request, 'profile.html', context)


# # class signup(CreateView):
# #     model = UserModel
# #     fields = ['username', 'password']  
# #     template_name = 'singup.html'


# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = User.objects.create_user(username=username, email=email, password=password)
#         # user = User.objects.create_user(username, email, password)
#         user.save()
#         return redirect('auth')

#     else:
#         return render(request, 'singup.html')





# def auth(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # user = authenticate(username=username, password=password)
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             request.session['session'] = username
#             login(request, user)
#             return redirect('blog')
#         else:
#             return render(request, 'auth.html')
#     # No backend authenticated the credentials
#         # if UserModel.objects.all().filter(username=username) and UserModel.objects.all().filter(password=password):
#         #     request.session['session'] = username
#         #     return redirect('blog')
    
#     return render(request, 'auth.html')
    # r = open('user.txt', 'r  hhcvyn  -- bv                                                                                                                                                                                            +')
    # if request.method == 'POST':
    #     username = request.POST.get('ID')
    #     password = request.POST.get('PASS')
    #     list_user = r.read().split('\n')
    #     item_list = []
    #     for item in list_user:
    #         item_list.append(item.split('|'))
    #     for item in item_list:
    #         if (username == item[0]) and (password == item[1]):
    #             request.session['session'] = username
    #             return redirect('blog')
    #     return render(request, 'auth.html')
    # r.close()
    # return render(request, 'auth.html')



# def blog(request):
#     # if not fav_color:
#     #     return redirect('auth')
#     # print(dict(request.session))


#     if not 'session' in request.session:
#         print('ไม่มีsessionเว้นย')
#     else:
#         name = request.session['session']
#         context = {
#             'blogs' : BlogModel.objects.all(),
#             'user' : name  
#         }
#         return render(request, 'blog.html', context)
        # return redirect('auth')


    # try:
    #     fav_color = request.session['session']
    # except KeyError:
    #     return redirect('auth')
        # fav_color = request.session.get('session')
        # if request.method == 'POST':
        #     return render(request, 'blog.html')    
        

        # r = open('blog.txt', 'r+')
        # list_blog = r.read().split('\n')
        # blog = [i.split('|') for i in list_blog]
        # fav_color = request.session['session']
        # len_blog = len(blog)
               
        # context = {
        #     'blogs' : blog[len_blog:len_blog-10:-1],
        #     'range' : len_blog,
        #     'user' : fav_color, 
        # }
        # return render(request, 'blog.html', context)   
        # if request.method == 'POST':
        




# def addblog(request):
#     name = request.session['session']
#     form = BlogForm()
#     if name == 'admin':
#         if request.method == 'POST':
#             form = BlogForm(request.POST)
#             if form.is_valid():
#                 text = form.cleaned_data['text']
#                 form.save()
#                 return redirect('blog')
#             elif forms.errors:
#                 error = forms.errors.as_json()
#                 print(error)
            
        # if request.method == 'POST':
        #     r = open('blog.txt', 'a+')
        #     blog = request.POST.get('box')
        #     ran_num = random.randint(1,100)
        #     a = '\n' + blog + '|' + name + '|' + str(ran_num)
        #     r.write(a)
        #     return redirect('blog')

        #Get method
        # else:   
            
        #     return render(request, 'addblog.html', {"forms":form})
    # Not an admin
    # else:
    #     return render(request, 'addblog.html',{'forms':form})
    


   

# def item(request, blog_id):
#     if request.method == 'POST':
#         forms = CommentForm(request.POST)
#         if forms.is_valid():
#             comment = forms.cleaned_data['comment']
#             forms.save()
#             return redirect('blog_item', blog_id=blog_id)
        # name = request.session['session']
        # comment = request.POST.get('comment')
        # f = open('comment.txt', 'a+')
        # a = '\n' + comment + '|' + name + '|' + str(blog_id)
        # f.write(a)
        # return redirect('blog_item', blog_id=blog_id)
    #     elif forms.errors:
    #         error = forms.errors.as_json()
    #         print(error)
            
    # else:
    #     forms = CommentForm()
    #     context = {
    #         'comment' : CommentModel.objects.filter(blog_id=str(blog_id)),
    #         'blogs' : BlogModel.objects.filter(id=str(blog_id)),
    #         'forms' : forms
    #     }
    #     return render(request, 'blog_item.html', context)
                
    #     for i in my_blog:
    #         if i['id'] == blog_id:
    #             i['comment'].append({'user':name, 'text':comment})
    #             return redirect('blog_item', blog_id=blog_id)

    # for i in my_blog:
    #     if i['id'] == blog_id:
    #         context = {
    #             'blog' : i
    #         }
#     r = open('blog.txt', 'r+')
#     list_blog = r.read().split('\n')
#     blog = [i.split('|') for i in list_blog]
#     new_blog = []
#     for i in blog:
#         if str(blog_id) in i:
#             new_blog.append(i)
    
#     c = open('comment.txt', 'r+')
#     list_comment = c.read().split('\n')
#     blog_comment = [i.split('|') for i in list_comment]
#     comment = []
#     for i in blog_comment:
#         if str(blog_id) in i:
#             comment.append(i)
#     context = {
#        'blog' : new_blog,
#         'comment' : comment
#     }
#     print(comment)
#     c.close()
#     r.close()
#     return render(request, 'blog_item.html', context)



    # form = SignupForm()
    # if request.method == 'POST':
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('auth')
    #     elif form.errors:
    #         error = form.errors.as_json()
    #         print(error)        
    # else:
    #     return render(request, 'singup.html', {'forms':form})



    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # f = open('user.txt','a+')
    # if request.method == 'POST':
    #     a = username + '|' + password + '\n'
    #     print(a)
    #     f.write(a)
    #     f.close()
    #     return redirect('auth')
    # f.close()
    # return render(request, 'singup.html')




# def signout(request):
#     name = request.session['session']
#     if request.method == 'POST':
#         request.session.pop('session')
#         return redirect('auth')
    
#     else:
#         # name = request.session['session']
#         context ={
#             'user' : name
#         }
#         return render(request, 'signout.html', context)


# class profile(ListView):
#     model = UserModel
#     context_object_name = ''
#     template_name='profile.html'


    






