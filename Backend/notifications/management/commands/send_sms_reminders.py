
# import datetime
# from django.core.management.base import BaseCommand
# from django.conf import settings
# from django.utils import timezone
# import africastalking
# from mother.models import Mother_visit

# # Initialize Africa's Talking API
# africastalking.initialize(settings.AFRICAS_TALKING_USERNAME, settings.AFRICAS_TALKING_API_KEY)
# sms = africastalking.SMS

# class Command(BaseCommand):
#     help = 'Send SMS reminders to parents for their upcoming visits'

#     def handle(self, *args, **kwargs):
#         today = timezone.now().date()
#         reminder_days = [10, 5, 3, 2, 1]

#         for days_before in reminder_days:
#             visit_date = today + datetime.timedelta(days=days_before)
#             visits = Mother_visit.objects.filter(date_of_next_visit=visit_date)

#             for visit in visits:
#                 message = f"Dear {visit.mother_name}, you have a scheduled visit on {visit.date_of_next_visit}. Please make sure to attend."
#                 phone_number = visit.mother.phone

#                 # Debug print statements
#                 # self.stdout.write(f"Phone number: {phone_number}, Type: {type(phone_number)}")
#                 # self.stdout.write(f"Message: {message}, Type: {type(message)}")

#                 # Ensure phone_number and message are strings
#                 if not isinstance(phone_number, str):
#                     phone_number = str(phone_number)
#                 if not isinstance(message, str):
#                     message = str(message)

#                 try:
#                     response = sms.send(message, [phone_number])
#                     self.stdout.write(self.style.SUCCESS(f"Successfully sent reminder to {phone_number}"))
#                 except Exception as e:
#                     self.stdout.write(self.style.ERROR(f"Failed to send reminder to {phone_number}: {str(e)}"))



# import datetime
# from django.core.management.base import BaseCommand
# from django.conf import settings
# from django.utils import timezone
# import africastalking
# from mother.models import Mother_visit, Mother
# from child.models import Child_visit, Child

# # Initialize Africa's Talking API
# africastalking.initialize(settings.AFRICAS_TALKING_USERNAME, settings.AFRICAS_TALKING_API_KEY)
# sms = africastalking.SMS

# class Command(BaseCommand):
#     help = 'Send SMS reminders to parents for their upcoming visits'

#     def handle(self, *args, **kwargs):
#         today = timezone.now().date()
#         reminder_days = [10, 5, 3, 2, 1]

#         for days_before in reminder_days:
#             visit_date = today + datetime.timedelta(days=days_before)
            
#             # Send reminders for mother visits
#             mother_visits = Mother_visit.objects.filter(date_of_next_visit=visit_date)
#             for visit in mother_visits:
#                 self.send_reminder(visit.mother.phone, visit.mother_name, visit.date_of_next_visit, is_child=False)
            
#             # Send reminders for child visits
#             child_visits = Child_visit.objects.filter(return_date=visit_date)
#             for visit in child_visits:
#                 mother = visit.child.mother
#                 self.send_reminder(mother.phone, visit.child.child_name, visit.return_date, is_child=True)
    
#     def send_reminder(self, phone_number, name, visit_date, is_child):
#         if is_child:
#             message = f"Dear, your child {name}has a scheduled visit on {visit_date}. Please make sure to attend."
#         else:
#             message = f"Dear {name}, you have a scheduled visit on {visit_date}. Please make sure to attend."

#         # Ensure phone_number and message are strings
#         if not isinstance(phone_number, str):
#             phone_number = str(phone_number)
#         if not isinstance(message, str):
#             message = str(message)
        
#         try:
#             response = sms.send(message, [phone_number])
#             self.stdout.write(self.style.SUCCESS(f"Successfully sent reminder to {phone_number}"))
#         except Exception as e:
#             self.stdout.write(self.style.ERROR(f"Failed to send reminder to {phone_number}: {str(e)}"))


import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone
import africastalking
from mother.models import Mother_visit, Mother
from child.models import Child_visit, Child

# Initialize Africa's Talking API
africastalking.initialize(settings.AFRICAS_TALKING_USERNAME, settings.AFRICAS_TALKING_API_KEY)
sms = africastalking.SMS

class Command(BaseCommand):
    help = 'Send SMS reminders to parents for their upcoming visits'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        reminder_days = [10, 5, 3, 2, 1]

        for days_before in reminder_days:
            visit_date = today + datetime.timedelta(days=days_before)
            
            # Send reminders for mother visits
            mother_visits = Mother_visit.objects.filter(date_of_next_visit=visit_date)
            for visit in mother_visits:
                self.send_reminder(visit.mother.phone, visit.mother.mother_name, None, visit.date_of_next_visit, is_child=False)
            
            # Send reminders for child visits
            child_visits = Child_visit.objects.filter(return_date=visit_date)
            for visit in child_visits:
                mother = visit.child.mother
                self.send_reminder(mother.phone, mother.mother_name, visit.child.child_name, visit.return_date, is_child=True)
    
    def send_reminder(self, phone_number, mother_name, child_name, visit_date, is_child):
        if is_child:
            message = f"Dear {mother_name}, your child {child_name} has a scheduled visit on {visit_date}. Please make sure to attend."
        else:
            message = f"Dear {mother_name}, you have a scheduled visit on {visit_date}. Please make sure to attend."

        # Ensure phone_number and message are strings
        if not isinstance(phone_number, str):
            phone_number = str(phone_number)
        if not isinstance(message, str):
            message = str(message)
        
        try:
            response = sms.send(message, [phone_number])
            self.stdout.write(self.style.SUCCESS(f"Successfully sent reminder to {phone_number}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to send reminder to {phone_number}: {str(e)}"))
