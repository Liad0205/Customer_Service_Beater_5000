# Customer Service Beater 5000

# Disclaimer
There are some awesome companies with great customer service/support out there and this script isn't meant for them.
If you're facing an issue with customer support and you're feeling helpless and passed around, this is for you.

# Manual
Hello, Welcome to the Customer Service Beater 5000! <br>
Instructions:<br>
* Currently only gmail accounts are supported but you can change setupSMTP method to any <br>
  other host and port number. <br>
* Change the textTemplate variable in the updateText() method to suit your needs.<br>
  Note the example textTemplate if you want to incorporate the date and counter to your email<br>
  content, it will be updated with every email sent. <br>
* Run the script and answer the prompts.<br>
* The script will login via SMTP to gmail and will send an emails with the following logic:<br>
     1. Initially - send a mail every 3 hours<br>
     2. If 4 emails have been sent - decrease time interval by 15 minutes until the minimum time of 15 minutes is reached<br>
* Wait for customer service to give up or until the specified amount of emails is reached.<br>

Hope this helps!<br>


NOTE: Please allow less secure app logins to enable SMTP login: https://www.google.com/settings/security/lesssecureapps <br>

# Suggestions
For any suggestion or fixes feel free to contact me or to propose it directly here. 
