import re
import os
import shutil
from core.base_task import BaseTask

class CopyFolderTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)
    
    def _get_output_data(self):
        return self.result_manager

    def _process(self, source, target):
        print('start {} task'.format(self.name))
        data = shutil.copytree(source, target)
        print('end {} task'.format(self.name))
        return data

if __name__ == '__main__':
    task_config = { 'name':'copy folder'}
    task = CopyFolderTask(task_config)
    task.run('processed', 'test')
    print(task.result_manager)