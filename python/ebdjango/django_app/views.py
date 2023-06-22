import boto3
from django.http.response import JsonResponse

def version(request):
    return JsonResponse({'version': 'v1.0'})

def health(request):
    return JsonResponse({'status': 'OK'})

def aws(request):
    return JsonResponse(boto3.client('sts').get_caller_identity())