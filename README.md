# Auto-Bookmark_backup_BOT
This script, written in Python, creates a backup of all your browser's bookmarks.

<h3>How does it work?</h3>
The user must add the "BOOKMARK_PATH" to the ".env" file. Browser local bookmarks are usually stored in JSON format. This script parses the bookmarks from JSON to HTML format. Then, the script saves(overwrites if there is already a previous bookmark backup from a previous time) the bookmark. The bookmarks are parsed in HTML format so that the backed-up bookmarks can easily be imported into the browser. This script also maintains the folder order through indent_level.

<h3>How to use?</h3>
0. Download the dotenv library using "pip install dotenv" in PowerShell or CMD. <br> 
1. Download the GitHub repository.<br>
2. Unzip the repository.<br>
3. The BOOKMARK_PATH varies between browsers. Search on Google for your browser's bookmark path. <br>
4. Create a ".env" file in the same directory and open it. <br>
5. Write: BOOKMARK_PATH="". Inside the inverted commas, write the bookmarks path.<br>
6. Open the Task Scheduler.<br>
7. Create a new task for the script. (Trigger can be whatever the user wants. Personally, I like to back up my bookmarks every Friday.)<br>