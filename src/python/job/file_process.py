
from core.base_job import BaseJob
from task.load_index_html import LoadIndexTask
from task.read_from_file import ReadFileTask
from task.write2file import WriteFileTask


class FileProcessJob(BaseJob):
    def run(self):
        return super().run()


if __name__ == '__main__':

    domains = [{'name':'google','url':'https://www.google.com/'},
    {'name':'yahoo','url':'https://www.yahoo.com/'},
    {'name':'bing','url':'https://www.bing.com/'},
    {'name':'baidu','url':'https://www.baidu.com/'},
    {'name':'naver','url':'https://www.naver.com/'},
    ]
    # download_task.run(domains)

    file_job = FileProcessJob('rest')
    file_job.add_task(ReadFileTask, {'name': 'read_file'}, 'test.txt')
    file_job.add_task(WriteFileTask, {'name': 'write_file'}, 'test22.txt', '%1%')
    file_job.add_task(LoadIndexTask, {'concurrency': 4, 'name': 'load search index html'}, domains)
    file_job.run()
