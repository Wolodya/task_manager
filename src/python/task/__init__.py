# mapper
# map string to class name
from .archive_folder import ArchiveFolderTask
from .read_from_file import ReadFileTask
from .write2file import WriteFileTask
from .copy_folder import CopyFolderTask
from .count_words import CountWordsTask
from .delete_folder import DeleteFolderTask
from .filter_text_file import FilterStringTask
from .list_files import ListFilesTask
from .load_image import LoadImageTask
from .load_index_html import LoadIndexTask
from .move_folder import MoveFolderTask
from .process_photo import ProcessPhotoTask
from .rename_folder import DeleteFolderTask
from .system_command import SystemCommandTask


TASK_MAP = {
    'WriteFileTask': WriteFileTask,
    'ReadFileTask': ReadFileTask,
    'ArchiveFolderTask': ArchiveFolderTask,
    'CopyFolderTask': CopyFolderTask,
    'CountWordsTask': CountWordsTask,
    'DeleteFolderTask': DeleteFolderTask,
    'FilterStringTask': FilterStringTask,
    'ListFilesTask': ListFilesTask,
    'LoadImageTask': LoadImageTask,
    'LoadIndexTask': LoadIndexTask,
    'MoveFolderTask': MoveFolderTask,
    'ProcessPhotoTask': ProcessPhotoTask,
    'SystemCommandTask': SystemCommandTask
}
