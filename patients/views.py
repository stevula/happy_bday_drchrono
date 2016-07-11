import datetime
import pytz
import requests

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from happy_bday.settings import CLIENT_ID, REDIRECT_URI

from .models import Patient, Doctor


# VIEWS

class IndexView(generic.ListView):
    def get_queryset(self):
        """ All patients for currently signed in doctor """
        # TODO: get currently signed in doctor
        doctor = Doctor.objects.get(pk=1)
        return doctor.patient_set.all()


class DetailView(generic.DetailView):
    model = Patient


class SigninView(generic.View):
    template_name = 'patients/patient_signin.html'

    def get(self, request):
        return render(request, 'patients/patient_signin.html', {
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
            })


# VIEWLESS ACTIONS

def drchrono(request):
    if 'error' in get_params:
        raise ValueError('Error authorizing application: %s' % get_params[error])

    response = requests.post('https://drchrono.com/o/token/', data={
        'code': get_params['code'],
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    response.raise_for_status()
    data = response.json()

    # Save these in your database associated with the user
    access_token = data['access_token']
    refresh_token = data['refresh_token']
    expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])

    response = requests.get('https://drchrono.com/api/users/current', headers={
        'Authorization': 'Bearer %s' % access_token,
    })
    response.raise_for_status()
    data = response.json()

    # You can store this in your database along with the tokens
    username = data['username']
    return HttpResponse(username)


def create(request):
    # TODO: get currently signed in doctor
    doctor = Doctor.objects.get(pk=1)
    form = request.POST
    doctor.patient_set.create(
        name=form['name'],
        dob=form['dob'],
        email=form['email'],
        phone=form['phone'])
    # TODO: redirect to patient show?
    return HttpResponseRedirect(reverse('patients:index'))


def destroy(request):
    # TODO: get specific patient
    patient = Patient.objects.get(pk=1)
    return HttpResponseRedirect(reverse('patients:index'))
