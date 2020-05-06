#!python
import json
import plistlib
import yaml
import sys
import os
import shutil


def convert(lib_in, file_in, lib_out, file_out):
    tmp = lib_in.load(file_in)
    lib_out.dump(tmp, file_out)


class yaml_wrap:
    @staticmethod
    def load(fp):
        return yaml.load(fp, Loader=yaml.FullLoader)

    @staticmethod
    def dump(obj, fp=None):
        # TODO(rado) dumping with some strings as literal or folded: https://yaml-multiline.info/
        # dumper = yaml.Dumper()

        return yaml.dump(obj, fp)


libs = {
    ".json": json,
    ".yaml": yaml_wrap,
    ".tmLanguage": plistlib,
}


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
