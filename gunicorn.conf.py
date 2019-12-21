import multiprocessing

command = '/root/.local/share/virtualenvs/first-we8fLymr/bin/gunicorn'
bind = "0.0.0.0:5000"
workers = 2  #workers是工作进程数，一般设置成：服务器CPU个数 + 1
errorlog = 'gunicorn.error.log'
accesslog = 'gunicorn.access.log'
loglevel = 'debug'