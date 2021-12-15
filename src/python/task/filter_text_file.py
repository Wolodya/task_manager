import re
import os

from core.base_task import BaseTask

class FilterStringTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)
    
    def _get_output_data(self):
        return self.result_manager

    def _process(self, file_name, regex_str):
        print('start {} task'.format(self.name))
        data = os.system(f"sed '{regex_str}' {file_name}")
        # data = re.sub(r'p\w+', r'', input)
        print('end {} task'.format(self.name))
        return data

if __name__ == '__main__':
    task_config = { 'name':'filter_file'}
    task = FilterStringTask(task_config)
    task.run('sample1.txt', 's/p[^ ]*//g')
    print(task.result_manager)