#!/bin/bash

# Получение списка юнитов
units=$(systemctl list-units --all 'foobar-*' --no-legend --no-pager | awk '{print $1}' | grep -o 'foobar-[^.]*\.service')

if [[ -z "$units" ]]; then
    echo "Не найдено ни одного юнита"
    exit 1
fi

echo "Найдены следующие юниты:"
echo "$units"

for unit in $units; do
    
    # Получение пути к файлу юнита
    unit_path=$(systemctl show -p FragmentPath "$unit" | cut -d= -f2)
    
    if [[ -z "$unit_path" ]]; then
        echo "Не удалось получить путь для юнита $unit"
        exit 1
    fi
    
    echo "Путь к файлу юнита: $unit_path"

    # Остановка сервиса
    systemctl stop "$unit" || { echo "Ошибка остановки $unit"; exit 1; }

    # Извлечение параметров
    working_dir=$(systemctl show -p WorkingDirectory --value "$unit")
    exec_start_full=$(systemctl show -p ExecStart --value "$unit")
    
    # Разбор ExecStart (удаляем { и } если есть)
    exec_start_clean=$(echo "$exec_start_full" | sed 's/^{ //; s/ }$//')
    exec_start_cmd=$(echo "$exec_start_clean" | grep -oP 'path=\K[^;]+')
    exec_start_args=$(echo "$exec_start_clean" | grep -oP 'argv\[\]=\K[^;]+' | sed "s|^$exec_start_cmd ||")

    echo "Рабочая директория: $working_dir"
    echo "Команда запуска: $exec_start_cmd"
    echo "Аргументы: $exec_start_args"

    # Определение новых путей
    service_name=${unit#foobar-}
    service_name=${service_name%.service}
    new_dir="/srv/data/$service_name"
    new_exec="/srv/data/$service_name/$(basename "$exec_start_cmd")"

    # Создание новой директории и копирование файлов
    echo "Создание новой директории $new_dir"
    mkdir -p "$new_dir" || { echo "Ошибка создания директории"; exit 1; }
    cp -a "$working_dir"/. "$new_dir"/ || { echo "Ошибка копирования файлов"; exit 1; }

    # Создание override.conf
    override_dir="/etc/systemd/system/$unit.d"
    mkdir -p "$override_dir"
    
    echo "Создание override.conf с новыми путями"
    cat > "$override_dir/override.conf" <<EOF
[Service]
WorkingDirectory=$new_dir
ExecStart=$new_exec $exec_start_args
EOF

    # Перезагрузка конфигурации и запуск
    systemctl daemon-reload || { echo "Ошибка daemon-reload"; exit 1; }
    systemctl reset-failed "$unit" 2>/dev/null
    systemctl start "$unit" || { echo "Ошибка запуска $unit"; exit 1; }
    
    echo "Проверка статуса:"
    systemctl status "$unit" --no-pager
done
