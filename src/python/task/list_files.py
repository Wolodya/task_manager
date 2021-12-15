import re
import os
import shutil
from core.base_task import BaseTask

class ListFilesTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)
    
    def _get_output_data(self):
        return self.result_manager

    def _process(self, source):
        print('start {} task'.format(self.name))
        data = os.listdir(source)
        print('end {} task'.format(self.name))
        return data

if __name__ == '__main__':
    task_config = { 'name':'list files in folder'}
    task = ListFilesTask(task_config)
    task.run('loaded_photos')
    print(task.result_manager)