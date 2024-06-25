from django.shortcuts import render

# Create your views here.

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from mother.models import Mother_visit, Mother
from child.models import Child_visit, Child


@csrf_exempt
def get_next_visit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        registration_number = data.get('registration_number')

        try:
            # Search for the child
            child = Child.objects.get(child_number=registration_number)
            latest_visit = Child_visit.objects.filter(child=child).order_by('-date').first()

            if latest_visit:
                return_date = latest_visit.return_date
                response_text = f"The next scheduled visit for your child {child.child_name} is on {return_date}."
                return JsonResponse({'message': response_text})
            else:
                return JsonResponse({'error': 'No visits found for this child'}, status=404)

        except Child.DoesNotExist:
            # If the child does not exist, search for the mother
            try:
                mother = Mother.objects.get(registration_number=registration_number)
                latest_mother_visit = Mother_visit.objects.filter(mother=mother).order_by('-visit_date').first()

                if latest_mother_visit:
                    next_visit_date = latest_mother_visit.date_of_next_visit
                    response_text = f"Dear {mother.mother_name} your next scheduled visit is on {next_visit_date}."
                    return JsonResponse({'message': response_text})
                else:
                    return JsonResponse({'error': 'No visits found for this mother'}, status=404)

            except Mother.DoesNotExist:
                return JsonResponse({'error': 'Registration number not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=400)






