import re
import multiprocessing


class BaseStep:

    def __init__(self, step_config) -> None:
        self.tasks = {}
        self.step_config = step_config
        self.order = 1
        self.result_manager = multiprocessing.Manager().dict()
    
    def _worker(self, key):
        self.tasks[key]['task'].run(*self.tasks[key]['args'], **self.tasks[key]['kwargs'])
        self.result_manager[self.tasks[key]['task'].name] = self.tasks[key]['task'].result_manager

    def add_task(self, task_class, task_config, *args, **kwargs):
        task = task_class(task_config)
        self.tasks[self.order] = {'task': task, 'args': args, 'kwargs': kwargs}
        self.order += 1

    def run(self):
        if len(self.tasks) == 1:
            result = self.tasks[1]['task'].run(*self.tasks[1]['args'], **self.tasks[1]['kwargs'])
            self.result_manager[self.tasks[1]['task'].name] = self.tasks[1]['task'].result_manager
            return result
        elif len(self.tasks) > 1:
            processes = []
            for key in self.tasks:
                process = multiprocessing.Process(target=self._worker, args=(key,))
                process.start()
                processes.append(process)
            for process in processes:
                process.join()