
from core.base_job import BaseJob
from core.errors import StepConfigError
from task.archive_folder import ArchiveFolderTask
from task.copy_folder import CopyFolderTask
from task.delete_folder import DeleteFolderTask
from task.list_files import ListFilesTask
from task.load_image import LoadImageTask
from task.load_index_html import LoadIndexTask
from task.process_photo import ProcessPhotoTask
from task.read_from_file import ReadFileTask
from task.system_command import SystemCommandTask
from task.write2file import WriteFileTask
from core.base_job2 import BaseMultiprocessingJob
from core.base_step import BaseStep

import os


class FileProcessJob(BaseMultiprocessingJob):
    def run(self):
        return super().run()


class Step(BaseStep):

    def run(self, *args, **kwargs):
        return super().run(*args, **kwargs)


if __name__ == '__main__':

    domains = [{'name': 'google', 'url': 'https://www.google.com/'},
               {'name': 'yahoo', 'url': 'https://www.yahoo.com/'},
               {'name': 'bing', 'url': 'https://www.bing.com/'},
               {'name': 'baidu', 'url': 'https://www.baidu.com/'},
               {'name': 'naver', 'url': 'https://www.naver.com/'},
               ]
    # download_task.run(domains)

    file_job = FileProcessJob('multiprocess step job')
    step1 = Step({'name': 'step1'})
    step1.add_task(ReadFileTask, {'name': 'read_file'}, 'test.txt')

    step2 = Step({'name': 'step2', 'processes': 2})
    step2.add_task(WriteFileTask, {
                   'name': 'write_file'}, 'test22.txt', '%step1.read_file%')
    step2.add_task(LoadIndexTask, {
                   'concurrency': 2, 'name': 'load search index html'}, domains)

    step3 = Step({'name': 'step3'})
    urls = ['https://www.pexels.com/photo/479454/download/',
            'https://www.pexels.com/photo/7291988/download/',
            'https://www.pexels.com/photo/5591708/download/',
            'https://www.pexels.com/photo/8953401/download/',
            'https://www.pexels.com/photo/7599030/download/',
            'https://www.pexels.com/photo/9254523/download/',
            'https://www.pexels.com/photo/9263838/download/'
            ]
    step3.add_task(LoadImageTask, {
                   'concurrency': 2, 'name': 'load photos'}, urls)

    step4 = Step({'name': 'step4'})
    step4.add_task(SystemCommandTask, {'name': 'create folder'}, 'mkdir', 'loaded_photos')

    step5 = Step({'name': 'step5'})
    step5.add_task(SystemCommandTask, {
                   'name': 'create folder'}, 'mkdir', 'processed')

    step6 = Step({'name': 'step6'})
    step6.add_task(SystemCommandTask, {'name': 'move files to folder'}, 'mv', '*.jpg', 'loaded_photos')

    step7 = Step({'name': 'step7'})
    step7.add_task(ListFilesTask, {'name': 'list files in folder'}, 'loaded_photos')

    step8 = Step({'name': 'step8'})
    step8.add_task(ProcessPhotoTask, {'name': 'filter_photos', 'concurrency': 3}, '%step7.list files in folder%')

    step9 = Step({'name': 'step9'})
    step9.add_task(CopyFolderTask, {
                   'name': 'copy_folder'}, 'processed', 'test_folder')

    step10 = Step({'name': 'step10'})
    step10.add_task(ArchiveFolderTask, {
                   'name': 'archive_folder'}, '%step9.copy_folder%', 'zip')

    step11 = Step({'name': 'step11'})
    step11.add_task(SystemCommandTask, {
                    'name': 'delete archive'}, 'rm', '%step10.archive_folder%')

    file_job.add_step(step1)
    file_job.add_step(step2)
    file_job.add_step(step3)
    file_job.add_step(step4)
    file_job.add_step(step5)
    file_job.add_step(step6)
    file_job.add_step(step7)
    file_job.add_step(step8)
    file_job.add_step(step9)
    file_job.add_step(step10)
    file_job.add_step(step11)
    file_job.run()
    print(file_job.result_manager['step2'])
    print(file_job.result_manager['step3'])
    print(file_job.result_manager['step4'])
    print(file_job.result_manager['step5'])
    print(file_job.result_manager['step6'])
    print(file_job.result_manager['step7'])
    print(file_job.result_manager['step8'])
    print(file_job.result_manager['step9'])
    print(file_job.result_manager['step10'])
    # print(file_job.steps[1]['step'].tasks[1]['task'].result_manager)
