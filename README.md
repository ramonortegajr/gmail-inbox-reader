# Gmail Inbox Reader
This Python script marks all unread messages in your Gmail inbox as read. It continues to read messages until all are marked as read, at which point it stops.

# How to Use
# 1. Set Up Google Developers Console and Enable Gmail API
- Before running the script, set up a project in the Google Developers Console.<br>
- Enable the Gmail API and download the credentials.json file containing your client ID and client secret.<br>
- Ensure the token.json file is present in the same directory as the script or run the script once to generate it through the authentication flow.<br>
# 2. Obtain Token for Authentication
- Run the provided Python script to obtain the token.json file needed for authentication with the Gmail API.<br>
- The script initiates the OAuth flow, prompting you to authorize access to your Gmail account.<br>
- Follow the on-screen instructions to grant permission to the application.<br>
- After authorization, the script generates the token.json file in the script's directory.<br>
- Subsequent runs of the script will use this token for authentication without requiring re-authorization.<br>
# 3. Install Required Python Modules
Install the necessary modules for Python using pip:<br>
- pip install google-auth<br>
- pip install google-auth-oauthlib<br>
- pip install google-api-python-client<br>
# 4. Set Up Google Console Credentials
- Go to the Google Cloud Console and navigate to your project.<br>
- Enable necessary APIs like Gmail API.<br>
- Configure OAuth consent screen and create OAuth client ID.<br>
- Choose the appropriate application type and configure OAuth consent screen.<br>
- Specify authorized redirect URIs and obtain client ID and client secret.<br>
- Integrate these credentials into your application's code for authentication with Google APIs.<br>
# 5. Run the Script
- Once set up, run the Python script and enjoy watching as the messages are marked as read one by one.
# Note
Ensure you have appropriate permissions and follow security best practices when dealing with authentication credentials.<br>
For any issues or questions, feel free to open an issue or reach out to the developer.<br>
# Happy Email Reading! 📧✨
