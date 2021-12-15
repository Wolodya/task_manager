
import re
import functools

from core.base_step import BaseStep


class BaseMultiprocessingJob:
    def __init__(self, name) -> None:
        self.name = name
        self.steps = {}
        self.step = 1
        self.pattern = re.compile(r'^%(.+)%$')
        self.result_manager = {}

    def add_step(self, step: BaseStep):
        self.steps[self.step] = {'step': step,
                                 'result': None}
        self.step += 1

    def run(self):

        print('here in step')
        for key, step in sorted(self.steps.items()):
            for index in step['step'].tasks:
                args_params = []
                kwargs_params = {}
                for arg in step['step'].tasks[index]['args']:
                    try:
                        found = re.search(self.pattern, arg)
                        if found:
                            result_path = found.group(1).split('.')
                            result_value = functools.reduce(
                                lambda d, key: d[key], result_path, self.result_manager)
                            args_params.append(result_value)
                        else:
                            args_params.append(arg)
                    except TypeError:
                        args_params.append(arg)
                # for kwarg in step['step'].tasks[index]['kwargs']:
                #     found = re.search(self.pattern, step['step'].tasks[index]['kwargs'][kwarg])
                #     if found:
                #         result_path = found.group(1).split('.')
                #         result_value = functools.reduce(
                #             lambda d, key: d[key], result_path, self.result_manager)
                #         kwargs_params[kwarg] = result_value
                #     else:
                #         kwargs_params[kwarg] = step['step'].tasks[index]['kwargs'][kwarg]
                self.steps[key]['step'].tasks[index]['args'] = args_params
                self.steps[key]['step'].tasks[index]['kwargs'] = kwargs_params
            
            result = step['step'].run()
            self.steps[key]['result'] = result
            self.result_manager[step['step'].step_config['name']
                                ] = step['step'].result_manager
