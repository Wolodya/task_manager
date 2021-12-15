import re
import os
from subprocess import Popen
import shutil
from core.base_task import BaseTask

class CountWordsTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)
    
    def _get_output_data(self):
        return self.result_manager

    def _process(self, input):
        print('start {} task'.format(self.name))
        data = os.system(f'wc -w {input}')
        print('end {} task'.format(self.name))
        return data

if __name__ == '__main__':
    task_config = { 'name':'filter_file'}
    task = CountWordsTask(task_config)
    task.run('sample1.txt')
    print(task.result_manager)