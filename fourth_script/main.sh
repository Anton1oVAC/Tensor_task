#!/bin/bash

# Получение списка юнитов
units=$(systemctl list-units --all 'foobar-*' --no-legend --no-pager | awk '{print $1}' | grep -o 'foobar-[^.]*\.service')

if [[ -z "$units" ]]; then
    echo "Не найдено ни одного юнита"
    exit 1
fi

echo "Найдены следующие юниты:"
echo "$units"


# Обрабатка каждого юнита
for unit in $units; do
    echo "Обрабатываю юнит: $unit"
    
    # Получение пути к файлу юнита
    unit_path=$(systemctl show -p FragmentPath "$unit" | cut -d= -f2)
    
    if [[ -z "$unit_path" ]]; then
        echo "Не удалось получить путь для юнита $unit"
        exit 1
    fi
    
    echo "Путь к файлу юнита: $unit_path"
    
   
done
