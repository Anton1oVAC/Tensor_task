#!/bin/bash

# Создание рабочей директории тест юнита
mkdir -p /opt/misc/test_service


# Создание простого демон-скрипт
tee /opt/misc/test_service/foobar-daemon >/dev/null <<'EOF'
#!/bin/bash
while true; do
    echo "$(date) - Test service is running" >> /opt/misc/test_service/service.log
    sleep 5
done
EOF

chmod +x /opt/misc/test_service/foobar-daemon


# Создание systemd юнит
tee /etc/systemd/system/foobar-test_service.service >/dev/null <<EOF
[Unit]
Description=Foobar Test Service

[Service]
WorkingDirectory=/opt/misc/test_service
ExecStart=/opt/misc/test_service/foobar-daemon
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF



systemctl daemon-reload

systemctl enable foobar-test_service.service

systemctl start foobar-test_service.service

systemctl status foobar-test_service.service