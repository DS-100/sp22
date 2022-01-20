---
layout: page
title: Syllabus
nav_order: 2
description: >-
    Principles and Techniques of Data Science
markdown: kramdown
course:
    edstem: https://edstem.org/us/courses/15436/
    faq: https://ds100.org/sp22faq
    bcourses: ""
    head_ta: Andrew Lenz
    head_email: andrew.lenz@berkeley.edu
    comms_ta: Samantha
    comms_email: snhing@berkeley.edu
    email: data100.instructors@berkeley.edu
---

# Syllabus
{:.no_toc}

Jump to:
* TOC
{:toc}

<br>

<a name = 'about'></a>

## About Data 100

Combining data, computation, and inferential thinking, data science is redefining how people and organizations solve challenging problems and understand their world. This intermediate level class bridges between [Data 8](http://data8.org) and upper division computer science and statistics courses as well as methods courses in other fields. In this class, we explore key areas of data science including question formulation, data collection and cleaning, visualization, statistical inference, predictive modeling, and decision making.​ Through a strong emphasis on data centric computing, quantitative critical thinking, and exploratory data analysis, this class covers key principles and techniques of data science. These include languages for transforming, querying and analyzing data; algorithms for machine learning methods including regression, classification and clustering; principles behind creating informative data visualizations; statistical concepts of measurement error and prediction; and techniques for scalable data processing.

### Goals
{:.no_toc}

- Prepare students for advanced Berkeley courses in data-management, machine learning, and statistics, by providing the necessary foundation and context.
- Enable students to start careers as data scientists by providing experience working with real-world data, tools, and techniques.
- Empower students to apply computational and inferential thinking to address real-world problems.

<a name = 'prerequisites'></a>
### Prerequisites

While we are working to make this class widely accessible, we currently require the following (or equivalent) prerequisites. **Unlike past semesters, prerequisites will be enforced in this class. It is your responsibility to know the material in the prerequisites.** The instructors do not have the authority to waive these requirements. You should contact CDSS at <a href="https://data.berkeley.edu/academics/data-science-undergraduate-studies/courses/spring-2022-classes">https://data.berkeley.edu/academics/data-science-undergraduate-studies/courses/spring-2022-classes</a> to request an exception.

- **Foundations of Data Science**: [Data 8](http://data8.org) covers much of the material in Data 100 but at an introductory level. Data8 provides basic exposure to python programming and working with tabular data as well as visualization, statistics, and machine learning.
- **Computing**: _The Structure and Interpretation of Computer Programs_ ([CS 61A](http://cs61a.org)) or _Computational Structures in Data Science_ ([CS 88](https://cs88-website.github.io)). These courses provide additional background in python programming (e.g., for loops, lambdas, debugging, and complexity) that will enable Data 100 to focus more on the concepts in Data Science and less on the details of programming in python.
- **Math**: _Linear Algebra_ (Math 54, [EE 16A](https://eecs16a.org/), or Stat 89A): We will need some basic concepts like linear operators, eigenvectors, derivatives, and integrals to enable statistical inference and derive new prediction algorithms. <b>This may be satisfied concurrently to Data 100.</b>

<br>

## Course Culture

Students taking Data C100/C200 come from a wide range of backgrounds. We hope to foster an inclusive and safe learning environment based on curiosity rather than competition. All members of the course community—the instructor, students, and GSIs—are expected to treat each other with courtesy and respect. Some of the responsibility for that lies with the staff, but a lot of it ultimately rests with you, the students.

### Be Aware of Your Actions

Sometimes, the little things add up to creating an unwelcoming culture to some students. For example, you and a friend may think you are sharing in a private joke about other races, majors, genders, abilities, cultures, etc. but this can have adverse effects on classmates who overhear it. There is a great deal of research on something called “stereotype threat,” which finds simply reminding someone that they belong to a particular culture or share a particular identity (on whatever dimension) can interfere with their course performance.

Stereotype threat works both ways: you can assume that a student will struggle based on who they appear to be, or you can assume that a student is doing great based on who they appear to be. Both are potentially harmful.

Bear in mind that diversity has many facets, some of which are not visible. Your classmates may have medical conditions (physical or mental), personal situations (financial, family, etc.), or interests that aren’t common to most students in the course. Another aspect of professionalism is avoiding comments that (likely unintentionally) put down colleagues for situations they cannot control. Bragging in open space that an assignment is easy or “crazy,” for example, can send subtle cues that discourage classmates who are dealing with issues that you can’t see. Please take care, so we can create a class in which all students feel supported and respected.

### Be Respectful

Beyond the slips that many of us make unintentionally are a host of behaviors that the course staff, department, and university do not tolerate. These are generally classified under the term harassment; sexual harassment is a specific form that is governed by federal laws known as Title IX.

UC Berkeley’s <a href="https://ophd.berkeley.edu/">Title IX website</a> provides many resources for understanding the terms, procedures, and policies around harassment. Make sure you are aware enough of these issues to avoid crossing a line in your interactions with other students. For example, repeatedly asking another student out on a date after they have said no can cross this line.

Your reaction to this topic might be to laugh it off, or to make or think snide remarks about “political correctness” or jokes about consent or other things. You might think people just need to grow a thicker skin or learn to take a joke. This isn’t your decision to make. Research shows the consequences (emotional as well as physical) on people who experience harassment. When your behavior forces another student to focus on something other than their education, you have crossed a line. You have no right to take someone else’s education away from them.

### Communicate Issues with Course Staff

Professionalism and respect for diversity are not just matters between students; they also apply to how the course staff treat the students. The staff of this course will treat you in a way that respects our differences. However, despite our best efforts, we might slip up, hopefully inadvertently. If you are concerned about classroom environment issues created by the staff or overall class dynamic, please feel free to talk to us about it. The instructors and the Head TA ({{page.course.head_ta}}) in particular welcome any comments or concerns regarding conduct of the course and the staff.

We are committed to creating a learning environment welcoming of all students that supports a diversity of thoughts, perspectives and experiences and respects your identities and backgrounds (including race, ethnicity, nationality, gender identity, socioeconomic class, sexual orientation, language, religion, ability, and more.) To help accomplish this:

- If your name and/or pronouns differ from those that appear in your official records, please let us know.
- If you feel like your performance in the class is being affected by your experiences outside of class (e.g., family matters, current events), please don’t hesitate to come and talk with us. We want to be resources for you.
- We (like many people) are still in the process of learning about diverse perspectives and identities. If something was said in class (by anyone) that made you feel uncomfortable, please talk to us about it.
<!-- Sometimes, you may not be comfortable bringing this up directly to us. If so, you are welcome to talk to the department’s Faculty Equity Advisor Prof. Fox (fox@berkeley.edu).  -->
- While the course staff understands that improving diversity, equity, and inclusion (DEI) are not enough to overcome systemic issues in academia such as racism, queerphobia, and other forms of discrimination and hatred, we also recognize the importance of DEI work.
  - The Data Science Department has some resources available at [https://data.berkeley.edu/about/diversity-equity-and-inclusion](https://data.berkeley.edu/about/diversity-equity-and-inclusion).
  - There’s also a great set of resources available at [https://eecs.berkeley.edu/resources/students/grievances](https://eecs.berkeley.edu/resources/students/grievances).
- If there are other resources you think we should list here, let us know!

**We take all complaints about unprofessional or discriminatory behavior seriously.**

## Course Components

Below is a high-level “typical week in the course” for Spring 2022.

|  Mo | Tu | We | Th | Fr |
| --- | --- | --- | --- | --- | --- |
| | Office Hours | Office Hours | Office Hours | | 
| | <span style="color:Green">Live Lecture</span> | | <span style="color:Green">Live Lecture</span> | |
| | | | | <span style="color:Blue">Discussion Section</span> | 
| | | | <span style="color:Red">**Homework N due**</span> | <span style="color:Red">**Homework N+1 released**</span> | 
| | <span style="color:Purple">Lab N Help<br/>**Lab N due**</span> | | | <span style="color:Purple"> **Lab N+1 released**</span> | 
| Weekly check due/released | | | | | 

* **All deadlines are subject to change.**
* **Note: In-person meetings are fully dependent on public health guidelines. We are prepared to hold all course activities online should circumstances demand.**
* If you have COVID symptoms, please do not attend in-person activities. Instead, please keep up with the class using the online or asynchronous modes of participation (Zoom, EdStem).
* Office Hours are scheduled on the [Calendar page](../calendar). 
* Lectures, discussions, assignments, projects, and exams are scheduled on the [Home page](../).

<br>

### Lecture
There are 2 live lectures per week. You can attend in-person or via Zoom as permitted by campus policy. All lecture recordings will also be published within 24 hours of the live recording. Each lecture will also have an EdStem thread for students to ask questions.


<!--
We will have some guest speakers this term, on topics including Human Context and Ethics of Data Science and applications to Climate Change. **These lectures will be held live on Zoom**, and we strongly encourage you to attend them!
-->

### Discussion
Live discussion sections are on Fridays, lasting for one hour. The goal of these sessions is to work through problems, hone your skills, and flesh out your understanding as part of a team. The problems that you solve and present as part of discussion are important in understanding this material.

- **You must be assigned to a discussion section, even if you don't intend on regularly attending.**
- To encourage attendance and participation in live discussion, you have the option to have discussion attendance contribute to your overall course grade. See [Policies](#policies) below for more details.
- Discussion sign-ups will be released the first week of class through Signup Genius (link forthcoming). Attendance points will only be given for the section you are assigned to.
- **You can switch sections via the sign-up form through the end of the 3rd week, Friday 2/24/2022.** From the 4th week onwards, your section will be locked in for the rest of the semester.  Due to room restrictions, you may not attend an in-person section that you were not assigned to; there is no such restriction on online sections.
- In a typical week, we will release the discussion worksheet on Friday morning and solutions on Saturday. We are still receiving guidance as to whether we can provide physical handouts during in-person discussions. 
<!--- We will release discussion recordings or walkthroughs the week after the discussion.-->

### Homework and Projects

Homeworks are week-long assignments that are designed to help students develop an in-depth understanding of both the theoretical and practical aspects of ideas presented in lecture.

Projects: Projects are two-week long assignments that synthesize multiple topics.

- In a typical week, the homework (or project) is released on Friday and is due the following Thursday at 11:59PM Pacific. One or two homeworks will be on-paper written assignments; the rest will be Jupyter notebooks. See the [Policies](#policies) section for grading details.
<!-- - Near the midterm, or during weeks in which a project is assigned, you will have more than one week to work on the current assignment. -->
- Homeworks and projects have both visible and hidden autograder tests. The visible tests are mainly sanity checks. For example, a sanity check might verify that the answer you entered is a number as expected, and not a word. The hidden tests generally check for correctness, and are invisible to students while they are doing the assignment.
- The primary form of support students will have for homeworks and projects are the **office hours** we’ll host, and **Ed**.
- Homeworks and projects must be completed individually. See the [Collaboration Policy](#collaboration-policy-and-academic-dishonesty) for more details.

### Lab

Labs are shorter programming assignments designed to give students familiarity with new ideas.

- In a typical week, the lab is released on Friday and is due the following Tuesday at 11:59PM.
- All lab autograder tests are visible.
- In lieu of official lab sections, we will be helping with lab in several ways:
    - Lab walkthroughs, which are recorded videos posted as part of the lab.
    - Lab Help Sections, which are Tuesday office hours that prioritize lab debugging and questions. See the [Calendar](../calendar) and our [Office Hours](#office-hours) for more details.
    - EdStem.
- All labs are intended to take about an hour. You can therefore think of Lab Help Sections as lab sections, where attendance is not required nor expected to complete the lab. The best place to get individual help with lab is Lab Help Sections.

### Office Hours and Communication

The office hours and locations are listed on the [Calendar](../calendar); office hours will be held both virtually and in-person. Instructor office hours are also listed on the calendar. **To adhere to public health guidelines, we ask that students leave the OH room after their questions have been answered**.

In general, students can come to office hours for any questions on course assignments or material. Note that events labeled Lab Help Sections will prioritize lab debugging and questions, after which other questions can be addressed.

Virtual OH can be accessed via [oh.ds100.org](https://oh.ds100.org/), where students add themselves to the “queue” and specify the assignment they need help on.
<!-- where students add themselves to the "queue" and specify the assignment they need help on. Once it's their turn, they will be provided with a Zoom link to join, in order to get help from staff. -->
<!-- - We are also holding "lost office hours" once a week. These are designed to accommodate students who are behind on material and would like help catching up. These are meant for conceptual questions only, not for assignment help. These will also be reflected on the [Calendar](../calendar). -->

**EdStem**, or **Ed** for short, is our course forum this quarter. The course is [here]({{page.course.edstem}}). Please check out EdStem or the [FAQ](page.course.faq) page first before emailing instructors. 

**Staff email**:
You can email [{{page.course.email}}](mailto:{{page.course.email}}) and one of the instructors will get back to you. Note that to ensure more timely responses, this address is monitored by the team of the two lead instructors (Josh Hug and Lisa Yan) the Head TA ({{page.course.head_ta}}), as well as several lead GSIs, to ensure more timely responses. You can contact Josh and Lisa directly for matters that require strict privacy and their direct attention.

### Weekly Checks
While lecture and discussion section attendance is not required, nor even expected, we do expect you to stay up to date with material. To help us keep track of your progress and sentiment about the course, there will be 14 weekly surveys due on Mondays at 11:59 PM Pacific. Weekly check-ins are submitted via Google Form, and links will be provided on the [Home page](../) each week. Weekly Checks are graded on completion, not correctness.

<!--
Quick Checks, as mentioned above, are short conceptual questions embedded into each lecture, in the form of Google Forms. **Quick Checks are not graded.** These are meant for you to check your understanding of the concepts that were just introduced.

Since there are roughly 26 lectures, there are roughly 26 Quick Checks, each of which consists of 4-7 Google Forms.

That is, your score on them does not matter, you just need to do them. For each lecture, you will be required to submit a code to Gradescope that you will receive after completing one of the Google Forms for that lecture. These are due the Monday after the lecture is released. (Though we will assign grades using Gradescope, we will also collect emails on the Google Forms themselves.)
-->

<br>

### Exams

There will be three exams in this course:
* Midterm 1 on **Thursday, February 24** (7-9PM Pacific)
* Midterm 2 on **Thursday, April 7** (7-8:30PM Pacific). Note the shorter exam time period.
* Final exam during our scheduled slot, **Friday, May 13, 7-10pm Pacific**.

- We are still deciding proctoring format, but we will primarily have in-person exams with the option for virtual exams. Alternate exam times will be provided for all exams for pre-approved reasons, such as a concurrent final exam. If you miss an exam due to a personal emergency or illness, please email the Head TA {{page.course.head_ta}} at [{{page.course.head_email}}]({{page.course.head_email}}) immediately.<!--The exam will be primarily virtual and zoom proctored, following campus guidelines. We will have the option to be proctored in-person, but you will still be completing the exam online (just being in-person proctored instead of zoom proctored). In-person spots will be given on a case by case basis by only those who necessarily need it (form coming soon).-->
- In the first few weeks of the semester, we will be releasing forms for exam options on EdStem so that you can let us know of your conflicts (for both midterms and the final).
- DSP students will be offered the option for on-campus exams as per their accommodations.

<!--
Two time options will be offered to cover various timezones. No further alternates will be offered.
-->

### Graduate Final Project
All students enrolled in the graduate version of the course (CS C200 or Stat C200C, i.e. Data 200) will be graded according to the Graduate grading scheme, which includes a graduate final project. More details to follow.

<br/>
<br/>


## Policies

### Grading Scheme

|Category | Data C100 | Data C200 | Details |
| --- | --- | --- |
| Homeworks | 22.5% | 20% | Drop lowest 2 scores |
| Labs      | 10% | 5% <br/>(or 0%, lab opt-out)| Drop lowest 3 scores |
| Projects  | 15% | 10% <br/>(or 15%, lab opt-out)| 
| Midterms  | 25% | 25% | Midterm 1: 15%<br/>Midterm 2: 10% |
| Final     | 25% | 25% | |
| Weekly Check | 2.5% |  - | Drop lowest 4 scores|
| Final Graduate Project | -  | 15% ||

**Optional attendance grading:** For both graduate and undergraduates, you may substitute 5% of your HW grade with discussion attendance throughout the semester. When calculating your overall grade at the end of the semester, we will automatically determine your homework grade as the maximum of your homework grade with and without attendance. Attending 11 of the 14 scheduled discussions is considered full attendance credit (i.e., there are 3 drops).

**Grad lab opt-out**: When calculating your overall grade at the end of the semester, we will automatically take the max of your grade with and without labs. 

<br>


### Late Policy

All assignments are due at 11:59 pm Pacific on the due date specified on the syllabus. 

**Homeworks, labs, and weekly checks will not be accepted late.** 
Google Forms (weekly checks) will promptly close after the deadline.
Gradescope (labs and homeworks) may allow you to make late submissions, but you will later be given a 0. 

**Projects** are marked down by 10% per day, **up to two days**. After two days, project submissions will not be accepted. Submission times are rounded up to the next day. That is, 2 minutes late = 1 day late.

**Extensions** are only provided to students with DSP accommodations, or in the case of exceptional circumstances. If you have DSP accommodations, you should expect to receive an email from us. Otherwise, email our Communications TA {{page.course.comms_ta}} at [{{page.course.comms_email}}]({{page.course.comms_email}}) to request an extension. If you make a request close to the deadline, we can not guarantee that you will receive a response before the deadline. Additionally, simply submitting a request does not guarantee you will receive an extension. Even if your work is incomplete, please submit before the deadline so you can receive credit for the work you did complete.

Note that extension requests will *not* be granted in cases where a student’s local (DataHub) tests are not passing. It is the student’s responsibility to solve such problems in advance of the deadline.

### Regrade Requests

Students will be allowed to submit regrade requests for the autograded and written portions of assignments in cases in which the rubric was incorrectly applied or the autograder scored their submission incorrectly. Regrades for the written portions of assignments will be handled through Gradescope, and autograder regrades via a Google Form.

**Always check that the autograder executes correctly!** Gradescope will show you the output of the public tests, and you should see the same results as you did on DataHub. If you see a discrepancy, ensure that you have exported the assignment correctly and, if there is still an issue, post on EdStem _as soon as possible_.

Regrade requests will **not** be considered in cases in which:

- a student uploads the incorrect file to the autograder.
- the autograder fails to execute and the student does not notify the course staff _before the assignment deadline_.
- a student fails to save their notebook before exporting and uploads an old version to the autograder.
- a situation arises in which the course staff cannot ensure that the student's work was done before the assignment deadline.
<!--- a students submits without following the steps outlined in [@13](https://piazza.com/class/kqsiwfz12g0482?cid=13)-->

### Collaboration Policy and Academic Dishonesty

We will be following the [EECS departmental policy on Academic Honesty](https://eecs.berkeley.edu/resources/students/academic-dishonesty), which states that using work or resources that are not your own or not permitted by the course may lead to disciplinary actions, up to and including a failing grade in the course.

**Assignments.**
Data science is a collaborative activity. While you may talk with others about the homework and projects, we ask that you write your solutions individually in your own words. If you do discuss the assignments with others please include their names at the top of your notebook. Keep in mind that content from assignments will likely be covered on both the midterm and final.

If we suspect that you have submitted plagiarized work, we will call you in for a meeting. If we then determine that plagiarism has occurred, we reserve the right to give you a negative full score (-100%) or lower on the assignments in question, along with reporting your offense to the Center of Student Conduct.

Rather than copying someone else's work, ask for help. You are not alone in this course! The entire staff is here to help you succeed. If you invest the time to learn the material and complete the assignments, you won't need to copy any answers. (taken from [CS61A](https://cs61a.org/articles/about/#academic-honesty))

We also ask that you **do not post your assignment solutions publicly**.

**Exams.**
Cheating on exams is a serious offense. We have methods of detecting cheating on exams – so don't do it! Students caught cheating on any exam will fail this course.

## We want you to succeed!

If you are feeling overwhelmed, visit our office hours and talk with us. We know college can be stressful – and especially so during the COVID-19 pandemic – and we want to help you succeed.

**Important Note**: We are committed to being a resource to you, but it is important to note that all members of the teaching staff for this course are [responsible employees](https://svsh.berkeley.edu/responsible-employee), meaning that **we must disclose any incidents of sexual harassment or violence to campus authorities**. If you would like to speak to a confidential advocate, please consider reaching out to the [Berkeley PATH to Care Center](https://care.berkeley.edu/).


## Additional Resources
Please see our [Resources](../resources/) page for course content resources, including the optional supplementary textbook.

### COVID-19 Resources and Support
{:.no_toc}
You can find UC Berkeley’ COVID-19 resources and support [here](https://coronavirus.berkeley.edu/).

### For academic performance, support, and technology
{:.no_toc}
The [Center for Access to Engineering Excellence](https://engineering.berkeley.edu/student-services/academic-support) (Bechtel Engineering Center 227) is an inclusive center that offers study spaces, nutritious snacks, and tutoring in >50 courses for Berkeley engineers and other majors across campus. The Center also offers a wide range of professional development, leadership, and wellness programs, and loans iclickers, laptops, and professional attire for interviews.

As the primary academic support service for undergraduates at UC Berkeley, the [Student Learning Center](http://slc.berkeley.edu/) (510-642-7332) assists students in transitioning to Cal, navigating the academic terrain, creating networks of resources, and achieving academic, personal, and professional goals. Through various services including tutoring, study groups, workshops, and courses, SLC supports undergraduate students in Biological and Physical Sciences, Business Administration, Computer Science, Economics, Mathematics, Social Sciences, Statistics, Study Strategies, and Writing.

The [Educational Opportunity Program](http://eop.berkeley.edu/) (EOP, Cesar Chavez Student Center 119; 510-642-7224) at Cal has provided first generation and low income college students with the guidance and resources necessary to succeed at the best public university in the world. EOP’s individualized academic counseling, support services, and extensive campus referral network help students develop the unique gifts and talents they each bring to the university while empowering them to achieve.

The [Student Technology Equity Program](STEP, https://technology.berkeley.edu/STEP) connects laptops, Wi-Fi hotspots, and other required technology to students in need.

### For mental well-being
{:.no_toc}
The staff of the [UHS Counseling and Psychological Services](https://uhs.berkeley.edu/caps) (Tang Center, 2222 Bancroft Way; 510-642-9494; for after-hours support, please call the 24/7 line at 855-817-5667) provides confidential, brief counseling and crisis intervention to students with personal, academic and career stress. Services are provided by a multicultural group of professional counselors including psychologists, social workers, and advanced level trainees. All undergraduate and graduate students are eligible for CAPS services, regardless of insurance coverage.

To improve access for engineering students, a licensed psychologist from the Tang Center also holds walk-in appointments for confidential counseling in Bechtel Engineering Center 241 (check [here](https://engineering.berkeley.edu/student-services/advising-counseling) for schedule).

### For disability accommodations
{:.no_toc}
The [Disabled Students’ Program](https://dsp.berkeley.edu/) (DSP, 260 César Chávez Student Center \#4250; 510-642-0518) serves students with disabilities of all kinds, including mobility impairments, blind or low vision, deaf or hard of hearing; chronic illnesses (chronic pain, repetitive strain injuries, brain injuries, AIDS/HIV, cancer, etc.) psychological disabilities (bipolar disorder, severe anxiety or depression, etc.), Attention Deficit Disorder/Attention Deficit Hyperactivity Disorder, and Learning Disabilities. Services are individually designed and based on the specific needs of each student as identified by DSP’s Specialists. The Program’s official website includes information on DSP staff, UCB’s disabilities policy, application procedures, campus access guides for most university buildings, and portals for students and faculty.

### For solving a dispute
{:.no_toc}
The [Ombudsperson for Students](https://sa.berkeley.edu/Ombuds) (Sproul Hall 102; 510-642-5754) provides a confidential service for students involved in a University-related problem (academic or administrative), acting as a neutral complaint resolver and not as an advocate for any of the parties involved in a dispute. The Ombudsperson can provide information on policies and procedures affecting students, facilitate students’ contact with services able to assist in resolving the problem, and assist students in complaints concerning improper application of University policies or procedures. All matters referred to this office are held in strict confidence. The only exceptions, at the sole discretion of the Ombudsperson, are cases where there appears to be imminent threat of serious harm.

The [Student Advocate’s Office](https://advocate.berkeley.edu/) (SAO) is an executive, non-partisan office of the ASUC. We offer free, confidential casework services and resources to any student(s) navigating issues with the University, including academic, conduct, financial aid, and grievance concerns. All support is centered around students and aims for an equity-based approach.

### For recovery from sexual harassment or sexual assault
{:.no_toc}
The [Care Line](https://care.berkeley.edu/care-line/) (510-643-2005) is a 24/7, confidential, free, campus-based resource for urgent support around sexual assault, sexual harassment, interpersonal violence, stalking, and invasion of sexual privacy. The Care Line will connect you with a confidential advocate for trauma-informed crisis support including time-sensitive information, securing urgent safety resources, and accompaniment to medical care or reporting.

### For social services
{:.no_toc}
[Social Services](http://uhs.berkeley.edu/students/counseling/socialservices.shtml) provides confidential services and counseling to help students with managing problems that can emerge from illness such as financial, academic, legal, family concerns, and more. They specialize in helping students with pregnancy resources and referrals; alcohol/drug problems related to one’s own or a family member’s use; sexual assault/rape; relationship or other violence; and support for health concerns-new diagnoses or ongoing conditions. Social Services staff will assess a student’s immediate needs, work with the student to develop a plan to meet those needs, and facilitate arrangements with academic departments and advocate for the student with other campus offices and community agencies, as well as coordinate services within UHS.


### For finding community on campus
{:.no_toc}

The mission of the [Berkeley International Office](BIO, http://internationaloffice.berkeley.edu/) (2299 Piedmont Avenue, 510-642-2818) is to provide support with all the essential resources needed to not only survive, but thrive here at UC Berkeley. Their mission is to support you and work together towards justice and belonging for all. They define Basic Needs as the essential resources that impact your health, belonging, persistence, and overall well being. It is an ecosystem that includes: nutritious food, stable housing, hygiene, transportation, healthcare, mental wellness, financial sustainability, sleep, and emergency dependent services. They refuse to accept hunger, homelessness, and all other basic needs injustices as part of our university.

The [Gender Equity Resource Center](https://cejce.berkeley.edu/geneq), fondly referred to as GenEq, is a UC Berkeley campus community center committed to fostering an inclusive Cal experience for all. GenEq is the campus location where students, faculty, staff and Alumni connect for resources, services, education and leadership programs related to gender and sexuality. The programs and services of the Gender Equity Resource Center are focused into four key areas: women; lesbian, gay, bisexual, and transgender (LGBT); sexual and dating violence; and hate crimes and bias driven incidents. GenEq strives to provide a space for respectful dialogue about sexuality and gender; illuminate the interrelationship of sexism, homophobia and gender bias and violence; create a campus free of violence and hate; provide leadership opportunities; advocate on behalf of survivors of sexual, hate, dating and gender violence; foster a community of women and LGBT leaders; and be a portal to campus and community resources on LGBT, Women, and the many intersections of identity (e.g., race, class, ability, etc.).

The [Undocumented Students Program](https://undocu.berkeley.edu/) (119 Cesar Chavez Center; 642-7224) practices a holistic, multicultural and solution-focused approach that delivers individualized service for each student. The academic counseling, legal support, financial aid resources and extensive campus referral network provided by USP helps students develop the unique gifts and talents they each bring to the university, while empowering a sense of belonging. The program’s mission is to support the advancement of undocumented students within higher education and promote pathways for engaged scholarship.

The [Multicultural Education Program](http://mep.berkeley.edu/) (MEP) is one of six initiatives funded by the Evelyn and Walter Haas, Jr. Fund to work towards institutional change and to create a positive campus climate for diversity. The MEP is a five-year initiative to establish a sustainable infrastructure for activities like educational consultation and diversity workshops for the campus that address both specific topics, and to cater to group needs across the campus.

### For basic needs (food, shelter, etc.)
{:.no_toc}
The [Basic Needs Center](https://basicneeds.berkeley.edu/home) (lower level of MLK Student Union, Suite 72) provides support with all the essential resources needed to not only survive, but thrive here at UC Berkeley. Their mission is to support you and work together towards justice and belonging for all. They define Basic Needs as the essential resources that impact your health, belonging, persistence, and overall well being. It is an ecosystem that includes: nutritious food, stable housing, hygiene, transportation, healthcare, mental wellness, financial sustainability, sleep, and emergency dependent services. They refuse to accept hunger, homelessness, and all other basic needs injustices as part of our university.

The [UC Berkeley Food Pantry](https://pantry.berkeley.edu/) (#68 Martin Luther King Student Union) aims to reduce food insecurity among students and staff at UC Berkeley, especially the lack of nutritious food. Students and staff can visit the pantry as many times as they need and take as much as they need while being mindful that it is a shared resource. The pantry operates on a self-assessed need basis; there are no eligibility requirements. The pantry is not for students and staff who need supplemental snacking food, but rather, core food support.

## Acknowledgments!
{:.no_toc}

Course Culture and Additional Resources inspired and adapted with permission from Dr. Sarah Chasins' [Fall 2021 CS 164 Syllabus](https://inst.eecs.berkeley.edu/~cs164/fa21/syllabus.html) and Grace O'Connell, the Asssociate Dean for Inclusive Excellence.
