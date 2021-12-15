from core.base_step import BaseStep
from task.read_from_file import ReadFileTask


class StepFileRead(BaseStep):

    def run(self, *args, **kwargs):
        return super().run(*args, **kwargs)

if __name__ == '__main__':
    step = StepFileRead({'name': 'read files'})
    step.add_task(ReadFileTask, {'name': 'read sample1'} , 'sample1.txt')
    step.add_task(ReadFileTask, {'name': 'read sample2'} , 'sample2.txt')
    step.add_task(ReadFileTask, {'name': 'read sample2'} , 'sample3.txt')
    step.run()
    print(step.result_manager['read sample1'])
