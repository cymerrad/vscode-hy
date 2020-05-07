#!python
import json
import plistlib
import yaml
import sys
import os
import shutil
import re


def traverse_dict(dd, key, cb):
    if type(dd) == dict:
        for k, v in dd.items():
            traverse_dict(v, f"{key}.{k}", cb)
    elif type(dd) == list:
        for ind, el in enumerate(dd):
            traverse_dict(el, f"{key}.{ind}", cb)
    else:
        cb(key, dd)


class yaml_wrap:
    @staticmethod
    def load(fp):
        return yaml.load(fp, Loader=yaml.FullLoader)

    @staticmethod
    def dump(obj, fp=None):
        # TODO(rado) dumping with some strings as literal or folded: https://yaml-multiline.info/
        # dumper = yaml.Dumper()

        return yaml.dump(obj, fp)


class json_wrap:
    @staticmethod
    def load(*args, **kwargs):
        return json.load(*args, **kwargs)

    @staticmethod
    def dump(obj, *args, **kwargs):
        (fails, _) = json_wrap.check_regexes_correctness(obj)

        if len(fails):
            err_msg = f"Found {len(fails)} error{'s' if len(fails) > 1 else ''}"
            footer = "-" * len(err_msg)
            print(footer)
            print(err_msg)

            for where, fail in fails.items():
                print(f"In: {where}\n\t{fail}")

            print(footer)

        return json.dump(obj, *args, **kwargs)

    @staticmethod
    def check_regexes_correctness(dictionary):
        fails = {}
        warnings = {}

        def check_re(key, pattern):
            nonlocal fails
            for ending in ["begin", "match", "end"]:
                if key.endswith(ending):
                    break
            else:
                return

            try:
                rex = re.compile(pattern)
            except re.error as e:
                fails[key] = e

            if rex.match("") and key.endswith("match"):
                fails[key] = "Matches empty string"

        traverse_dict(dictionary, "{}", check_re)
        return fails, warnings


libs = {
    ".json": json_wrap,
    ".yaml": yaml_wrap,
    ".tmLanguage": plistlib,
}


def convert(lib_in, file_in, lib_out, file_out):
    tmp = lib_in.load(file_in)
    lib_out.dump(tmp, file_out)


def main():
    _, filename_in, filename_out, *_ = sys.argv
    assert os.path.exists(filename_in)
    if os.path.exists(filename_out):
        shutil.move(filename_out, filename_out + "_copy")

    lib_in, lib_out = None, None
    for ending in libs.keys():
        if filename_in.endswith(ending):
            lib_in = libs[ending]

        if filename_out.endswith(ending):
            lib_out = libs[ending]

    if lib_in is None or lib_out is None:
        raise Exception("Unsupported conversion pair")

    with open(filename_in, "rb") as fr, open(filename_out, "w") as fw:
        convert(lib_in, fr, lib_out, fw)


if __name__ == "__main__":
    main()
