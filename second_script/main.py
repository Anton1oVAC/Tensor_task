import git
from log import logger
import os

repo_url = 'https://github.com/Anton1oVAC/s21_Matrix_oop'
dest_dir = 's21'

# Клонирование репо
def install_repo(repo_url, dest_dir):
    # Проверяем, существует ли директория
    if os.path.exists(dest_dir):
        logger.error(f"Директория {dest_dir} уже существует. Завершение.")
        return None
    
    logger.info(f"Клонирование репозитория {repo_url}")

    repo = git.Repo.clone_from(repo_url, dest_dir)
    logger.info(f"Репозиторий успешно клонирован в {dest_dir}")
    return repo


def main():
    try:
        result = install_repo(repo_url, dest_dir)
        if result is None:  # Если директория уже существует
            return 1
        
        logger.info("Скрипт успешно завершен")
        return 0
    except Exception as e:
        logger.error(f"Скрипт завершился с ошибкой: {e}")
        return 1

if __name__ == '__main__':
    exit(main())