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

+ **All discussions (Week 1), Lab Help Sections (Week 2), and office hours (Week 2) will be held online for the first two weeks (through 1/28)**. Zoom links, discussions sign up link is on Ed [here](https://edstem.org/us/courses/15436/discussion/1021263). In-person sections will go back to in-person starting the week of 1/31.
+ **Frequently Asked Questions:** Before posting on the [class Ed]({{page.course.edstem}}), please read the [class FAQ page]({{page.course.faq}}). FAQ also has Ed join/sign-up link.
+ The [Syllabus]({{site.baseurl}}/syllabus) page contains a detailed explanation of how each course component will work this semester, given the course will be taught in a hybrid format.
+ The scheduling of all weekly events is in the [Calendar]({{ site.baseurl }}/calendar). Zoom links for any remote live events will be posted on EdStem once they are available. Lecture recordings will be up by the morning after lecture.
+ Textbook readings are optional and actively in development. See the [Resources]({{site.baseurl}}/resources/#textbook) for more details.
+ **Note:** The schedule of lectures and assignments is subject to change.

<br><br>

<a name="calendar"></a>
## Calendar

{% for module in site.modules %}
{{ module }}
{% endfor %}
