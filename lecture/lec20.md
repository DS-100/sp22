---
layout: page
title: Lecture 20 – Logistic Regression Part 2, Classification
nav_exclude: true
---

# Lecture 20 – Logistic Regression Part 2, Classification

Presented by Suraj Rampure

Content by Suraj Rampure, Josh Hug, Joseph Gonzalez

- [slides](https://docs.google.com/presentation/d/1tMptJfqYT-76pw-P7XWz3TVqQy3qTGth-T4TdQgvERQ/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfrFoQSf1O8cT1Dqb2Wr0e7h)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/su21&subPath=lecture/lec20/)
- [code HTML](../../resources/assets/lectures/lec20/lec20.html)

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
<td><iframe width="300" height="300" height src="https://youtube.com/embed/IDTMTgrGSQ0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScHvaTMxWgLMcN4R0bWfUEDmjOYCFY6r00yTqPx44c9Ano99Q/viewform?usp=sf_link" target="\_blank">20.1</a></td>
</tr>
<tr>
<td><strong>20.2</strong> <br>Defining several metrics of classifier performance – accuracy, precision, and recall. Confusion matrices.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/flODuLEm3kw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSc_5btRitHk1Qs9om-Uj0ysAO6nlcdV-mpHORxjBWfa4B6rkw/viewform?usp=sf_link" target="\_blank">20.2</a></td>
</tr>
<tr>
<td><strong>20.3</strong> <br>Using scikit-learn to compute accuracy, precision, recall, and confusion matrices.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/crX5vMh4nng" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfZzhNsvx1JGpglFhPq41Ikp8WQJuSey_sLqeuzfwqyhIP6_Q/viewform?usp=sf_link" target="\_blank">20.3</a></td>
</tr>
<tr>
<td><strong>20.4</strong> <br>Exploring how threshold impacts accuracy, precision, and recall. Precision-recall curves. ROC curves. AUC.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/Ytsrhj5-lsk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSd4C0azOBPONYObtqFgA11oyjwlGNcYfX_6GqF_McGDRq8_oA/viewform?usp=sf_link" target="\_blank">20.4</a></td>
</tr>
<tr>
<td><strong>20.5</strong> <br>Exploring the decision boundaries that result from a logistic regression classifier, and their relationship to the model's parameters.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/vaQBhcXmOMI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdosR22CgM389t7aZMSc1BFGGOhirOmlybNHsvzHy0u6jG9gQ/viewform?usp=sf_link" target="\_blank">20.5</a></td>
</tr>
<tr>
<td><strong>20.6</strong> <br>Linear separability. Why we sometimes need regularization for logistic regression.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/8aG81hQxUNI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSczA7RR3BNHOs0IIi5nsPpXcpEjzt12jkMlwFczTe3g6AIjZg/viewform?usp=sf_link" target="\_blank">20.6</a></td>
</tr>
<tr>
<td><strong>20.7</strong> <br>Summary. Brief introduction to multiclass classification.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/Sh6QTQt2kfQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td>N/A</td>
</tr>
