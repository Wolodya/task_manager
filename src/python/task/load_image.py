import requests
import threading

from core.base_task import BaseTask


from core.errors import TaskConfigError


class LoadImageTask(BaseTask):

    def __init__(self, task_config) -> None:
        if task_config['concurrency'] < 2:
            raise TaskConfigError('expected concurrency value more than 1')
        super().__init__(task_config)

    def _create_input_data(self, photo_urls):
        for url in photo_urls:
            self.input_queue.put(((url, ), {}))

    def _get_output_data(self):
        return self.result_manager

    def _process(self, url):
        print('{}. start download photo {}'.format(
            threading.current_thread().getName(), url))
        response = requests.get(url)
        print(response)
        if response.status_code == 200:

            name = url.split('/')[4]
            print(name)
            with open('{}.jpg'.format(name), 'wb') as f:
                f.write(response.content)
        print('{}. end download photo {}'.format(
            threading.current_thread().getName(), url))
        return '{}.jpg was downloaded'.format(name)


if __name__ == '__main__':
    task_config = {'concurrency': 2, 'name': 'load photos'}
    task = LoadImageTask(task_config)
    urls = ['https://www.pexels.com/photo/479454/download/',
            'https://www.pexels.com/photo/7291988/download/',
            'https://www.pexels.com/photo/5591708/download/',
            'https://www.pexels.com/photo/8953401/download/',
            'https://www.pexels.com/photo/7599030/download/',
            'https://www.pexels.com/photo/9254523/download/',
            'https://www.pexels.com/photo/9263838/download/'
            ]
    task.run(urls)
    print(task.result_manager)
