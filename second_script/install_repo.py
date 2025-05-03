from log import logger
import os
import git

# Клонирование репо
def install_repo(repo_url, dest_dir):
    
    if os.path.exists(dest_dir):
        logger.error(f"Директория {dest_dir} уже существует. Завершение.")
        return None
    
    logger.info(f"Клонирование репозитория {repo_url}")
    repo = git.Repo.clone_from(repo_url, dest_dir)
    logger.info(f"Репозиторий успешно клонирован в {dest_dir}")
    return repo