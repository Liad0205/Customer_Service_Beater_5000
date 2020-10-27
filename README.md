# Customer Service Beater 5000

# Disclaimer
There are some awesome companies with great customer service/support out there and this script isn't meant for them.
If you're facing an issue with customer support and you're feeling helpless and passed around, this is for you.

# Manual
Hello, Welcome to the Customer Service Beater 5000!
Instructions:
    * Currently only gmail accounts are supported but you can change setupSMTP method to any 
      other host and port number. 
    * Change the textTemplate variable in the updateText() method to suit your needs.
      Note the example textTemplate if you want to incorporate the date and counter to your email
      content, it will be updated with every email sent. 
    * Run the script and answer the prompts.
    * The script will login via SMTP to gmail and will send an emails with the following logic:
        1. Initially - send a mail every 3 hours
        2. If 4 emails have been sent - decrease time interval by 15 minutes until the minimum time of 15 minutes is reached
    * Wait for customer service to give up or until the specified amount of emails is reached.
Hope this helps!
NOTE: Please allow less secure app logins to enable SMTP login: https://www.google.com/settings/security/lesssecureapps

# Suggestions
For any suggestion or fixes feel free to contact me or to propose it directly here. 
