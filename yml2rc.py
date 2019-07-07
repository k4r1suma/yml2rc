import yaml
import re
import sys
import urllib.request


class Plugin:
    def __init__(self, raw_plug={}, name=None,
                 comment=None, custom=None, repo=None):
        self.repo_regex = re.compile(r'^[\w\-\.]+\/[\w\-\.]+$')
        self.provider = 'https://github.com/'
        self.name = name
        self.comment = comment
        self.custom = custom
        self.repo = repo
        self.raw_plug = raw_plug

    def parse_raw(self):
        typeof_plug = type(self.raw_plug)
        if typeof_plug is str:
            pass
        elif typeof_plug is dict:
            pass
        else:
            raise TypeError


class Config:
    def __init__(self):
        self.plugin_list = []

    def parse_yml(self, path):
        with open(path) as f:
            cfgs = yaml.safe_load(f)
            for cfg in cfgs:
                self.plugin_list.append(Plugin(cfg))

    def generate_rc(self):
        pass
