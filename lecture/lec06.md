---
layout: page
title: Lecture 6 – Data Cleaning and EDA
nav_exclude: true
---

# Lecture 6 – Data Cleaning and EDA

Presented by Anthony D. Joseph

Content by Anthony D. Joseph, Joseph Gonzalez, Deborah Nolan, Joseph Hellerstein

- [slides](https://docs.google.com/presentation/d/1d75B4Co8jHeSam8Mt5nZNfyIAVu_f1WFNIqdz19D7To/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfr0cSQwchFj1HM8HtNv3jdg)
- [code](https://github.com/DS-100/sp21/tree/main/lec/lec07) ([launch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/sp21&subPath=lec/lec07/&branch=main))
- [code HTML](../../resources/assets/lectures/lec07/lec07.html)
- [(bonus) Joe Hellerstein's primer on data models](https://drive.google.com/file/d/1nLftW2PaJNot-J9zIgES4HchXTTrB_63/view?usp=sharing)

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
<td><strong>7.0</strong> <br>Announcements.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/YQJqBWqPHRk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>7.1</strong> <br>Exploratory data analysis and its position in the data science lifecycle. The relationship between data cleaning and EDA.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/aT4rAFtgTQM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdhM3ZZO9BR50VqX1iqhSyKIW6cLag51W36Pd5kmMQKBgkRCA/viewform" target="\_blank">7.1</a></td>
</tr>
<tr>
<td><strong>7.2</strong> <br>Exploring various different data storage formats and their tradeoffs.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/XoeWbniS_K0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSf8FKACS4oa39ENYLHTVDWi35veaUqOd95AaU70NiFvIQyyxQ/viewform" target="\_blank">7.2</a></td>
</tr>
<tr>
<td><strong>7.3</strong> <br>Primary keys and foreign keys. Eliminating redundancy in tables.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/uhb7WXxau80" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSf3gWujjkLunnVgvYeO5ICXPZw3h4gdVIwSbMkhOwM_7w5VJw/viewform" target="\_blank">7.3</a></td>
</tr>
<tr>
<td><strong>7.4</strong> <br>Defining and discussing the terms quantitative discrete, quantitative continuous, qualitative ordinal, qualitative nominal.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/qj8KtCBTkpQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeYe4HhdLEVddHZdgLo-va3MYJUc8EqMHUL9zp1bL2FwXkwXA/viewform" target="\_blank">7.4</a></td>
</tr>
<tr>
<td><strong>7.5</strong> <br>Discussing the granularity and scope of our data to ensure that it's appropriate for analysis. Discussing various methods of encoding time, and flaws to be aware of.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/WCpMSFi_VnI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdLSiF303lHiqydSiyJPTYAuA91f8BdzzgPkyr8uH3UfPrctA/viewform" target="\_blank">7.5</a></td>
</tr>
<tr>
<td><strong>7.6</strong> <br>Ways in which our data can be incorrect or corrupt. Different methods for addressing missing values, and their tradeoffs.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/EaicN4nauGY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfiFwPE7wsuvTkT1BxcQFsEb9_govzRT3a7L3XucyVGyLk9Mw/viewform" target="\_blank">7.6</a></td>
</tr>
<tr>
<td><strong>7.7</strong> <br>Summarizing the process of EDA.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/2SLRHQNcta4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScPFnU-x3IuHY4G9mas5f9crJhJQdsxAk5X8q7paG4Ogr9I2g/viewform" target="\_blank">7.7</a></td>
</tr>
<tr>
<td><strong>(Optional) 7.8</strong> <br>A demo of EDA on real data.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/Ta2MysR0_G0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td>N/A</td>
</tr>
