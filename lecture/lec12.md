---
layout: page
title: Lecture 12 – Gradient Descent, sklearn
nav_exclude: true
---

# Lecture 12 – Gradient Descent, sklearn

Presented by Josh Hug

Content by Josh Hug
- [slides](https://docs.google.com/presentation/d/1j9ESgjn-aeZSOX5ON1wjkF5WBZHc4IN7XvTpYnX1pFs/edit?usp=sharing)
- [code](https://github.com/DS-100/sp22/tree/main/lec/lec12){:target="_blank"} ([launch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDS-100%2Fsp22&urlpath=lab%2Ftree%2Fsp22%2Flec%2Flec12%2Flec12.ipynb&branch=main){:target="_blank"})
- [code HTML](../../resources/assets/lectures/lec12/lec12.html){:target="_blank"}
- [recording](https://youtu.be/oX5YAEYycx4){:target="_blank"}

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
<td><strong>12.1</strong> <br />Motivating examples of models.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/o_HGiWy8A-E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/4yY3RZYR6zzrYeZP6" target="\_blank">12.1</a></td>
</tr>
<tr>
<td><strong>12.2</strong> <br />Defining the constant model. Formalizing the notion of a parameter.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/buq9H1xOavU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/m8BJXoKJ3YuWjEkV8" target="\_blank">12.2</a></td>
</tr>
<tr>
<td><strong>12.3</strong> <br />Loss functions and their purpose. Squared loss and absolute loss. Minimizing average loss (i.e. empirical risk).</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/5z3q6E6FC8o" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/ZahFauDFggdqA8438" target="\_blank">12.3</a></td>
</tr>
<tr>
<td><strong>12.4</strong> <br />Minimizing mean squared error for the constant model using calculus, to show that the sample mean is the optimal model parameter in this case.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/_yY-jFZRaVs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/XojKNWZd9F5UmYoi7" target="\_blank">12.4</a></td>
</tr>
<tr>
<td><strong>12.5</strong> <br />Performing the same optimization as in the last video, but by using a non-calculus algebraic manipulation.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/c5pbo8FJuO4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/qYpGybMbmt7QSceUA" target="\_blank">12.5</a></td>
</tr>
<tr>
<td><strong>12.6</strong> <br />Minimizing mean absolute error for the constant model using calculus, to show that the sample median is the optimal parameter in this case. Identifying that this solution isn't necessarily unique.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/fWCuiWAEtUc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/wwb7Jfqcuc6GdZig8" target="\_blank">12.6</a></td>
</tr>
<tr>
<td><strong>12.7</strong> <br />Comparing the loss surfaces of MSE and MAE for the constant model. Discussing the benefits and drawbacks of squared and absolute loss. Recapping the "modeling process".</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/TZd-Jk0ltW8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/BBRXcxd8U958ZMN58" target="\_blank">12.7</a></td>
</tr>
-->
