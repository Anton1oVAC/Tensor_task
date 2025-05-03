from log import logger
from install_repo import install_repo
from clean_dir import clean_directory
from create_json_file import create_json
from create_arch import create_archive

repo_url = 'https://github.com/Anton1oVAC/s21_Matrix_oop'
dest_dir = 's21_Matrix_oop'
source_path = 'src'
version = '0.1.1'


def main():
    try:

        repo_dir = install_repo(repo_url, dest_dir) 
        create_dir = clean_directory(dest_dir, source_path) 
        create_json(source_path, version)
        create_archive(source_path)
        
        if repo_dir and create_dir is None:  # Если директория уже существует
            return 1
        
        logger.info("Скрипт успешно завершен")
        return 0
    except Exception as e:
        logger.error(f"Скрипт завершился с ошибкой: {e}")
        return 1

if __name__ == '__main__':
    exit(main())