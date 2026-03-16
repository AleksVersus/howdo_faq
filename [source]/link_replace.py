import json
import os
import re

OLD_COMM_LINK = re.compile(r"https?://qsp\.org/index\.php\?option\=com_agora&task\=topic[^/\\\(\)\s\"\']*")
COMMENT = re.compile(r'#p(\d+)')
TOPIC = re.compile(r'\&id\=(\d+)')
Path = str

def j(file_path:Path) -> None:
    with open(file_path, 'r', encoding='utf-8') as fp:
        return json.load(fp)

def search_files(folder_path:Path) -> list[Path]:
    md_files: list[Path] = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(os.path.join(root, file)))
    return md_files

def read_file(file_path:Path) -> str:
    with open(file_path, 'r', encoding='utf-8') as fp:
        return fp.read()

def write_file(file_path:Path, text:str) -> None:
    with open(file_path, 'w', encoding='utf-8') as fp:
        fp.write(text)

def replace_links(text:str, comments_id_map:dict, topic_id_map:dict) -> str:
    all_links = OLD_COMM_LINK.findall(text)
    for link in all_links:
        comment = COMMENT.search(link)
        if comment:
            cid = comments_id_map.get(comment.group(1), -1)
            if cid == -1:
                print(f'error cid {comment.group(1)} in {link}')
                continue
            text = text.replace(link, f'https://qsp.org/forum/comments/{cid}')
            continue
        topic = TOPIC.search(link)
        if topic:
            tid = topic_id_map.get(topic.group(1), -1)
            if tid == -1:
                print(f'error tid {topic.group(1)} in {link}')
                continue
            text = text.replace(link, f'https://qsp.org/forum/{tid}')
            continue
        print(link)
    return text

def main() -> None:
    comments_id_map = j('forum_comments_id_map.json')
    topic_id_map = j('forum_topics_id_map.json')

    md_files: list[Path] = []
    md_files.extend(search_files('../docs'))
    md_files.extend(search_files('../blog'))
    for md_file in md_files:
        text = read_file(md_file)
        new_text = replace_links(text, comments_id_map, topic_id_map)
        if new_text != text:
            write_file(md_file, new_text)


if __name__ == "__main__":
    main()
