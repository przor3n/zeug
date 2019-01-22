# encoding: utf-8
import logging


class Zeug(object):

    def __init__(self, slots, instructions=None):
        self.slots = slots
        self.environment = dict(**slots)
        self.instructions = instructions
        self.output = None
        self.on = True
        self.single_run = True

    def do(self):
        while self.on:
            try:
                exec(self.instructions, globals(), self.environment)
            except Exception as e:
                logging.error(e)
                raise e
            finally:
                self.update_state()
                self.update_instructions()

    def update_state(self):
        if self.single_run:
            self.on = False

        self.output = self.environment.get('output', None)

    def update_instructions(self):
        pass

    def clean(self):
        for name, tool in self.slots.items():
            tool.clean()
