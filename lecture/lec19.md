---
layout: page
title: Lecture 19 – Logistic Regression, Part 1
nav_exclude: true
---

# Lecture 19 – Logistic Regression, Part 1

Presented by Fernando Perez, Suraj Rampure

Content by Suraj Rampure, Josh Hug, Joseph Gonzalez, Ani Adhikari

- [slides](https://docs.google.com/presentation/d/12wrGaQdhna2cs7chxcknV85YvInMajXIJN3Z1Z8NYm0/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfpVrztbjoDxeQar0NxjsxTf)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/sp21&subPath=lec/lec19/&branch=main)
- [code HTML](../../resources/assets/lectures/lec18/lec18.html)

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
<td><strong>19.1</strong> <br>Classification, and a brief overview of the machine learning taxonomy.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/n24YOheURw0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfZBbF4L0iYBCqNKd8jz10sQsewErNTmEQv661biAHEPDYkrQ/viewform" target="\_blank">19.1</a></td>
</tr>
<tr>
<td><strong>19.2</strong> <br>Pitfalls of using least squares to model probabilities. Creating a graph of averages to motivate the logistic regression model.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/5tO27qVS3zA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSe8t2_YNe9RDP1rBaep3-O1HcgeNq_n8WkCUr32mZCLqKT8IA/viewform" target="\_blank">19.2</a></td>
</tr>
<tr>
<td><strong>19.3</strong> <br>Deriving the logistic regression model from the assumption that the log-odds of the probability of belonging to class 1 is linear.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/RPeLrOS3FjA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdVFWXBa9NRPbQVxzDur289qikYIIVfUb68VbhhQiTPqkHQHw/viewform" target="\_blank">19.3</a></td>
</tr>
<tr>
<td><strong>19.4</strong> <br>Formalizing the logistic regression model. Exploring properties of the logistic function. Interpreting the model coefficients.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/A-mD0g3cXBo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSe43oGnOHI5d4_0U_EYqE_ZYls34EpVG0uTNBoESDv3lnPZKA/viewform" target="\_blank">19.4</a></td>
</tr>
<tr>
<td><strong>19.5</strong> <br>Discussing the pitfalls of using squared loss with logistic regression.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/NmxwIgbMhgc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSd63KxgLbTZqhAtpVVUJshDVbEnhACpft7-FIzDU7sjfviP0A/viewform" target="\_blank">19.5</a></td>
</tr>
<tr>
<td><strong>19.6</strong> <br>Introducing cross-entropy loss, as a better alternative to squared loss for logistic regression.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/zFXrM6Lmlxk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSc2ZvGWUdw2gXPniiko8XEPX3-XaDfDhDiEW0lQlOZCNIdXLg/viewform" target="\_blank">19.6</a></td>
</tr>
<tr>
<td><strong>19.7</strong> <br>Using maximum likelihood estimation to arrive at cross-entropy loss.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/3wqXRQzJBpE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSekYOGwFHets-G_08A-SyDRyFGyhBMsFwmKo5D6lrtNeB3N_Q/viewform" target="\_blank">19.7</a></td>
</tr>
<tr>
<td><strong>19.8</strong> <br>Demo of using scikit-learn to fit a logistic regression model. An overview of what's coming next.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/PWm1KYNFkSM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdpB4Ll7TqBCVNFvHwiR0JArusWu_zqupWYMmqNceJQ82-uFw/viewform" target="\_blank">19.8</a></td>
</tr>
