import os
import json
from dotenv import load_dotenv

load_dotenv(".env")

bookmark_path = os.getenv("BROWSER_PATH")

def main():
    with open(bookmark_path, 'r') as bookmark:
        # stores the bookmark data into a python dict
        data = json.load(bookmark)

    # gets the bookmarks in HTML format with proper indentation
    bookmark_bar = extract_bookmarks(data["roots"]["bookmark_bar"]["children"])
    other_bookmarks = extract_bookmarks(data["roots"]["other"]["children"])

    all_bookmarks = bookmark_bar + other_bookmarks

    # exports the HTML file
    exporting_to_HTML(all_bookmarks)


# extracts all the bookmarks recursively from the JSON file
# if there is no indent_level as argument, use 0 as default value
def extract_bookmarks(json_data, indent_level=0):
    html_content = ""
    indent = "  " * indent_level

    for item in json_data:
        # if the type is url, then add it to the html_content
        if item["type"] == "url":
            html_content += f'{indent}<DT><A HREF="{item["url"]}">{item["name"]}</A>\n'
        elif item["type"] == "folder":
            folder_name = item["name"]

            # Start of a folder
            html_content += f'{indent}<DT><H3>{folder_name}</H3>\n'
            html_content += f'{indent}<DL><p>\n'
            
            # Recursively process the children of the folder
            html_content += extract_bookmarks(item['children'], indent_level + 1)
            
            # End of the folder
            html_content += f'{indent}</DL><p>\n'

    # returns html contents ready to wirte
    return html_content


# exports a HTML file using the all extracted bookmarks
def exporting_to_HTML(bookmarks):
    # the initials of the file
    html_headers = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<HTML>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
"""

    html_footer = "</DL><p></HTML>"

    full_html = html_headers + bookmarks + html_footer

    filename = "Brave_bookmark_backup.HTML"
    # force opens a html file
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(full_html)


if __name__ == "__main__":
    main()