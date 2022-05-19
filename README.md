![Bandersnatch Logo](https://github.com/sherryrich/bandersnatch/blob/main/docs/black_mirror_bandersnatch.PNG)

## README Table of contents
* [Introduction](#bandersnatch)
* [User Experience](#user-experience)
* [Logic](#logic)
* [Design](#design)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

# Bandersnatch

Inspiration for this project came from Netflix's popular series Black Mirror. A particular episode entitled [Bandersnatch](https://www.imdb.com/title/tt9495224/) where the user gets to choose different scenarios and possible paths which determine the outcome of the story.

A deployed link to the website can be found [here](https://sherryrich.github.io/bandersnatch/)

## Showcase
![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_amiresponsive.PNG)


## User Experience
### User Stories

#### As the site creator:
* Create a simple website incorporating the app to allow users interact with the game.
* Build a simple and challenging game for users to complete.

#### As a first time user:
* Immediately be informed of the main purpose of the game and how to play.
* Try to remember the path chosen and not to take the wrong path the next time.

#### As a returning user:
* Choose alternative paths to see different outcomes.
* Try to complete the game by guessing the password.

## Logic
* A flowchart was created to visualise the logical flow and various paths possible.

![Flowchart](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch.drawio.png)

## Design
* Favicon logo represents branch point or multiple choice. This logo also features in the episode of Bandersnatch.

![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_logo.png)


### Colour
* Colours sourced via Python Colorama, used Green, Yellow, Red & Cyan accordingly to various paths chosen and result. Example Green was chosen when user wins and Red was chosen when user ends game. The main landing page "Bandersnatch" is displayed in Yellow and "Welcome to Bandersnatch" in Red. See various screen shots below.


### Features

Users are greeted and asked for their name which is then used later in the game.

![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_welcome.PNG)

When users choose the incorrect path they are displayed why it was the wrong path and shown game over message.

![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_game_over.PNG)


They are then given with the option of starting again which loops back to the start.

![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_play_again.PNG)

Offer on the table - multiple paths to choose from.

![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_paths.PNG)

Offer 2 path - a deal is done if you choose <= 20 weeks only. Otherwise user is advised wrong choice and game ends.

![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_offer_2_path.PNG)

* Offer 3 path - user wins and is shown a bonus guess the password game.
* Random word is chosen as the password to guess.
* "_" blank spaces displayed as per the random word.
* User asked to choose a letter.
* If the letter is contained withing the random word then it replaces the blank space.
* If the letter is not within the random word the user looses a life.
* If the user has 5 failed attempts the game is over and asked would they like to play again.

![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_offer_3_path.PNG)

User is given 5 attempts to guess the password.

![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_5_lives.PNG)

If the user correctly guess the random word they completed the game Bandersnatch.

![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_win_game.PNG)


### Future Features:
* I had set up linking externally to Google Sheet API and the functionality was to retrieve the password from the Google Sheet rather than the password.py file. I reverted back as felt this was adding unnecessary complexity to the project as the current password.py file worked as expected.
* Add a leaderboard and Log users details to the Google Sheet.



## Technologies Used
### Languages Used 

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Python](https://www.python.org/)

### Python Packages
* [Colorama](https://pypi.org/project/colorama/) Text in terminal are shown in different colours.
* [Random](https://docs.python.org/3/library/random.html) returns a random integer to get a random word.
* [Time](https://pypi.org/project/time/) used for typewrite effect delay.

### Tools
* [Heroku](https://id.heroku.com) was used to deploy the live project.
* [Patorjk](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) was used to generate Ascii Art.
* [PEP8](http://pep8online.com/) online was used to validate Python code.
* [diagrams.net](https://app.diagrams.net/) was used to create the Flowchart.
* [Balsamiq](https://balsamiq.com/) was used to create the Wireframes.
* [amiresponsive](http://ami.responsivedesign.is/) to see how responsive the site is on different devices.
* [Favicon](https://www.favicon.cc/) Used to created bookmark URL icon.
* [Unicode](https://www.fileformat.info/info/unicode/char/1f47e/index.htm) Used for Alien Monster Unicode in python.
* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
* [Gitpod](https://www.gitpod.io/) An online IDE linked to the GitHub repository used to write my code.


## Testing

Extensive testing was completed to review each possible path / scenario a user might take. This was to ensure looping back to the start and no dead ends were encountered.
Input validation were also completed to test possible errors.
Validating code via PEP8 Linter.


### PEP 8 Online
[PEP8](http://pep8online.com/) was used to validate Python code to ensure no errors were shown upon submission.

#### PEP8 Validator result
![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/pep8online_validator_result.PNG)

<details>
<summary>Password file result</summary>

![Password File result](https://github.com/sherryrich/bandersnatch/blob/main/docs/pep8online_validator_result_password.PNG)
</details>

<details>
<summary>Art file result</summary>

![Password File result](https://github.com/sherryrich/bandersnatch/blob/main/docs/pep8online_validator_result_art.PNG)
</details>


#### Lighthouse Report
![Preview](https://github.com/sherryrich/bandersnatch/blob/main/docs/bandersnatch_lightouse_report.PNG)


## Bugs
* [PEP8 test for membership should be 'not in'](https://stackoverflow.com/questions/24671925/pep8-e713-test-for-membership-should-be-not-in) - Updated code to pass validator.
* [PEP8 expected 2 blank lines found 1](https://stackoverflow.com/questions/40275866/pycharm-shows-pep8-expected-2-blank-lines-found-1) - Updated code to pass validator.
* [No newline at end of file](https://stackoverflow.com/questions/5813311/whats-the-significance-of-the-no-newline-at-end-of-file-log) - Updated code to pass validator.
* [Indentation is not a multiple of four](https://peps.python.org/pep-0008/#indentation) - Updated code to pass validator.
* [ModuleNotFoundError: No module named 'colorama'](https://pypi.org/project/colorama/) - Needed to install Colorama to run in terminal when testing locally.
* Line too long - example "line too long (104 > 79 characters)". I refactored the code for each line to pass the PEP8 online Validator.
* Trailing whitespace -  I removed all whitespace to pass the PEP8 online Validator.
* ASCII Art - The Game Over displayed incorrectly as there was a "\" located at the end of the line. I simply changed it to "\." to solve this issue.
* ASCII Art was failing to pass the PEP8 online validator. I solved this by seeing an option to replace white space in text output with your character of choice. I chose "." and this fixed the issue.

## Unfix Bugs
* Unicode Character displaying 50% on in Firefox.
* Looping issue after game ends to re-start, occasionally stalls.
* User selecting keys while typewrite effect is running.

## Deployment
* The current deployment of this project was done using Gitpod.
* I used the gitpod interface to write the code and as it is linked with Github as it was easy to use the terminal to commit my files and push to my repository.
* The deployed website is hosted on Github pages for easy viewing without having to clone or fork the repository to view the running website. Deployment was done by clicking on the settings tab on my repository then navigating to "Github pages" Changing the source from none to master.
* I deployed the site to GitHub pages. 
* A deployed link to the website can be found [here](https://sherryrich.github.io/bandersnatch/)
* In the GitHub repository go to the Settings tab.
* Next from the source section drop-down select Master Branch.
* Once master branch is selected the page provides the link to the completed website. This can take a minute to activate and show live.

## Deployment to Heroku
* Create a new app in Heroku.
* Select "New" and "Create new app".
* Name the new app and click "Create new app".
* Click on the "Settings" tab at the top of the page.
* Open the "Reveal Config Vars" section and input the following information - KEY: PORT, VALUE: 8000.
Nothing else is needed here for this project
* Under the Config Vars section in "Settings" select "BuildPack" and select Python and Nodejs,
Make sure they are in this order.
* In "Deployment Method" click on "GitHub" to connect them.
* Select "connect".
* Enable Automatic Deploys" or "Deploy Branch".
* Heroku will now deploy the site.
* NOTE: Heroku deployment procedure changed from the Heroku dashboard so subsequent depoloments were deployments via the terminal only. [See here for steps.](https://github.com/sherryrich/bandersnatch/blob/main/docs/heroku_deployment.PNG)

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/sherryrich/bandersnatch
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/sherryrich/bandersnatch
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

For a more detailed explanations of the above process [Click Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)



## Credits

* [Code Institute](https://codeinstitute.net/ie/) - Full Stack Developer Course.
* [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/) - AJGreaves Code along for love sandwiches.
* [W3Schools](https://www.w3schools.com/) - Help and inspiration.
* [MDN](https://developer.mozilla.org/en-US/) - Constant source of information.
* [Udemy](https://www.udemy.com/course/100-days-of-code/) - 100 Days of Code: The Complete Python Pro Bootcamp for 2022.
* [Udemy](https://www.udemy.com/course/100-days-of-code/learn/lecture/19140848#overview) - Hangman - 100 Days of Code: The Complete Python Pro Bootcamp for 2022.
* [Udemy](https://www.udemy.com/course/the-modern-python3-bootcamp/) - The Modern Python 3 Bootcamp
* [YouTube](https://www.youtube.com/watch?v=A_1THfBpCH8) - Typewriter effect in python
* [YouTube](https://www.youtube.com/watch?v=u4QmAIoo4i0&t=81s) - Colours in Python

## Acknowledgements
* To create this website, I relied on material covered in the Full Stack Development course by Code Institute. I also relied on information from Code Institute, Slack Community Channels, Udemy, W3Schools, MDN and YouTube for Online Web Tutorials and resources.
* Martina Terlevic my tutor for reviewing my work and providing excellent feedback, advice, tips and additional resources.

## Note 
This project is for educational use only and was created for the Code Institute Module.

Created by Richard Sherry :sunglasses:

[Back to top](#bandersnatch)