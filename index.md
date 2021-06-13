---
layout: page
title: Home
nav_order: 1
description: A week-to-week description of the content covered in the course.
---

# Principles and Techniques of Data Science

{: .mb-2 }
UC Berkeley, Summer 2021
{: .mb-0 .fs-6 .text-grey-dk-000 }

<div>

<!-- {% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %} -->

</div>

<ul>
<li><b>THIS PAGE IS UNDER CONSTRUCTION. Please don’t interpret anything on this website as truth until this warning is removed. </b></li>
<!-- <li>Please read our <a href="http://www.ds100.org/su21faq">course FAQ</a> before contacting staff with questions that might be answered there.</li>
<li>The <a href="{{ site.baseurl }}/syllabus">Syllabus</a> contains a detailed explanation of how each course component will work this spring, given that the course is being taught entirely online.</li>
<li>The scheduling of all weekly events is in the <a href="{{ site.baseurl }}/calendar">Calendar</a>.</li>
<li>The Zoom links for all live events are in <a href="https://piazza.com/class/kk0b2ef3e7x5s3?cid=6">@6 on Piazza</a>.</li>
<li>Live events and lectures are highlighted in <strong><span style="color: green">green</span></strong> and asynchronous ones in <strong><span style="color: blue">blue</span></strong>.</li>
<li><strong>Note:</strong> The schedule of lectures and assignments is subject to change.</li> -->
</ul>

<br><br>

{% for module in site.modules %}
{{ module }}
{% endfor %}
