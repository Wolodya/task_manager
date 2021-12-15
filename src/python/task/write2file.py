from core.base_task import BaseTask

class WriteFileTask(BaseTask):

    def __init__(self, task_config) -> None:
        task_config['concurrency'] = 0
        super().__init__(task_config)

    def _get_output_data(self):
        return self.result_manager

    def _process(self, file_path,input):
        print('start {} task'.format(self.name))
        with open(file_path,'w') as f:
            f.write(input)
        print('end {} task'.format(self.name))


if __name__ == '__main__':
    task_config = { 'name':'write2file'}
    task = WriteFileTask(task_config)
    task.run('test_write.txt', 'test string')