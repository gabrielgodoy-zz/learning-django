# Generic class-based display views for when user is creating, editing or deleting an object
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# reverse_lazy adds ability to redirect after delete action for example
from django.core.urlresolvers import reverse_lazy

# redirects to whatever page you want after user login
from django.shortcuts import render, redirect

# authenticate | Verify that user is in database and give acces to them or not
# Login | handles authentication between pages, giving a sessions ID
from django.contrib.auth import authenticate, login

from django.views import generic

from django.views.generic import View

from .models import Album

from .forms import UserForm


# Django have built-in views for different scenarios
# that repeats on every website

# Pattern for displaying list of objects
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'  # Override default name object_list for view context

    def get_queryset(self):
        # generic.ListView  queries all Albums and return object_list as context to the HTML file
        return Album.objects.all()


# Pattern for displaying details of a single object
class DetailView(generic.DetailView):
    model = Album
    # Template view of details
    template_name = 'music/detail.html'


# template_name here dont need to specified, because the file name album_form.html follow name convention,
# So the class CreateView automatically finds files with template_name_suffix = _form
class AlbumCreate(CreateView):
    model = Album
    # Fields for user to fill
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    # Fields for user to fill
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    # When you successfully delete an object (album), go back to index
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    # Blueprint to use on the form | UserForm created in forms.py
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # When is a get request use this method
    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # When is a post request use this method
    # process form data via POST method
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # Creates an object from the form
            user = form.save(commit=False)  # Does not save to database yet, storing 'locally'

            # Get clean normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()  # Save to database

            # Authenticate and log in the user
            # returns USer objects  if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                # Check if user account is not disabled or banned
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')  # Go to Home after login

        return render(request, self.template_name, {'form': form})
