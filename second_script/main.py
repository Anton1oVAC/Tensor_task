from log import logger
from install_repo import install_repo
from clean_dir import clean_directory

repo_url = 'https://github.com/Anton1oVAC/s21_Matrix_oop'
dest_dir = 's21'
source_path = 'src'


def main():
    try:
        repo_dir = install_repo(repo_url, dest_dir); clean_directory(dest_dir, source_path)
        if repo_dir is None:  # Если директория уже существует
            return 1
        
        logger.info("Скрипт успешно завершен")
        return 0
    except Exception as e:
        logger.error(f"Скрипт завершился с ошибкой: {e}")
        return 1

if __name__ == '__main__':
    exit(main())