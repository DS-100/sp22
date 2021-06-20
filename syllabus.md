---
layout: page
title: Syllabus
nav_order: 2
description: >-
    Principles and Techniques of Data Science
---

# Syllabus

Jump to:

- [About Data 100](#about)
- [Online Format](#format)
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

While we are working to make this class widely accessible, we currently require the following (or equivalent) prerequisites. **We are not enforcing prerequisites during enrollment. However, all of the prerequisties will be used starting very early on in the class. It is your responsibility to know the material in the prerequisites.**

- **Foundations of Data Science**: [Data8](http://data8.org) covers much of the material in Data 100 but at an introductory level. Data8 provides basic exposure to python programming and working with tabular data as well as visualization, statistics, and machine learning.
- **Computing**: _The Structure and Interpretation of Computer Programs_ ([CS 61A](http://cs61a.org)) or _Computational Structures in Data Science_ ([CS 88](https://cs88-website.github.io)). These courses provide additional background in python programming (e.g., for loops, lambdas, debugging, and complexity) that will enable Data 100 to focus more on the concepts in Data Science and less on the details of programming in python.
- **Math**: _Linear Algebra_ (Math 54, [EE 16a](http://ee16a.org), or Stat89a): We will need some basic concepts like linear operators, eigenvectors, derivatives, and integrals to enable statistical inference and derive new prediction algorithms. This may be satisfied concurrently to Data 100.

<br>

<a name = 'format'></a>

## Online Format

This summer, Data 100 will be run entirely online. This section details exactly how each component of the course will operate. But here's a nice high-level "typical week in the course":

|  Mo | Tu | We | Th | Fr |
| --- | --- | --- | --- | --- |
| Office Hours | Office Hours | Office Hours | Office Hours | Office Hours |
| <span style="color:Green">Lecture released</span> | <span style="color:Green">Lecture released</span> | <span style="color:Green">Lecture released</span> | <span style="color:Green">Lecture released</span> | <span style="color:Orange">Live Lecture</span> |
| <span style="color:Red">Homework A released</span> | | | <span style="color:Red">Homework B released</span> | |
| <span style="color:Red">**Homework B due**</span> | | | <span style="color:Red">**Homework A due**</span> | |
| <span style="color:Purple">[SUNDAY] Labs A, B released</span> | | | | <span style="color:Purple">[SATURDAY] **Labs A, B due**</span> |
| <span style="color:Blue">Discussion Section</span> | | <span style="color:Blue">Discussion Section</span> | | |

Note that these deadlines are subject to change.

- To see when any live events are scheduled, check the [Calendar](../calendar).
- To see when lectures, discussions, and assignments are released (and due), check the [Home Page](../).

<br>

### Discussions

This course has discussion sections on Mondays and Wednesdays, lasting for one hour each. There will also be some sections on Tuesdays and Thursdays. The goal of these sessions is to work through problems, hone your skills, and flesh out your understanding as part of a team. The problems that you solve and present as part of discussion are important in understanding this material.

To encourage attendance and participation in live discussion, we will offer the option of having discussion contribute to your grade. Specifically, points you earn from attending/participating in discussion can reduce the weighting of exams on your overall course grade. See the grading breakdown below for details.

<br>

### Lecture

- There are 4 lectures per week.
- **Lectures will be entirely pre-recorded**, in a format that is optimized for online learning (short 5-10 minute videos with optional conceptual problems in between). Lecture videos will be released on the mornings of Monday, Tuesday, Wednesday and Thursday at 9:40 AM PT.
  - Many of these will be from previous semesters, but some will be recorded this summer by the instructors.
  - Lecture videos will be posted on YouTube. Each “lecture” will be an html page linked on the course website, containing videos and links to slides and code.
  <!-- - There are "Quick Check" conceptual questions in between each lecture video, linked on the lecture webpage. See below for more details. -->
  - Each lecture will also have a Piazza thread for students to ask questions.

<!-- Note: Alongside each lecture are textbook readings. Textbook readings are purely supplementary, and may contain material that is not in scope (and may also not be comprehensive). -->

<br>

<!-- ### Quick Checks

Quick Checks, as mentioned above, are short conceptual questions embedded into each lecture, in the form of Google Forms. These are meant for you to check your understanding of the concepts that were just introduced. Since there are roughly 26 lectures, there are roughly 26 Quick Checks, each of which consists of 4-7 Google Forms.

**Quick Checks are graded on completion.** That is, your score on them does not matter, you just need to do them. For each lecture, you will be required to submit a code to Gradescope that you will receive after completing one of the Google Forms for that lecture. These are due the Monday after the lecture is released. (Though we will assign grades using Gradescope, we will also collect emails on the Google Forms themselves.)

<br> -->

### Homeworks

Homeworks are assignments that are designed to help students develop an in-depth understanding of both the theoretical and practical aspects of ideas presented in lecture.

- In a typical week, there will be two homeworks. The first will be released Monday morning, by 9:40 AM PT, and will be due Thursday at 11:59 PM PT. The second homework will be released Thursday morning at 9:40 AM PT, and will be due the following Monday at 11:59 PM PT. There may be some deviation in this schedule to account for holidays, exams, etc.
<!-- - Near the midterm, or during weeks in which a project is assigned, you will have more than one week to work on the current assignment. -->
- Most homeworks will be Jupyter notebooks; one or two homeworks will be on-paper written assignments.
- Homeworks have both visible and hidden autograder tests. The visible tests are mainly sanity checks, e.g. a probability is <= 1, and are visible to students while they do the assignment. The hidden tests generally check for correctness, and are invisible to students while they are doing the assignment.
- The primary form of support students will have for homeworks and projects are the **office hours** we’ll host, and **Piazza**.
- Homeworks must be completed individually.

<br>

### Labs

Labs are shorter programming assignments designed to give students familiarity with new ideas.

- In a typical week, there will be two labs, often covering content taught in lecture the same week. Both labs will be released simultaneously on Sunday morning by 9:40 AM PT, and they will both be due on Saturday at 11:59 PM PT.
- All lab autograder tests are visible.
<!-- - To help with lab, we will host **live lab sections** on Monday at various times, in which GSIs will walk through the assignment via Zoom. See the [Calendar](../calendar) for when these are scheduled. -->
- In previous semesters, we held live lab sections; this semester, we will _not_ be holding live sections for labs. Instead, the labs have been condensed and simplified, and will include a video walk-through to assist students in completing the assignment.
- Students can get help with labs at **office hours** and on **Piazza**.

<br>

### Office Hours

- We plan on hosting roughly 10 hours of office hours each weekday. These hours are listed on the [Calendar](../calendar).
- OH will serve as a one-stop shop for students to get help with assignments.
- Office Hours can be accessed via [oh.ds100.org](https://oh.ds100.org), where students add themselves to the "queue" and specify the assignment they need help on. Once it's their turn, they will be provided with a Zoom link to join, in order to get help from staff.
- The instructors will also be hosting conceptual office hours. These will be reflected on the [Calendar](../calendar).
<!-- - We are also holding "lost office hours" once a week. These are designed to accommodate students who are behind on material and would like help catching up. These are meant for conceptual questions only, not for assignment help. These will also be reflected on the [Calendar](../calendar). -->

<br>

### Exams

There will be one midterm exam, on **July 15th** (9:30 AM - 11:00 AM PT), and a final exam on **August 12th** (9:30 AM - 12:30 PM PT).

Alternate exam times will be offered for the midterm and final, and the form to request the alternate will be posted on Piazza soon after the start of class. The alternate midterm is July 15th from 8:00 PM - 9:30 PM PT and the alternate final is August 12th from 8:00 PM - 11:00 PM PT. The primary purpose of the alternate exam is to accommodate students in different timezones, but students with documented conflicts and unique personal circumstances may also be approved to take the alternate exam.

<br>

### Regrade Requests

Students will be allowed to submit regrade requests for the autograded and written portions of assignments in cases in which the rubric was incorrectly applied or the autograder scored their submission incorrectly. Regrades for the written portions of assignments will be handled through Gradescope, and autograder regrades via a Google Form.

**Always check that the autograder executes correctly!** Gradescope will show you the output of the public tests, and you should see the same results as you did on DataHub. If you see a discrepancy, ensure that you have exported the assignment correctly and, if there is still an issue, post on Piazza _as soon as possible_.

Regrade requests will **not** be considered in cases in which:

- a student uploads the incorrect file to the autograder
- the autograder fails to execute and the student does not notify the course staff _before the assignment deadline_
- a student fails to save their notebook before exporting and uploads an old version to the autograder
- a situation arises in which the course staff cannot ensure that the student's work was done before the assignment deadline
- a students submits without following the steps outlined in [@11](https://piazza.com/class/kpcl6edmxuk3fg?cid=11)

<br>

<a name = 'policies'></a>

## Policies

 **Grading Scheme**

| Category | Weight | Details |
| --- | --- | --- |
| Homeworks | 40% | 12, with 2 drops |
| Labs | 10% | 13, with 2 drops |

The remaining 50% of your grade will be the maximum of two scores. You do not need to explicitly select one or the other—we will automatically determine the maximum for you.

| Category | Weight | Details |
| --- | --- | --- |
| Discussion Score | 10% | 13, with 2 drops |
| Midterm Exam | 16% | |
| Final Exam | 24% | |

| Category | Weight | Details |
| --- | --- | --- |
| Discussion Score | 0% | |
| Midterm Exam | 20% | |
| Final Exam | 30% | |

Your discussion score is the average of your scores for each individual discussion. Each discussion will be graded on a 0/1 basis. As of now, that one point will be determined based on attendance—if you attend a discussion section, you will receive the point for that discussion section. However, we reserve the right to increase the threshold to earn this point, for example, by requiring some form of participation. Note that cameras are encouraged, but are **NOT** required in discussion section.

<!-- Note that a ninth homework and second homework drop were announced partway through the semester. -->

<br>

### Late Policy

All assignments are due at 11:59 pm on the due date specified on the syllabus. **Gradescope is where all assignments are submitted.** Extensions are only provided to students with DSP accommodations, or in the case of exceptional circumstances. If these conditions apply, please make a private Piazza post to request an extension. When posting, please put [EXTENSION REQUEST] in the title, and select the “extension” folder. **Homeworks and labs will not be accepted late.** Gradescope may allow you to make late submissions, but you will later be given a 0.

<!-- - Projects are marked down by 10% per day, **up to two days**. After two days, project submissions will not be accepted.
  - Submission times are rounded up to the next day. That is, 2 minutes late = 1 day late. -->

<br>

### Collaboration Policy and Academic Dishonesty

#### Assignments

Data science is a collaborative activity. While you may talk with others about the homework, we ask that you write your solutions individually in your own words. If you do discuss the assignments with others please include their names at the top of your notebook. Keep in mind that content from assignments will likely be covered on both the midterm and final.

If we suspect that you have submitted plagiarized work, we will call you in for a meeting. If we then determine that plagiarism has occurred, we reserve the right to give you a negative full score (-100%) or lower on the assignments in question, along with reporting your offense to the Center of Student Conduct.

Rather than copying someone else's work, ask for help. You are not alone in this course! The entire staff is here to help you succeed. If you invest the time to learn the material and complete the assignments, you won't need to copy any answers. (taken from [61A](https://cs61a.org/articles/about/#academic-honesty))

We also ask that you **do not post your assignment solutions publicly**.

#### Exams

Cheating on exams is a serious offense. We have methods of detecting cheating on exams – so don't do it! Students caught cheating on any exam will fail this course.  We will be following the [EECS departmental policy on Academic Honesty](https://eecs.berkeley.edu/resources/students/academic-dishonesty), so be sure you are familiar with it.

<br>

### We want you to succeed!

If you are feeling overwhelmed, visit our office hours and talk with us. We know college can be stressful – and especially so during the COVID-19 pandemic – and we want to help you succeed.
