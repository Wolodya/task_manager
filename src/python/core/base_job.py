
import re
from concurrent.futures import ThreadPoolExecutor

class BaseJob:
    def __init__(self, name) -> None:
        self.name = name
        self.tasks = {}
        self.order = 1
        self.pattern = re.compile(r'^%(\d+)%$')

    def add_task(self, task_class, task_config, *args, **kwargs):
        task = task_class(task_config)
        self.tasks[self.order] = {
            'instance': task, 'result': None, 'args': args, 'kwargs': kwargs}
        self.order += 1

    def run(self):
        for key, task in sorted(self.tasks.items()):
            args_params = []
            kwargs_params = {}
            for param in task['args']:
                found = re.search(self.pattern, param)
                if found:
                    result_key = int(found.group(1))
                    args_params.append(self.tasks[result_key]['result'])
                else:
                    args_params.append(param)
            for key in task['kwargs']:
                found = re.search(self.pattern, task['kwargs'][key])
                if found:
                    result_key = int(found.group(1))
                    kwargs_params[key] = self.tasks[result_key]['result']
                else:
                    kwargs_params[key] = task['kwargs'][key]
            
            result = task['instance'].run(*args_params, **kwargs_params)
            self.tasks[key]['result'] = result
