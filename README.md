# Team-27: eVaidya
## Problem statement
Taru Foundation: Telemedication

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Intoduction</a>
      <ul>
        <li><a href="#our-aim">Our Aim</a></li>
        <li><a href="#functionalities">Functionalities </a></li>
      </ul>
    </li>
    <li>
      <a href="#tech-stack-used">Tech Stack Used</a>
<!--       <ul>
        <li><a href="#what-is-agile">What is Agile</a></li>
        <li><a href="#how-i-incorporated-agile-methodology-during-the-development-cycle">How I Incorporated Agile Methodology During The Development Cycle</a></li>
      </ul> -->
    </li>
    <li><a href="#website-screenshots"> Web Site Screenshots </a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
<!--     <li><a href="#navigating-through-the-application">Navigating through the Application</a></li><ul> -->
  </ol>
</details>


## Introduction
## Our Aim
To provide platform to connect RMPs, Patients and Doctors at one stop destination. Our vision is to provide an app for all basic healthcare needs of the rural people. 
It is an accessible, free, instant, user-friendly platfrom. Making it a one stop solution for a health platform.
## Functionalities
The app allows RMPs to schedule an appointment for the patient or the patient can schedule it themselves. The patient can access the video chat feature enabled which they can use to interact with the doctors from the comfort of their homes if internet is available or they can go to their local RMP’s office where they provide this service. It renders a hassle-free environment and saves transportation time and the time spent in waiting queues for patients. Here even the doctors can have a look at thier scheduled appointments and also accept, deny, reschedule the appointments.
## Use Case Diagram

<img src="https://user-images.githubusercontent.com/72303810/175796987-46eb2175-f907-425e-8441-80c8f4c1bab6.png" width="700">

## Tech stack used
<!-- <p><a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> 
  </p> -->
  - *Front End:* HTML, CSS, JS, Bootstrap, jQuery
  - *Back end:* Django, Python
  - *API:* Agora 
  - *Database:* SQLite


## Website screenshots

### Landing page

<img width="700" alt="Screenshot 2022-11-06 at 10 43 07 AM" src="https://user-images.githubusercontent.com/72303810/200155342-a24224d0-a8e1-4b8a-8585-482e80353ac6.png">

### Login page
<img src="https://user-images.githubusercontent.com/72303810/175796630-29dcb6de-28a5-4b34-8c74-ffecb6b4bda8.jpeg" width="700">
<img src="https://user-images.githubusercontent.com/72303810/175796633-4355d576-2df8-4560-b3f5-08d0d2e7242a.jpeg" width="700">
<img src="https://user-images.githubusercontent.com/72303810/175796635-44996cd7-c970-496e-832a-ff9d845e8c49.jpeg" width="700">
<img src="https://user-images.githubusercontent.com/72303810/175796636-c5cde6af-b686-4295-ae81-09a87e3defe7.jpeg" width="700">

### Dashboard
<img src="https://user-images.githubusercontent.com/72303810/175796650-f8cdc8a2-0e8a-45c4-9ed2-a0c570ac1998.jpeg" width="700">
<img src="https://user-images.githubusercontent.com/72303810/175796654-1076b12d-0516-4809-9442-1f30925c7c16.jpeg" width="700">

## Getting started
To install and run the project on your local system, following are the requirements:
 - Clone the GitHub repository
``` sh
$ git clone https://github.com/cfgmum22/team-27.git
```
 - Change directory to team-27
``` sh
$ cd team-27
  ```
- Make sure to install the required dependencies from requirements.txt file
``` sh
 pip install -r requirements.txt 
```
- To install additional dependencies run the following commands
```
pip3 install pipenv
pipenv shell
```

```
pip install django-widget-tweaks
pip install django==3.0.5
pip install xhtml2pdf
```

```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```



