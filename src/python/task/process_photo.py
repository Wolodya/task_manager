from PIL import Image, ImageFilter
import os
from core.errors import TaskConfigError

from core.base_task import BaseTask

class ProcessPhotoTask(BaseTask):

    def __init__(self, task_config) -> None:
        if task_config['concurrency'] < 2:
            raise TaskConfigError('expected concurrency value more than 1')
        super().__init__(task_config)

    def _create_input_data(self, paths):
        for path in paths:
            self.input_queue.put(((path, ), {}))

    def _get_output_data(self):
        return self.result_manager

    def _process(self, input):
        print('start {} task'.format(self.name))
        photo = Image.open(f'loaded_photos/{input}')
        photo = photo.filter(ImageFilter.MedianFilter(3))
        photo.save(f'processed/{os.path.basename(input) }')
        print('end {} task'.format(self.name))

if __name__ == '__main__':
    task_config = { 'name':'filter_photo'}
    task = ProcessPhotoTask(task_config)
    task.run('479454.jpg')
    print(task.result_manager)