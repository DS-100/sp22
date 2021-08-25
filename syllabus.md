---
layout: page
title: Syllabus
nav_order: 2
description: >-
    Principles and Techniques of Data Science
---

# Syllabus

<!-- ## Note: This page is under construction. Everything on this website is subject to change. -->

Jump to:

- [About Data 100](#about)
- [Hybrid Format](#format)
- [Policies](#policies)

<br>

<a name = 'about'></a>

## About Data 100

Combining data, computation, and inferential thinking, data science is redefining how people and organizations solve challenging problems and understand their world. This intermediate level class bridges between [Data 8](http://data8.org) and upper division computer science and statistics courses as well as methods courses in other fields. In this class, we explore key areas of data science including question formulation, data collection and cleaning, visualization, statistical inference, predictive modeling, and decision making.​ Through a strong emphasis on data centric computing, quantitative critical thinking, and exploratory data analysis, this class covers key principles and techniques of data science. These include languages for transforming, querying and analyzing data; algorithms for machine learning methods including regression, classification and clustering; principles behind creating informative data visualizations; statistical concepts of measurement error and prediction; and techniques for scalable data processing.

<br>

### Goals

- Prepare students for advanced Berkeley courses in data-management, machine learning, and statistics, by providing the necessary foundation and context
- Enable students to start careers as data scientists by providing experience working with real-world data, tools, and techniques
- Empower students to apply computational and inferential thinking to address real-world problems

<br>

### Prerequisites

While we are working to make this class widely accessible, we currently require the following (or equivalent) prerequisites. **Unlike past semesters, prerequisites will be enforced in this class. It is your responsibility to know the material in the prerequisites.**

- **Foundations of Data Science**: [Data 8](http://data8.org) covers much of the material in Data 100 but at an introductory level. Data8 provides basic exposure to python programming and working with tabular data as well as visualization, statistics, and machine learning.
- **Computing**: _The Structure and Interpretation of Computer Programs_ ([CS 61A](http://cs61a.org)) or _Computational Structures in Data Science_ ([CS 88](https://cs88-website.github.io)). These courses provide additional background in python programming (e.g., for loops, lambdas, debugging, and complexity) that will enable Data 100 to focus more on the concepts in Data Science and less on the details of programming in python.
- **Math**: _Linear Algebra_ (Math 54, [EE 16A](http://ee16a.org), or Stat 89A): We will need some basic concepts like linear operators, eigenvectors, derivatives, and integrals to enable statistical inference and derive new prediction algorithms. This may be satisfied concurrently to Data 100.

<br>

<a name = 'format'></a>

## Hybrid Format

This fall, Data 100 will be run in a hybrid format. This section details exactly how each component of the course will operate. But here’s a nice high-level “typical week in the course”:

|  Mo | Tu | We | Th | Fr |
| --- | --- | --- | --- | --- |
| Office Hours | Office Hours | Office Hours | Office Hours | Office Hours |
| | <span style="color:Green">Lecture released</span> | | <span style="color:Green">Lecture released</span> | |
| | <span style="color:Purple">Lab Section</span> | | | <span style="color:Blue">Discussion Section</span> |
| | | | <span style="color:Red">**Homework due**</span> | <span style="color:Red">**Homework released**</span> |
| | <span style="color:Purple">**Lab due**</span> | | | <span style="color:Purple"> **Lab released**</span> |


Note that these deadlines are subject to change.

- To see when any live events are scheduled, check the [Calendar](../calendar).
- To see when lectures, discussions, and assignments are released (and due), check the [Home Page](../).

<br>

**Note: In-person meetings are fully dependent on public health guidelines. We are prepared to hold all course activities online should circumstances demand.**

<br>

### Lecture

- There are 2 lectures per week.
- **Regular lectures will be pre-recorded**, in a format that is optimized for online learning (short 5-10 minute videos with optional conceptual problems in between). Lecture videos will be released on the mornings of Tuesday and Thursday.
  - Many of these will be from previous semesters, but some will be recorded this fall by the instructors.
  - Lecture videos will be posted on YouTube. Each “lecture” will be an html page linked on the course website, containing videos and links to slides and code.
  <!-- - There are "Quick Check" conceptual questions in between each lecture video, linked on the lecture webpage. See below for more details. -->
  - Each lecture will also have a Piazza thread for students to ask questions.

We will have some guest speakers this term, on topics including Human Context and Ethics of Data Science and applications to Climate Change. **These lectures will be held live on Zoom**, and we strongly encourage you to attend them!

<!-- Note: Alongside each lecture are textbook readings. Textbook readings are purely supplementary, and may contain material that is not in scope (and may also not be comprehensive). -->

<br>

### Discussions

This course has discussion sections on Fridays, lasting for one hour. The goal of these sessions is to work through problems, hone your skills, and flesh out your understanding as part of a team. The problems that you solve and present as part of discussion are important in understanding this material.

To encourage attendance and participation in live discussion, we will offer the option of having discussion contribute to your grade. Specifically, points you earn from attending/participating in discussion can reduce the weighting of homeworks on your overall course grade. See the course policies for more details.

- In a typical week, we will release the discussion worksheet on Friday morning.
- We will be holding live discussion sections on Fridays. You will sign up for a section, but attendance will not be required.
  - **Unlike past semesters, live discussions will not provide physical handouts.**
- We will release discussion recordings or walkthroughs the week after the discussion.
  - These will be videos from past semesters, so they may not be up-to-date with the current content. Unfortunately, we do not have the capacity to record walkthroughs this semester.


<br>

<!-- ### Quick Checks

Quick Checks, as mentioned above, are short conceptual questions embedded into each lecture, in the form of Google Forms. These are meant for you to check your understanding of the concepts that were just introduced. Since there are roughly 26 lectures, there are roughly 26 Quick Checks, each of which consists of 4-7 Google Forms.

**Quick Checks are graded on completion.** That is, your score on them does not matter, you just need to do them. For each lecture, you will be required to submit a code to Gradescope that you will receive after completing one of the Google Forms for that lecture. These are due the Monday after the lecture is released. (Though we will assign grades using Gradescope, we will also collect emails on the Google Forms themselves.)

<br> -->

### Homeworks

Homeworks are week-long assignments that are designed to help students develop an in-depth understanding of both the theoretical and practical aspects of ideas presented in lecture.

- In a typical week, the homework is released on Friday and is due the following Thursday at 11:59PM.
<!-- - Near the midterm, or during weeks in which a project is assigned, you will have more than one week to work on the current assignment. -->
- One or two homeworks will be on-paper written assignments; the rest will be Jupyter notebooks.
- Homeworks have both visible and hidden autograder tests. The visible tests are mainly sanity checks, e.g. a probability is <= 1, and are visible to students while they do the assignment. The hidden tests generally check for correctness, and are invisible to students while they are doing the assignment.
- The primary form of support students will have for homeworks and projects are the **office hours** we’ll host, and **Piazza**.
- Homeworks must be completed individually.

<br>

### Labs

Labs are shorter programming assignments designed to give students familiarity with new ideas.

- In a typical week, the lab is released on Friday and is due the following Tuesday at 11:59PM.
- All lab autograder tests are visible.
<!-- - To help with lab, we will host **live lab sections** on Monday at various times, in which GSIs will walk through the assignment via Zoom. See the [Calendar](../calendar) for when these are scheduled. -->
- To help with lab, we will host live lab sections on Tuesday. You will sign up for a section, but attendance will not be required.
- Students can get help with labs in **lab section**, **office hours**, and on **Piazza**. However, the best place to get help is lab section.

<br>

### Office Hours

- The office hours are listed on the [Calendar](../calendar), and will be held both virtually and in-person.
- Students can come to office hours for any questions on course assignments or material.
- In-person office hours will be held in various locations specified in the [Calendar](../calendar). **To adhere to public health guidelines, we ask that students leave the OH room after their questions have been answered**.
- Virtual OH can be accessed via [oh.ds100.org](https://oh.ds100.org/), where students add themselves to the “queue” and specify the assignment they need help on.
<!-- where students add themselves to the "queue" and specify the assignment they need help on. Once it's their turn, they will be provided with a Z at oom link to join, in order to get help from staff. -->
- The instructors will also be hosting office hours. These will be reflected on the [Calendar](../calendar).
<!-- - We are also holding "lost office hours" once a week. These are designed to accommodate students who are behind on material and would like help catching up. These are meant for conceptual questions only, not for assignment help. These will also be reflected on the [Calendar](../calendar). -->

<br>

### Midterm

There will be one midterm exam, on **November 1st** (7-9PM PDT).

The exam will be primarily virtual and zoom proctored, following campus guidelines. We will have the option to be proctored in-person, but you will still be completing the exam online (just being in-person proctored instead of zoom proctored). In-person spots will be given on a case by case basis by only those who necessarily need it (form coming soon).

- Two time options will be offered to cover various timezones. No further alternates will be offered.
- DSP students will be offered on-campus exam taking as per their accommodations.

<br>

### Final Project

In lieu of a final exam, we will have a final project. The details of this project will be released on **TBD**, and it will be due **TBD** (during RRR or finals week).

- 3-person groups, assigned by us around project release time.
- Details being worked on, will offer a few (2-3) dataset options.

<br>

### Regrade Requests

Students will be allowed to submit regrade requests for the autograded and written portions of assignments in cases in which the rubric was incorrectly applied or the autograder scored their submission incorrectly. Regrades for the written portions of assignments will be handled through Gradescope, and autograder regrades via a Google Form.

**Always check that the autograder executes correctly!** Gradescope will show you the output of the public tests, and you should see the same results as you did on DataHub. If you see a discrepancy, ensure that you have exported the assignment correctly and, if there is still an issue, post on Piazza _as soon as possible_.

Regrade requests will **not** be considered in cases in which:

- a student uploads the incorrect file to the autograder
- the autograder fails to execute and the student does not notify the course staff _before the assignment deadline_
- a student fails to save their notebook before exporting and uploads an old version to the autograder
- a situation arises in which the course staff cannot ensure that the student's work was done before the assignment deadline
- a students submits without following the steps outlined in [@13](https://piazza.com/class/kqsiwfz12g0482?cid=13)

<br>

<a name = 'policies'></a>

## Policies

 **Data C100 Grading Scheme**

| Category | Weight | Details |
| --- | --- | --- |
| Homeworks | 35% | 13 + 1 optional, with 2 drops |
| Labs | 10% | 14, with 3 drops |
| Midterm Exam | 25% | |
| Final Exam | 30% | |

 **Data C200 Grading Scheme**

| Category | Weight | Details |
| --- | --- | --- |
| Homeworks | 35% | 13 + 1 optional, with 2 drops |
| Midterm Exam | 25% | |
| Final Exam | 40% | |

**For C100/C200 optional:** You may shift 5% of your HW grade to discussion attendance via [this Google form](https://forms.gle/YfT3KunoRm2U9oA39).

<br>

### Late Policy

All assignments are due at 11:59 pm on the due date specified on the syllabus. **Gradescope is where all assignments are submitted. Homeworks and labs will not be accepted late.** Gradescope may allow you to make late submissions, but you will later be given a 0.

Extensions are only provided to students with DSP accommodations, or in the case of exceptional circumstances. If you have DSP accommodations, you should expect to receive an email from us. Otherwise, email [snhing@berkeley.edu](mailto:snhing@berkeley.edu to request an extension. If you make a request close to the deadline, we can not guarantee that you will receive a response before the deadline. Additionally, simply submitting a request does not guarantee you will receive an extension. Even if your work is incomplete, please submit before the deadline so you can receive credit for the work you did complete.

Note that extension requests will not be granted in cases where a student’s local (DataHub) tests are not passing. It is the student’s responsibility to solve such problems in advance of the deadline.

- Projects are marked down by 10% per day, **up to two days**. After two days, project submissions will not be accepted.
  - Submission times are rounded up to the next day. That is, 2 minutes late = 1 day late.

<br>

### Collaboration Policy and Academic Dishonesty

We will be following the [EECS departmental policy on Academic Honesty](https://eecs.berkeley.edu/resources/students/academic-dishonesty), which states that using work or resources that are not your own or not permitted by the course may lead to disciplinary actions, up to and including a failing grade in the course.

#### Assignments

Data science is a collaborative activity. While you may talk with others about the homework, we ask that you write your solutions individually in your own words. If you do discuss the assignments with others please include their names at the top of your notebook. Keep in mind that content from assignments will likely be covered on both the midterm and final.

If we suspect that you have submitted plagiarized work, we will call you in for a meeting. If we then determine that plagiarism has occurred, we reserve the right to give you a negative full score (-100%) or lower on the assignments in question, along with reporting your offense to the Center of Student Conduct.

Rather than copying someone else's work, ask for help. You are not alone in this course! The entire staff is here to help you succeed. If you invest the time to learn the material and complete the assignments, you won't need to copy any answers. (taken from [61A](https://cs61a.org/articles/about/#academic-honesty))

We also ask that you **do not post your assignment solutions publicly**.

#### Exams

Cheating on exams is a serious offense. We have methods of detecting cheating on exams – so don't do it! Students caught cheating on any exam will fail this course.

<br>

### We want you to succeed!

If you are feeling overwhelmed, visit our office hours and talk with us. We know college can be stressful – and especially so during the COVID-19 pandemic – and we want to help you succeed.
