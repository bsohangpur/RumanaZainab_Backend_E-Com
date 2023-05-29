FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    systemd \
    nginx \
    python3 \
    nodejs \
    python3-pip \
    python3-venv

WORKDIR /app
COPY . /app

RUN python3 -m venv env && \
    . env/bin/activate && \
    pip install -r requirements.txt && \
    pip install gunicorn && \
    deactivate

RUN echo '[Unit]\n\
    Description=Main socket\n\
    \n\
    [Socket]\n\
    ListenStream=/run/Main.sock\n\
    \n\
    [Install]\n\
    WantedBy=sockets.target\n' > /etc/systemd/system/Main.socket

RUN echo '[Unit]\n\
    Description=Main daemon\n\
    Requires=Main.socket\n\
    After=network.target\n\
    \n\
    [Service]\n\
    User=ubuntu\n\
    Group=www-data\n\
    WorkingDirectory=/app/\n\
    ExecStart=/app/env/bin/gunicorn \n\
    --access-logfile - \n\
    --workers 3 \n\
    --bind unix:/run/Main.sock \n\
    Main.wsgi:application\n\
    \n\
    [Install]\n\
    WantedBy=multi-user.target\n' > /etc/systemd/system/Main.service

ENV init /lib/systemd/systemd

RUN systemctl enable Main.socket

RUN echo 'server { \n\
    listen 80; \n\
    server_name localhost;\n\
\n\
    location = /favicon.ico { access_log off; log_not_found off; }\n\
location / {\n\
        root /path/to/react/build;\n\
        index index.html;\n\
        try_files $uri $uri/ /index.html;\n\
    }\n\
\n\
    location /static/ {\n\
        root /app;\n\
    }\n\
    location /media/ {\n\
        root /app;\n\
    }\n\
\n\
\n\
    location /api {\n\
        include proxy_params;\n\
        proxy_pass http://unix:/run/Main.sock;\n\
    }\n\
}' > /etc/nginx/sites-available/rumanazainab.conf

RUN ln -s /etc/nginx/sites-available/rumanazainab.conf /etc/nginx/sites-enabled

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
