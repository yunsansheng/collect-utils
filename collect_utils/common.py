# -*- coding: UTF-8 -*-

"""
Author: Henry Wang
Date: 2023-07-20 16:48
Short Description:

Change History:

"""


def parse_ac_attrs(attrs):
    full_attr = {}
    for line in attrs:
        assert line["type"] in {"string", "int", "list", "checkbox"}, "parse_ac_attrs中发现类型未出现过"
        name = line["name"]
        try:
            if line["type"] == 'string':
                full_attr = line["user_input"]
            elif line["type"] == 'int':
                full_attr = int(line["user_input"])
            elif line["type"] in {"list", "checkbox"}:
                key_idx = line["values"].index(line["user_input"])
                value = line["keys"][key_idx]
                full_attr[name] = value

        except:
            full_attr[name] = None
    return full_attr


if __name__ == "__main__":
    pass
