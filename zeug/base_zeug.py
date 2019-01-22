# encoding: utf-8
import logging
from zeug.zeug_tools import Tool


class Zeug(object):
    def __init__(self, tools, slots, instructions):
        self.tools = tools
        self.environment = {}
        self.environment.update(tools)
        self.environment.update(slots)
        self.instructions = instructions
        self.output = None
        self.on = True
        self.single_run = True

    def prepare(self, *args):
        raise NotImplementedError("You have to implement me")

    def on_exception(self, exception):
        raise NotImplementedError("You have to implement me")

    def do(self):
        while self.on:
            try:
                exec(self.instructions, globals(), self.environment)
            except Exception as e:
                logging.error(e)
                self.on_exception(e)
                raise e
            finally:
                self.update_state()

    def update_state(self):
        if self.single_run:
            self.on = False

        self.output = self.environment.get('output', None)

    def clean(self):
        for key, tool in self.tools.items():
            tool.clean()
