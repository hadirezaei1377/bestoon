from django.conf import settings

def submit_expense(request):
    """ submit an expense """

    this_date = request.POST['date'] if 'date' in request.POST else timezone.now()
    this_text = request.POST['text'] if 'text' in request.POST else ""
    this_amount = request.POST['amount'] if 'amount' in request.POST else "0"
    this_token = request.POST['token'] if 'token' in request.POST else ""
    this_user = get_object_or_404(User, token__token=this_token)

    Expense.objects.create(user=this_user, amount=this_amount,
                           text=this_text, date=this_date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)  # return {'status':'ok'}




# submit an income to system (api) , input : token(POST) , output : status
# = (ok)
@csrf_exempt
@require_POST
def submit_income(request):
    """ submit an income """

    # TODO: revise validation for the amount
    this_date = request.POST['date'] if 'date' in request.POST else timezone.now()
    this_text = request.POST['text'] if 'text' in request.POST else ""
    this_amount = request.POST['amount'] if 'amount' in request.POST else "0"
    this_token = request.POST['token'] if 'token' in request.POST else ""
    this_user = get_object_or_404(User, token__token=this_token)

    Income.objects.create(user=this_user, amount=this_amount,
                          text=this_text, date=this_date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


# submit an expanse to system (api) , input : token(POST) , output :
# status = (ok)
@csrf_exempt
@require_POST
def submit_expense(request):
    """ submit an expense """

    # TODO: revise validation for the amount
    this_date = request.POST['date'] if 'date' in request.POST else timezone.now()
    this_text = request.POST['text'] if 'text' in request.POST else ""
    this_amount = request.POST['amount'] if 'amount' in request.POST else "0"
    this_token = request.POST['token'] if 'token' in request.POST else ""
    this_user = get_object_or_404(User, token__token=this_token)

    Expense.objects.create(user=this_user, amount=this_amount,
                           text=this_text, date=this_date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)  # return {'status':'ok'}

