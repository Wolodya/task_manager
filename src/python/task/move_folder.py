import re
import os

from core.base_task import BaseTask

class MoveFolderTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)
    
    def _get_output_data(self):
        return self.result_manager

    def _process(self, source, target):
        print('start {} task'.format(self.name))
        data = os.system(f'mv {source} {target}')
        print('end {} task'.format(self.name))
        return data

if __name__ == '__main__':
    task_config = { 'name':'move folder'}
    task = MoveFolderTask(task_config)
    task.run('processed', 'test')
    print(task.result_manager)