from tasks import send_mail


if __name__ == '__main__':
    # send_mail.delay()   # 执行 Python main.py 会直接结束返回，无输出(包括print输出也没有)，
    send_mail()          # 执行 python main.py会将整个程序执行完才返回，包括代码里time.sleep()，会悬挂。
    
# 先运行如下：
# celery -A tasks worker --loglevel=info    
# 再运行
# Python main.py
  