import re
import shutil

from core.base_task import BaseTask

class DeleteFolderTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)
    
    def _get_output_data(self):
        return self.result_manager

    def _process(self, input):
        print('start {} task'.format(self.name))
        shutil.rmtree(input)
        print('end {} task'.format(self.name))
        return None

if __name__ == '__main__':
    task_config = { 'name':'delete folder'}
    task = DeleteFolderTask(task_config)
    task.run('test')
    print(task.result_manager)