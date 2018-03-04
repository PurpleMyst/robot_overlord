#!/usr/bin/env python3
import os
import shlex
import subprocess


class Program:
    def __init__(self, name, requires, location, setup, start):
        self.name = name
        self.requires = requires
        self.location = location
        self.setup_commands = setup
        self.start = start

        self._fetched = False
        self._directory = None

    def _run_command(self, command):
        if isinstance(command, str):
            command = shlex.split(command)

        return subprocess.run(command, check=True)

    def install_requirements(self):
        for item in self.requires:
            if item == "python3":
                pass
            else:
                raise ValueError("Unsupported requirement %r" % item)

    def fetch(self):
        if self.location["type"] == "local":
            self._directory = self.location["directory"]
        else:
            raise ValueError("Unsupported location %r" % self.location)

        self._fetched = True

    def setup(self):
        for command in self.setup_commands:
            self._run_command(command)

    def run(self):
        if not self._fetched:
            print(self.name, "was run without being fetched")

        print("Starting", self.name)
        os.chdir(self._directory)
        self._run_command(self.start)
