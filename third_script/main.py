import json
import argparse
from itertools import product


def parse_args():
    parser = argparse.ArgumentParser(description='Генератор версий на основе шаблонов')
    parser.add_argument('version', help='Текущая версия продукта')
    parser.add_argument('config_file', help='Путь к конф файлу')
    return parser.parse_args()


def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)


def generate_version_numbers(template):
    parts = template.split('.')
    wildcard_indices = [i for i, part in enumerate(parts) if part == '*']
    
    if not wildcard_indices:
        return [template]
    
    # Генерируем все возможные комбинации
    combinations = product(range(10), repeat=len(wildcard_indices))
    
    versions = []
    for combo in combinations:
        new_parts = parts.copy()
        for i, idx in enumerate(wildcard_indices):
            new_parts[idx] = str(combo[i])
        versions.append('.'.join(new_parts))
    
    # Возвращаем 2 уникальных варианта
    return sorted(list(set(versions))[:2])


def compare_versions(v1, v2):
    v1_parts = list(map(int, v1.split('.')))
    v2_parts = list(map(int, v2.split('.')))
    
    for p1, p2 in zip(v1_parts, v2_parts):
        if p1 < p2:
            return -1
        elif p1 > p2:
            return 1
    
    if len(v1_parts) < len(v2_parts):
        return -1
    elif len(v1_parts) > len(v2_parts):
        return 1
    
    return 0


def main():
    args = parse_args()
    current_version = args.version
    config_file = args.config_file
    
    try:
        config = load_config(config_file)
    except Exception as e:
        print(f"Ошибка загрузки конфигурационного файла: {e}")
        return
    
    all_versions = []
    
    print("\nШаблон - Версия:")
    for service, template in config.items():
        versions = generate_version_numbers(template)
        print(f"{service} ({template}): {', '.join(versions)}")
        all_versions.extend(versions)
    
    # Удаляем дубликаты и сортируем
    unique_versions = sorted(list(set(all_versions)), key=lambda x: list(map(int, x.split('.'))))
    
    print("\nСортировка сгенерированных версий:")
    for version in unique_versions:
        print(version)
    
    print(f"\nВерсии старше текущей {current_version}:")
    older_versions = [v for v in unique_versions if compare_versions(v, current_version) < 0]
    for version in older_versions:
        print(version)

if __name__ == '__main__':
    main()
