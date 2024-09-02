import pandocfilters as pf
import re
import json

l = []

def list_filter(key, value, format, meta):
    l.append([key, value])
    return None

if __name__ == "__main__":
    pf.toJSONFilter(list_filter)
    string = json.dumps(l, indent=4, ensure_ascii=False)
    with open('md2dw.json', 'w', encoding='utf-8') as fp:
        fp.write(string)