import requests
import threading

from core.base_task import BaseTask


from core.errors import TaskConfigError


class LoadIndexTask(BaseTask):

    def __init__(self, task_config) -> None:
        if task_config['concurrency'] < 2:
            raise TaskConfigError('expected concurrency value more than 1')
        super().__init__(task_config)

    def _create_input_data(self, domains):
        for domain in domains:
            self.input_queue.put(((domain, ), {}))

    def _get_output_data(self):
        return self.result_manager        

    def _process(self, download_param):
        print('{}. start download index {}'.format(
            threading.current_thread().getName(), download_param['name']))
        index_page = requests.get(download_param['url'])
        if index_page.status_code == 200:
            with open('{}.html'.format(download_param['name']), 'w') as f:
                f.write(index_page.text)
        print('{}. end download index {}'.format(
            threading.current_thread().getName(), download_param['name']))
        return '{}.html was created'.format(download_param['name'])


if __name__ == '__main__':
    task_config = {'concurrency': 2, 'name': 'load search index html'}
    task = LoadIndexTask(task_config)
    domains = [{'name': 'google', 'url': 'https://www.google.com/'},
               {'name': 'yahoo', 'url': 'https://www.yahoo.com/'},
               {'name': 'bing', 'url': 'https://www.bing.com/'},
               {'name': 'baidu', 'url': 'https://www.baidu.com/'},
               {'name': 'naver', 'url': 'https://www.naver.com/'},
               ]
    task.run(domains)
    print(task.result_manager)
