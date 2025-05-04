#!/bin/bash

units=$(systemctl list-units --all 'foobar-*' --no-legend --no-pager | awk '{print $1}' | grep -o 'foobar-[^.]*\.service')

if [[ -z "$units" ]]; then
    echo "Не найдено ни одного юнита"
    exit 1
fi

echo "Найдены следующие юниты:"
echo "$units"

