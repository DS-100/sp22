---
layout: page
title: Lecture 2 – Sampling and Probability
nav_exclude: true
slides: 
---

# Lecture 2 – Data Sampling and Probability

Presented by Lisa Yan

Content by Fernando Pérez, Suraj Rampure, Ani Adhikari, Joseph Gonzalez, and Lisa Yan


- [slides](https://docs.google.com/presentation/d/15CbbMS0guv9CNJTTDP4h5T4hrNK8rJJ2cO1rmXo3H3Y/edit?usp=sharing){:target="_blank"}
- [recording](https://youtu.be/CyLQGm_anEo){:target="_blank"}
- [Extra, Summer 2021] Binomial coefficient: [Part 1](https://www.youtube.com/watch?v=4j2mFGkvwWE){:target="_blank"}, [Part 2](https://www.youtube.com/watch?v=lR6FeO5Pgss){:target="_blank"}

<!--
>>>>>>> e0aa630e63dda30b12a0a9581799eb779c89bf4e

 A reminder – the right column of the table below contains _Quick Checks_. These are **not** required but suggested to help you check your understanding. -->

<!-- <table>
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
<<<<<<< HEAD
 <tr>
<td><strong>2.0</strong> <br> Introduction to lecture format.</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/L5hZE3_ECpg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr> 
=======
>>>>>>> e0aa630e63dda30b12a0a9581799eb779c89bf4e
<tr>
<td><strong>2.1.1</strong> <br> Data science lifecycle, case study on squirrels.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/fyhu-Xg2Dfw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/1JHrBWUfrZmbtUc26" target="\_blank">2.1.1</a></td>
</tr>
<tr>
<td><strong>2.1.2</strong> <br> Censuses and surveys. Issues with the US Census.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/iczkTOgVHN8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/vMVBcvzQsypLWBgB7" target="\_blank">2.1.2</a></td>
</tr>
<tr>
<td><strong>2.2</strong> <br> Samples. Drawbacks to convenience and quota samples.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/00ZzxbY_1ZM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/x7piDMsHnfESNMna7" target="\_blank">2.2</a></td>
</tr>
<tr>
<td><strong>2.3</strong> <br> A case study in sampling bias (1936 election).</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/67C-VvqSkos" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/WRKXQcHWpJ3kwWRS9" target="\_blank">2.3</a></td>
</tr>
<tr>
<td><strong>2.4</strong> <br> Sources of bias, and a formal definition of sampling frames.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/HCN_D5-PqPw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/3ybsfiou8qQcQs5d8" target="\_blank">2.4</a></td>
</tr>
<tr>
<td><strong>2.5</strong> <br> Probability samples, and why we need them.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/DF5UNpjpfXY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/ddPUeM6k4BHxhZXL8" target="\_blank">2.5</a></td>
</tr>
<tr>
<td><strong>2.6</strong> <br> Introducing binomial and multinomial probability calculations.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/ptormkLsXBA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/CeX3PMjecZ12N72z9" target="\_blank">2.6</a></td>
</tr>
<tr>
<td><strong>2.7</strong> <br> Generalizing binomial and trinomial probability calculations.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/OV4q_ZAq3JY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/AtNvQBmRxU2VdCPE6" target="\_blank">2.7</a></td>
</tr>
<tr>
<td><strong>2.8 (Extra)</strong> <br> Using permutations and combinations to derive the binomial coefficient.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/4j2mFGkvwWE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/12KkQhCu1zH5Wi3K9" target="\_blank">2.8</a></td>
</tr>
<tr>
<td><strong>2.9 (Extra)</strong> <br> Example usages of the binomial coefficient. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/lR6FeO5Pgss" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/hvX4ascExVahEb3h6" target="\_blank">2.9</a></td>
<<<<<<< HEAD
</tr> -->
