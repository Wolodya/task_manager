import re
import os
import shutil
from core.base_task import BaseTask

class ArchiveFolderTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)
    
    def _get_output_data(self):
        return self.result_manager

    def _process(self, source, format):
        print('start {} task'.format(self.name))
        print(source)
        data = shutil.make_archive(source, format, source)
        print('end {} task'.format(self.name))
        return data

if __name__ == '__main__':
    task_config = { 'name':'archive folder'}
    task = ArchiveFolderTask(task_config)
    task.run('test', 'zip')
    print(task.result_manager)