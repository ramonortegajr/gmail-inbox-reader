# Gmail Inbox Reader
This python script is to mark as read all the unread inboxes in your gmail account and loop reading the until the code detect that all messages is read it will stop

# How to use
1. Before running this script, make sure to set up a project in the Google Developers Console, enable the Gmail API, and download the credentials.json file containing your client ID and client secret. Also, ensure that the token.json file is present in the same directory as the script, or run the script once to generate it through the authentication flow.
2. To obtain the token.json file needed for authentication with the Gmail API, you'll need to run the Python script provided. When you run the script for the first time, it will initiate the OAuth flow and prompt you to authorize access to your Gmail account. Once you grant permission, the script will generate the token.json file containing the necessary access and refresh tokens.
   Steps:
   2.1 Run the Python script provided.
   2.2 The script will open a browser window or provide a URL in the console where you can authorize access to your Gmail account.
   2.3 Follow the on-screen instructions to log in to your Google account and grant permission to the application.
   2.4 After authorization, the script will generate the token.json file in the same directory as the script.
   2.5 Subsequent runs of the script will use this token.json file for authentication without requiring you to go through the authorization process again.
3. You need to install the required module for Python
   3.1 pip install google-auth
   3.2 pip install google-auth-oauthlib
   3.3 pip install google-api-python-client
4. Set-up the Google Console to have a credentials in OAUTH
   4.1 Go to the Google Cloud Console: Navigate to the Google Cloud Console.
   4.2 Create a New Project (if necessary): If you haven't already created a project for your application, click on the project drop-down menu at the top of the page and select "New Project." Follow the prompts to create a new project and give it a name.
   4.3 Select Your Project: Once your project is created (or if you already have one), select it from the project drop-down menu.
   4.4 Navigate to the API & Services Dashboard: From the left-hand menu, go to "APIs & Services" > "Dashboard."
   4.5 Enable APIs: If your project requires access to specific Google APIs (such as Google Drive API, Gmail API, etc.), you need to enable those APIs. Click on "Enable APIs and Services" and search for the API you need. Then, click on the API and enable it for your project.
   4.6 Create OAuth Consent Screen: Go to "APIs & Services" > "OAuth consent screen." Configure your OAuth consent screen by providing the necessary information such as the application name, user support email, developer contact information, etc. Save the setting
   4.7 Create OAuth Client ID: After configuring the OAuth consent screen, go to "APIs & Services" > "Credentials." Click on "Create Credentials" and select "OAuth client ID."
   4.8 Choose Application Type: Choose the appropriate application type based on your use case (Web application, Android, iOS, etc.).
   4.9 Configure OAuth Consent Screen: If prompted, select the consent screen you configured earlier.
   4.10 Enter Authorized Redirect URIs: For web applications, you'll need to specify authorized redirect URIs. This is the URL where users will be redirected after they authorize your application. Make sure to enter all the URIs that your application will us
   4.11 Obtain Client ID and Client Secret: Once you've configured the OAuth client ID, Google will provide you with a client ID and client secret. These are the credentials you'll use in your application to authenticate with Google APIs.
   4.12 Use the Credentials in Your Application: Integrate the client ID and client secret into your application's code. When users authenticate with your application, use these credentials to obtain an access token for accessing Google APIs on behalf of the user.
5.Run the python script and enjoy watching the messages read one by one !!!!!!
