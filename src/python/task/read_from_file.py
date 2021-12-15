from core.base_task import BaseTask
from core.errors import TaskRunError

class ReadFileError(TaskRunError):
    pass

class ReadFileTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)
    
    def _get_output_data(self):
        return self.result_manager

    def _process(self, input):
        print('start {} task'.format(self.name))
        print(input)
        data = ''
        try:
            with open(input) as f:
                data=f.read()
            print('end {} task'.format(self.name))
        except (ReadFileError, Exception) as e:
            print('exc starts here')
            return f"Error: {e}"
        return data

if __name__ == '__main__':
    task_config = { 'name':'read_from_file'}
    task = ReadFileTask(task_config)
    task.run('test.txt')
    print(task.result_manager)