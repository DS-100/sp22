---
layout: page
title: Lecture 6 – Regular Expressions
nav_exclude: true
---

# Lecture 6 - Regular Expressions

Presented by Lisa Yan

Content by Lisa Yan and Josh Hug

- [slides](https://docs.google.com/presentation/d/1xQsqa7e3xDZ9nBiekbSBOecwvQm8pSVGa-FBoV6aJ7E/edit){:target="_blank"}
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDS-100%2Fsp22&urlpath=tree%2Fsp22%2Flec%2Flec06%2Flec06.ipynb&branch=main){:target="_blank"}
- DS100 Regex Reference Sheet on the [Resources page]({{site.baseurl}}/resources#regex-practice){:target="_blank"}
- [recording](https://youtu.be/neFOzXoS06s){:target="_blank"}

<!--
A reminder – the right column of the table below contains _Quick Checks_. These are **not** required but suggested to help you check your understanding.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Video</th>
<th>Quick Check</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>6.1</strong> <br />Exploratory data analysis and its position in the data science lifecycle. The relationship between data cleaning and EDA.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/aT4rAFtgTQM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/Y16q3fw7J9kW34R5A" target="\_blank">6.1</a></td>
</tr>
<tr>
<td><strong>6.2</strong> <br />Exploring various different data storage formats and their tradeoffs.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/XoeWbniS_K0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/qv2r51AJU7KbJDD56" target="\_blank">6.2</a></td>
</tr>
<tr>
<td><strong>6.3</strong> <br />Primary keys and foreign keys. Eliminating redundancy in tables.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/uhb7WXxau80" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/HTHk9rGKFqJ1xjAD6" target="\_blank">6.3</a></td>
</tr>
<tr>
<td><strong>6.4</strong> <br />Defining and discussing the terms quantitative discrete, quantitative continuous, qualitative ordinal, qualitative nominal.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/qj8KtCBTkpQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/JMw598FPKdTwxsPv6" target="\_blank">6.4</a></td>
</tr>
<tr>
<td><strong>6.5</strong> <br />Discussing the granularity and scope of our data to ensure that it's appropriate for analysis. Discussing various methods of encoding time, and flaws to be aware of.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/WCpMSFi_VnI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/3NEUpHTpbGbKtUit7" target="\_blank">6.5</a></td>
</tr>
<tr>
<td><strong>6.6</strong> <br />Ways in which our data can be incorrect or corrupt. Different methods for addressing missing values, and their tradeoffs.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/EaicN4nauGY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/jprX2FjBUaFuZp6C6" target="\_blank">6.6</a></td>
</tr>
<tr>
<td><strong>6.7</strong> <br />Summarizing the process of EDA.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/2SLRHQNcta4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/m2g7epY8ftdKfZ597" target="\_blank">6.7</a></td>
</tr>
<tr>
<td><strong>(Optional) 6.8</strong> <br />A demo of EDA on real data.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/Ta2MysR0_G0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td>N/A</td>
</tr>
-->
