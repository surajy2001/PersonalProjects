This Selenium script helps automate GCN teacher training Modules using Selenium Chrome Webdriver:

- Script will automate going through the length of questions, by waiting for slide to complete and clicking next 
   - The script must be run independently each time for a specific module you would like completed
- Script will run from an empty desktop with no windows currently open.
- Cookies are accepted on the Webpage
- Script will wait on questions for user input before clicking 'next' 

-----------------------------------------------------  

To properly use my script, there are some changes that you need to make: 
  1) You will need to replace the 'org_ID' with your organization ID
  2) You will need to replace 'user_name' with your username
  3) You will need to change 'choose_assignment' to the XPATH of the current module you want to complete
     - Be sure the module name is visible on the webpage (One may need to scroll to get it into the view of the webpage)
  4) Change the 'for loop' to reflect the range of questions in your module

Optional:
 - Alter 'sleep' at the end of the file to keep the browser open for a longer time (in seconds) 


My mother was struggling to complete her GCN training modules for work as they take hours, so I wanted to step up and help. PLEASE SHARE AND USE THIS TO YOUR ADVANTAGE
