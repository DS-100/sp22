---
layout: page
title: Lecture 6 – Data Cleaning and EDA
nav_exclude: true
---

# Lecture 6 – Data Cleaning and EDA

Presented by Anthony D. Joseph

Content by Anthony D. Joseph, Joseph Gonzalez, Deborah Nolan, Joseph Hellerstein

- [slides](https://docs.google.com/presentation/d/1VW-SlLVnF8lfB2wBvK55JH3_SwNj7zZtQ2YPUL1YyQI/edit)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfrZ3pZkoL1R_J11iSV4FfZV)
- [code](https://github.com/DS-100/su21/tree/main/lec/lec06) ([launch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/su21&subPath=lec/lec06/&branch=main))
- [code HTML](../../resources/assets/lectures/lec06/lec06.html)
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
<td><strong>6.0</strong> <br>Announcements.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/YQJqBWqPHRk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>6.1</strong> <br>Exploratory data analysis and its position in the data science lifecycle. The relationship between data cleaning and EDA.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/aT4rAFtgTQM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSegDf4bsJCBtZ8ZRi5CyC_z0NVUFYQuC5xuwqAn4ogKQflyyA/viewform?usp=sf_link" target="\_blank">6.1</a></td>
</tr>
<tr>
<td><strong>6.2</strong> <br>Exploring various different data storage formats and their tradeoffs.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/XoeWbniS_K0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfUYhE58LltEPk9l2a-nU7U3I1YFtx9p7pbYkaqIeyByym_Ww/viewform?usp=sf_link" target="\_blank">6.2</a></td>
</tr>
<tr>
<td><strong>6.3</strong> <br>Primary keys and foreign keys. Eliminating redundancy in tables.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/uhb7WXxau80" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScfKoOjXhTaJdPiro5b-7iDS621e4MNmbABpYINELSi6zRu8g/viewform?usp=sf_link" target="\_blank">6.3</a></td>
</tr>
<tr>
<td><strong>6.4</strong> <br>Defining and discussing the terms quantitative discrete, quantitative continuous, qualitative ordinal, qualitative nominal.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/qj8KtCBTkpQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScFn86RYpMTvMrJf8bhBy6nP6XvjvpO8pP4LOoI_K1O2hmlkw/viewform?usp=sf_link" target="\_blank">6.4</a></td>
</tr>
<tr>
<td><strong>6.5</strong> <br>Discussing the granularity and scope of our data to ensure that it's appropriate for analysis. Discussing various methods of encoding time, and flaws to be aware of.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/WCpMSFi_VnI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSezqfOelJgfvGzcuzAtQ6zV792r9ON91S0543POC58uD_JJig/viewform?usp=sf_link" target="\_blank">6.5</a></td>
</tr>
<tr>
<td><strong>6.6</strong> <br>Ways in which our data can be incorrect or corrupt. Different methods for addressing missing values, and their tradeoffs.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/EaicN4nauGY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSf7-qbvn8GThR5AGWeeESsnEfzx1J3Ok5jtUV7E-YQ7DfRrrA/viewform?usp=sf_link" target="\_blank">6.6</a></td>
</tr>
<tr>
<td><strong>6.7</strong> <br>Summarizing the process of EDA.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/2SLRHQNcta4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScl9RXNNlnjlnI3j1BQPhCzQ1QJ3HN55UyYWf9qBknU6E_rSQ/viewform?usp=sf_link" target="\_blank">6.7</a></td>
</tr>
<tr>
<td><strong>(Optional) 6.8</strong> <br>A demo of EDA on real data.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/Ta2MysR0_G0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td>N/A</td>
</tr>
