import concurrent.futures
import multiprocessing
import threading
import queue

from core.errors import TaskConfigError


class BaseTask:

    def __init__(self, task_config: dict) -> None:
        '''
        name - task name
        concurrency: 
        0 - main thread
        1 - child trhead
        1< - child trheads
        input - task input data

        '''
        self.task_config = task_config
        self.input_queue = queue.Queue()
        self.result_manager = {}

    def _worker(self):
        while not self.input_queue.empty():
            args, kwargs = self.input_queue.get()
            res = self._process(*args, **kwargs)
            thread_name = threading.current_thread().getName()
            if thread_name in self.result_manager:
                self.result_manager[thread_name].append(res)
            else:
                self.result_manager[thread_name] = [res]
            self.input_queue.task_done()

    def _create_input_data(self, *args, **kwargs):
        raise NotImplementedError

    def _get_output_data(self):
        raise NotImplementedError

    def run(self, *args, **kwargs):
        print('{}. {}. start {} task'.format(multiprocessing.current_process().name,
                                             threading.current_thread().getName(), self.name))
        if self.task_config['concurrency'] == 0:
            res = self._process(*args, **kwargs)
            print(res)
            self.result_manager = res
        elif self.task_config['concurrency'] > 0:
            threads = []
            self._create_input_data(*args, **kwargs)
            for _ in range(self.task_config['concurrency']):
                thread = threading.Thread(target=self._worker)
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()
        else:
            raise TaskConfigError(
                'invalid config. concurrency must be 0 or more')
        print('{}. {}. end {} task'.format(multiprocessing.current_process().name,
                                           threading.current_thread().getName(), self.name))
        return self._get_output_data()

    def _process(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def name(self):
        return self.task_config['name']
