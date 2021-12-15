import os
import subprocess

from core.base_task import BaseTask


class SystemCommandTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)

    def _get_output_data(self):
        return self.result_manager

    def _process(self, *args):
        print('start {} task'.format(self.name))
        data = subprocess.Popen(
            ' '.join(args), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, err = data.communicate()
        print('end {} task'.format(self.name))
        return out


if __name__ == '__main__':
    task_config = {'name': 'system command'}
    task = SystemCommandTask(task_config)
    task.run('ls', 'loaded_photos')
    print(task.result_manager)
