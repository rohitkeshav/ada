import os
import json

from ada_project import settings
from rent.models import CustomUser

from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET


@csrf_exempt
@require_POST
def sign_up(request):
    r_body = json.loads(request.body)

    email_id = r_body['email']

    if not r_body['fname'] or not r_body['lname'] or not r_body['email'] or not r_body['password']:
        return JsonResponse({'message': 'Missing required attributes'})
    elif CustomUser.objects.filter(email=email_id).exists():
        return JsonResponse({'message': 'User with email already exists'})

    new_user = CustomUser.objects.create_user(
        first_name=r_body['fname']
        , middle_name=r_body.get('mname')
        , last_name=r_body['lname']
        , password=r_body['password']
        , email=email_id
        , date_of_birth=r_body.get('dob')
        , phone_number=r_body.get('pnum')
        , user_type=r_body['utype']
    )

    return JsonResponse({'message': 'Logged In', 'data': {'uname': new_user.email
                                                          , 'fname': new_user.first_name
                                                          , 'lname': new_user.last_name}})


@csrf_exempt
@require_POST
def sign_in(request):
    r_body = json.loads(request.body)

    if not r_body['email'] or not r_body['password']:
        return JsonResponse({'message': 'Missing either email or password'})

    user = authenticate(username=r_body['email'], password=r_body['password'])

    if user:
        login(request, user)
        return JsonResponse({'message': 'User signed in'})
    else:
        return JsonResponse({'message': 'Issue logging in, email-password combo mismatch'})


@require_GET
def sign_out(request):
    logout(request)

    return JsonResponse({'message': 'User successfully logged out'})


class ServeReactApp(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501, )
