import os
import json

from ada_project import settings
from rent.models import CustomUser, Listing, AcceptedApplicants, Applicants

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


@csrf_exempt
@require_POST
def create_listing(request):

    listing_body = json.loads(request.body)

    try:
        uobj = CustomUser.objects.get(email=listing_body['owner'])
        if uobj.user_type.lower() == 'owner':
            listing_body['owner'] = uobj
        else:
            raise AttributeError('User needs to be of type "Owner"')
    except:
        return JsonResponse({'message': 'User does not exist'})

    lobj = Listing(**listing_body)
    lobj.save()

    return JsonResponse({'message': 'Listing created'})


@require_POST
def apply_for_listing(request):
    tenant_user = CustomUser.objects.get(email=request.user)

    robj = json.loads(request.body)

    listing = Listing.objects.get(id=robj['lid'])

    aobj = Applicants(**{'listing': listing, 'applicant': tenant_user})
    aobj.save()

    return JsonResponse({'message': 'Application submitted'})


@require_POST
def create_tenant_for_listing(request):
    owner_user = CustomUser.objects.get(email=request.user)

    if owner_user.user_type.lower() != 'owner':
        return JsonResponse({'message': 'User not authorized to'})

    robj = json.loads(request.body)

    listing = Listing.objects.get(id=robj['lid'])
    tenant = CustomUser.objects.get(id=robj['tenant_id'])

    aobj = Applicants(**{'listing': listing, 'applicant': tenant})
    aobj.save()

    return JsonResponse({'message': f'Listing assigned to new tenant - { tenant.email }'})


@require_GET
def get_applicants(request, uid):
    all_applicants = Applicants.objects.filter(listing__id=uid)

    return JsonResponse(all_applicants)


@require_GET
def check_tenants(request, uid):
    all_applicants = AcceptedApplicants.objects.filter(listing__id=uid, listing__owner=request.user)

    return JsonResponse(all_applicants)


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
