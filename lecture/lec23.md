---
layout: page
title: Lecture 23 – Principal Components Analysis
nav_exclude: true
---

# Lecture 23 – Principal Components Analysis

Presented by Raguvir Kunani

Content by Raguvir Kunani, Isaac Schmidt

- [slides](https://docs.google.com/presentation/d/1zpawVI7o2cYA_C_kSQLBjOMrFkSwMDk23JcedzrzttA/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfoExIAxAyXKEqCtINHcippM)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/su21&subPath=lec/lec23/)
- [code HTML](../../resources/assets/lectures/lec23/lec23.html)

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
<td><strong>23.0</strong> <br>Introduction</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/0aSuT_h8ca4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>23.1</strong> <br>Covariance Matrix</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/twfAaeAOkN0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScvbPy6gpNJq9HoLiOeXrOuvT1OycFIrXnSWG_iBsRbqJ4YTw/viewform" target="\_blank">23.1</a></td>
</tr>
<tr>
<td><strong>23.2</strong> <br>Eigenvalues and Eigenvectors</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/omI8YeiIZ74" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfdlA5JBsAn3S4HBKh4Mb8Ur5FQPMd-5TbLT5WDI_c9EGZDug/viewform" target="\_blank">23.2</a></td>
</tr>
<tr>
<td><strong>23.3</strong> <br>Singular Value Decomposition</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/pkDB-kfJ8P0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSc0b1v9IzCisHgRZtnsk1VH4zB0arH_Xy4oLa41aAJqHRVZBA/viewform" target="\_blank">23.3</a></td>
</tr>
<tr>
<td><strong>23.4</strong> <br>Summarizing data with fewer dimensions</td>
<td><iframe width="300" height="500" height src="https://www.youtube.com/embed/A3859APMlGg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSf8ihkrgHgtbypZ6S53rQq6WlUKTpROCHpqDJRjS1b1ygxunA/viewform" target="\_blank">23.4</a></td>
</tr>
<tr>
<td><strong>23.5</strong> <br>Connecting SVD to summarizing data</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/hbNCTrT_7lA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSccbk136Ta5wZgmgp7L3I25qggHJM0Ku2yw7y0cNjymxpY_WQ/viewform" target="\_blank">23.5</a></td>
</tr>
<tr>
<td><strong>23.6</strong> <br>Principal Component Analysis</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/L9Nu8JmKT90" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeXU6EwmjDUDjKbTXe7I_GQ4OkZztJmWoaQSTHbe869TGXmNQ/viewform" target="\_blank">23.6</a></td>
</tr>
<tr>
<td><strong>23.7</strong> <br>Choosing the number of principal components</td>
<td><iframe width="300" height="500" height src="https://www.youtube.com/embed/PqAb5NLZdco" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSef67CEWBEFj84UZWf41enSl0IJu_u2NDSCp-XHeM_kS4qIeA/viewform" target="\_blank">23.7</a></td>
</tr>
<tr>
<td><strong>23.8</strong> <br>Interpreting principal components</td>
<td><iframe width="300" height="500" height src="https://www.youtube.com/embed/6z5bPiVPetc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeCTzPnnu9U02RMuv2n_tS67jmniJBhr_zXfOQYfuGOrXWCbw/viewform" target="\_blank">23.8</a></td>
</tr>
<tr>
<td><strong>23.9</strong> <br>Summary</td>
<td><iframe width="300" height="500" height src="https://www.youtube.com/embed/8fr88-o-svk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>23.10</strong> <br>(Bonus) PCA vs. Regression</td>
<td><iframe width="300" height="500" height src="https://www.youtube.com/embed/DT0BucrEJLw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
