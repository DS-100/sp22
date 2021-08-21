## Generating Staff Markdown files

Note: I followed this tutorial https://www.makeuseof.com/tag/read-write-google-sheets-python/.

### Google Cloud Setup

1. Go to [Google Cloud Platform API Dashboard](https://console.cloud.google.com/apis/dashboard). Make sure to be logged into your berkeley.edu account.
2. If available, select `Create New Project`, otherwise open the dropdown menu next to the `Google Cloud Platform` header and select `New Project`.
3. Title your project, verify that the organization is berkeley.edu, and set the location to berkeley.edu/Learning. Then select the `Create` button.
4. You should be brought to the `APIs & Services Dashboard`. If you are not, access it [here](https://console.cloud.google.com/apis/dashboard). Verify that there are graphs shown on this screen (the graphs may be blank or have a 'No data available' message, which is fine).
5. Select `Enable APIs and Services` at the top of the screen or go [here](https://console.cloud.google.com/apis/library).
6. In the `Search for APIs and Services` searchbar, type "sheets" and search.
7. Select the `Google Sheets API`. Then select `Enable`.
8. Select `Create Credentials`, then in the left menu, select `Credentials`.
9. At the top of the page, click `Create Credentials`, and select `Service Account` from the dropdown menu.
10. Fill in the name and select `Create` and then `Done`.
11. Find the name in the `Service Accounts` table and select the edit button.
12. Select `Keys`, choose `Add Key`, and click `Create new key`.
13. Choose `JSON` format, and select `Create`. The `.json` file will download.
14. Move it into the `_staffers` directory, and rename it `sheets_parser.json`.
15. Open the `.json` file and copy the `client_email` field.
16. Share the google sheet with this email.

**Note:** Do NOT add `sheets_parser.json` to GitHub. This file contains a private key, which should be kept private for maximum security. I recommend using `git stash push -m "sheets_parser.json should only be local" sheets_parser.json` to stash the file.

### Python Setup

**Note:** Prior to running the script, download all the staff photos, and make sure they are titled First_Last.[extension]. Staff photos will not be visible on the server unless they are already on GitHub.

1. Run the following lines in your terminal.

```
pip install oauth2client
pip install PyOpenSSL
pip install gspread
```

2. In line 56 of `sheets_parser.py`, change the second value in `range()` to the last line number in the Sheets file that contains a staff member.
3. Verify that the columns (used to index into `row` in `attribute_parser`) are correct. If they are not, update them and/or add other desired fields.
4. Run `python sheets_parser.py` in the terminal.
5. Open the `_staffers` directory. You should see all the files have been generated.

### Parsing the Sheet
See this doc for how the sheet was organized in Fall 2021 https://docs.google.com/document/d/1jftTGzRyYFKT8HwVXV-mNF5-ySI04ji8WiqFM5AYtNA/edit?usp=sharing.
