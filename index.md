---
layout: page
title: Home / Schedule
nav_order: 1
description: A week-to-week description of the content covered in the course.
course:
  edstem: https://edstem.org/us/courses/15436/
  faq: https://ds100.org/sp22faq
---

# Principles and Techniques of Data Science

{: .mb-2 }
UC Berkeley, Spring 2022
{: .mb-0 .fs-6 .text-grey-dk-000 }


<div>
<!-- {% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %} -->
</div>

Jump to the calendar [here](#calendar).

+ **Frequently Asked Questions:** Before posting on the [class Ed]({{page.course.edstem}}), please read the [class FAQ page]({{page.course.faq}}).
+ The [Syllabus]({{site.baseurl}}/syllabus) page contains a detailed explanation of how each course component will work this semester, given the course will be taught in a hybrid format.
+ The scheduling of all weekly events is in the [Calendar]({{ site.baseurl }}/calendar).
+ Zoom links for any remote live events will be posted on EdStem once they are available.
+ Textbook readings are optional and actively in development. See the [Resources]({{site.baseurl}}/resources/#textbook) for more details.
+ **Note:** The schedule of lectures and assignments is subject to change.

**Friday, January 14 Announcement**
+ The first lecture will be Tuesday 1/18, 3:30pm-5:00pm **online on Zoom**. Please attend, but it will be recorded and posted online in case you miss it. The Zoom link is available on the [class Ed]({{page.course.edstem}}), signup link on [class FAQ]({{page.course.faq}}). Subsequent lectures through Thursday 1/27 will also be online, though we are in the process of requesting permission to have a limited number of in-person attendees; we'll keep you posted. 
Starting Tuesday 2/1 we will resume the hybrid instruction as described in the [Syllabus]({{ site.baseurl }}/syllabus).
+ **All discussions, Lab Help Sections, and office hours will be held online for the first two weeks (through 1/28)**. We will post Zoom links on EdStem. In-person sections will go back to in-person starting the week of 1/31.
+ There will be a discussion the first week, on Friday 1/21. You will be able to sign up for discussion section starting Tuesday 1/18. We will post an announcement on EdStem with more specifics.
+ All Lab Help Sections and Office Hours start the second week (week of 1/24). You do not need to sign up for Lab Help Sections. More info on the [Syllabus]({{ site.baseurl}}/syllabus).

<br><br>

<a name="calendar"></a>
## Calendar

{% for module in site.modules %}
{{ module }}
{% endfor %}
