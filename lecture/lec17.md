---
layout: page
title: Lecture 17 – Cross-Validation and Regularization
nav_exclude: true
---

# Lecture 17 – Cross-Validation and Regularization

Presented by Isaac Schmidt, Paul Shao

Content by Isaac Schmidt, Joseph Gonzalez, Suraj Rampure, Paul Shao

- [slides](https://docs.google.com/presentation/d/1i4XmSfcBALeeJ3LaQjCGYOUt_mYHRBdpMHQFsxUCskM/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfrIBZQ24xuw2741XBoUX58J)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/su21&subPath=lec/lec17/&branch=main)
- [code HTML](../../resources/assets/lectures/lec17/lec17.html)

17.8 is a **supplementary** video, created by Paul Shao. It gives a great high-level overview of both the bias-variance tradeoff and regularization. **The instructors highly recommend this video.**

**Note:** The demos in this lecture were adapted from demos that Prof. Joeys Gonzalez recorded in Spring 2020. We decided to redo them as the originals significantly rely on sklearn's `Pipeline` object, which is not in scope this semester. However, these notebooks are still available to you, in case you wish to use this style of code for your own projects. They are in the lecture folder on DataHub named `lec17-alt-1.html` and `lec17-alt-2.html`, and you can see the HTML for [Part 1](../../resources/assets/lectures/lec17/lec17-alt-1.html) and [Part 2](../../resources/assets/lectures/lec17/lec17-alt-2.html).

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
<td><strong>17.0</strong> <br>Introduction.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/fjXeaRDtktg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>17.1</strong> <br>Training error vs. testing error. Why we need to split our data into train and test. How cross-validation works, and why it is useful.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/CxCkwdnfumY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfFjpL6klnB-Ffo8ioiU-J4sZlbiSk5TYcpzU6s6paL77SCoQ/viewform?usp=sf_link" target="\_blank">17.1</a></td>
</tr>
<tr>
<td><strong>17.2</strong> <br>Using scikit-learn to construct a train-test split. Building a linear model and determining its training and test error.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/WpbXyB58HC0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSe-jjZHAMVaz7s6e435shYIziFOh5qEFlsYM0MkEdyaWkYhpw/viewform?usp=sf_link" target="\_blank">17.2</a></td>
</tr>
<tr>
<td><strong>17.3</strong> <br>Implementing cross-validation, and using it to help select a model.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/QJ26VK9-_Sk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSc56m4kRDk8sCPf4DWgNigFLjjQorthevUiH2lxF3JSSlt1jg/viewform?usp=sf_link" target="\_blank">17.3</a></td>
</tr>
<tr>
<td><strong>17.4</strong> <br>An introduction to regularization.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/yXkO_J9hkXc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeOiR0On-JDZO9gLmbs-pIsO0zHHzJV50hQRHO91MrUTPSHRw/viewform?usp=sf_link" target="\_blank">17.4</a></td>
</tr>
<tr>
<td><strong>17.5</strong> <br>Reformulating the regularization optimization problem. Relationship between the hyperparameter and error. Standardizing features.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/W19a_mEr4gk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdv0Yeoa_7AJdPbb-xGGtv-iUIgxe1AFxG_HDLMNr2FqEOLtw/viewform?usp=sf_link" target="\_blank">17.5</a></td>
</tr>
<tr>
<td><strong>17.6</strong> <br>Ridge regression and LASSO regression. Distinction between parameters and hyperparameters.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/U3DOU7QbX8Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScsFllWrBZG8CyoCU63K6CGX2ktrfl-jsQS0364992bDZ_5qg/viewform?usp=sf_link" target="\_blank">17.6</a></td>
</tr>
<tr>
<td><strong>17.7</strong> <br>Using cross-validation with ridge regression and LASSO regression in scikit-learn.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/pHsG90Dp9t8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdQdno-_L4I8yweaVY8PtEXD6zF1m3B2ipwkm9_AgP9OsVywA/viewform?usp=sf_link" target="\_blank">17.7</a></td>
</tr>
<tr>
<td><strong>17.8</strong> <br>**Supplemental.** An overview of the bias-variance tradeoff, and how it interfaces with regularization.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/U2J75Iq2nrk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td>N/A</td>
</tr>
