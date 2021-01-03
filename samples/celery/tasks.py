from celery import Celery
import time

app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')

@app.task
def send_mail():
    print('邮件发送开始。。。')
    time.sleep(12)
    print('邮件发送结束')
    
    
# celery -A tasks worker --loglevel=info    