import mailchimp
from celery import task

@task()
def subscribe_to_list(email):
    #Subscribe user to codesters mailing list
    list = mailchimp.utils.get_connection().get_list_by_id('c9497f5882')
    list.subscribe(email, {'EMAIL':email})
