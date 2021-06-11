---
layout: page
title: Lecture 20 – Logistic Regression Part 2, Classification
nav_exclude: true
---

# Lecture 20 – Logistic Regression Part 2, Classification

Presented by Fernando Perez

Content by Suraj Rampure, Fernando Perez, Josh Hug, Joseph Gonzalez, Ani Adhikari

- [slides](https://docs.google.com/presentation/d/1DjTv0J5fH4H8QRHV-VsEB67Bb4Uc4RduimVXizySVf4/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfoGE4UR-p96SPlUMsfDHp-h)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/sp21&subPath=lec/lec20/&branch=main)
- [code HTML](../../resources/assets/lectures/lec19/lec19.html)
- (supplementary) [video](https://www.youtube.com/watch?v=ErfnhcEV1O8) on cross-entropy loss and KL divergence

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
<td><strong>20.1</strong> <br>Using thresholds to convert from predicted probabilities to classifications.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/BbyI2iMreeQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdu3cTROsq2oxje0uIakIW5s-NqyI6QawqWGE7LVJstyTcC1w/viewform" target="\_blank">20.1</a></td>
</tr>
<tr>
<td><strong>20.2</strong> <br>Defining several metrics of classifier performance – accuracy, precision, and recall. Confusion matrices.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/4hhYw1iEb7k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeomF6WCG6U_zn4Oc5Sna8ABWnE28UKW4gLcOqwVdcjMU1HEw/viewform" target="\_blank">20.2</a></td>
</tr>
<tr>
<td><strong>20.3</strong> <br>Using scikit-learn to compute accuracy, precision, recall, and confusion matrices.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/REQARx0aBCI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScNS4MHzVboapxvE-rddX0aPrfJ6UNifYSZoQ-EGV55JoWL4w/viewform" target="\_blank">20.3</a></td>
</tr>
<tr>
<td><strong>20.4</strong> <br>Exploring how threshold impacts accuracy, precision, and recall. Precision-recall curves. ROC curves. AUC.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/ILI4VmAcf9I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScRHYdQlAJZwWX9aFi5KTLAXvH8Pp4yXeNqMDfJ3yxM9Dh1Ow/viewform" target="\_blank">20.4</a></td>
</tr>
<tr>
<td><strong>20.5</strong> <br>Exploring the decision boundaries that result from a logistic regression classifier, and their relationship to the model's parameters.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/TVK7aPI_jZg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeFmXUJrHTRbwGKKrDE1EAilA2BHPjbX_u-oM5bwSTEa6Ux9g/viewform" target="\_blank">20.5</a></td>
</tr>
<tr>
<td><strong>20.6</strong> <br>Linear separability. Why we sometimes need regularization for logistic regression.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/DprPIxFVIcc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSevvpw9f56bi06hXrFh_YNbJi-5koBcy5F3mcJUEI4FIle-RQ/viewform" target="\_blank">20.6</a></td>
</tr>
<tr>
<td><strong>20.7</strong> <br>Summary. Brief introduction to multiclass classification.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/Sp2eAPFb2DM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="TODO" target="\_blank">N/A</a></td>
</tr>
