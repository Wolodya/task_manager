import re
import os

from core.base_task import BaseTask

class DeleteFolderTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)
    
    def _get_output_data(self):
        return self.result_manager

    def _process(self, input):
        print('start {} task'.format(self.name))
        data = os.system(f'rm -rf {input}')
        print('end {} task'.format(self.name))
        return data

if __name__ == '__main__':
    task_config = { 'name':'move folder'}
    task = DeleteFolderTask(task_config)
    task.run('test')
    print(task.result_manager)