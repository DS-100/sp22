---
layout: page
title: Lecture 2 – Data Sampling and Probability
nav_exclude: true
---

# Lecture 2 – Data Sampling and Probability

Presented by Andrew Bray, Fernando Perez, Suraj Rampure

Content by Fernando Perez, Suraj Rampure, Ani Adhikari, and Joseph Gonzalez

- [slides](https://docs.google.com/presentation/d/1pI4shcpHeNU9vjOaG9l7cYfPe4GWy6hXICpQR8zTH1A/edit#slide=id.p)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfqS6KWu1bborXNSvQGGVNmp)

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
<td><strong>2.0</strong> <br> Weekly course schedule. Introduction to the data science life cycle.</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/ZoUOm57rdSU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>2.1</strong> <br> Censuses and surveys. Issues with the US Census.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/1Ljtrhh_LBs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdicnNq5DDOtqGePTGbF7i8Hi34ZmvOp9cLfcJDWNctC12YMA/viewform" target="\_blank">2.1</a></td>
</tr>
<tr>
<td><strong>2.2</strong> <br> Samples. Drawbacks to convenience and quota samples.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/00ZzxbY_1ZM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSe_miHYK6YY64kWfTqzk26Q1s8eo5DlxsEMZDBL0hpgz52h2g/viewform" target="\_blank">2.2</a></td>
</tr>
<tr>
<td><strong>2.3</strong> <br> A case study in sampling bias (1936 election).</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/67C-VvqSkos" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSd4w_L6vZULi97gry58x8kKgn_gxis4FpJt8T9rEl4Rnk_Phw/viewform" target="\_blank">2.3</a></td>
</tr>
<tr>
<td><strong>2.4</strong> <br> Sources of bias, and a formal definition of sampling frames.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/HCN_D5-PqPw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfkSPouR3K05zc_ASiRT_y7Zi3ZtEkqr-4BQDw61fENES6X8w/viewform" target="\_blank">2.4</a></td>
</tr>
<tr>
<td><strong>2.5</strong> <br> Probability samples, and why we need them.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/DF5UNpjpfXY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSe3wfbnIkPhf52M5oaJ-mfl6zo8EbGjAA9JUG5wQeKxYhF3JA/viewform" target="\_blank">2.5</a></td>
</tr>
<tr>
<td><strong>2.6</strong> <br> Introducing binomial and multinomial probability calculations.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/ptormkLsXBA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdg12Iqi8QBcoJ8VR3W7GIFNNGp1gThE6dzVqwzLEcZCgK7EA/viewform" target="\_blank">2.6</a></td>
</tr>
<tr>
<td><strong>2.7</strong> <br> Generalizing binomial and trinomial probability calculations.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/OV4q_ZAq3JY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSc9hNve3nO0s9AGU8L9lT6UEDWNP6CMapcku9dN2jSnrpvcyg/viewform" target="\_blank">2.7</a></td>
</tr>
<tr>
<td><strong>2.8 (Extra)</strong> <br> Using permutations and combinations to derive the binomial coefficient.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/4j2mFGkvwWE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScT0hkAtv60WsNeI8Lp4xBgbZAm5BKysdSdEFjA2mKaHDbdUQ/viewform" target="\_blank">2.8</a></td>
</tr>
<tr>
<td><strong>2.9 (Extra)</strong> <br> Example usages of the binomial coefficient. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/lR6FeO5Pgss" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfWgaBrElxt2rOeM_t3ZWqQvKvKFSrUWU2RQBmn7r3enf4E_A/viewform" target="\_blank">2.9</a></td>
</tr>
