# Radar-positioning
Solve a radar positioning problem using linear programming.

## :pencil2: What is linear programming?

Linear programming is a technique used to solve optimization problems where the elements have a linear relationship.

Linear programs aims to maximize a **objective function** made of **decision variables** subject to **constraints** which ensures that all the elements have a linear relationship and all variables are non-negative.

## :triangular_ruler: Radar positioning model

<!-- In this case we just want to find a combination of variables that solves the puzzle. Therefore there will be no objetive function do be maximized, only linear constraints as follows: -->

<div align="center">

![formula](https://render.githubusercontent.com/render/math?math=$\qquad\qquad\\>\\:\text{Max}\quad\sum_{i=1}^{m}y_i%2B\sum_{i=1}^{m}\sum_{j=1}^{n}A_{ij}z_{ij})

![formula](https://render.githubusercontent.com/render/math?math=$\text{Subject%20to}\quad\sum_{j=1}^{n}z_{ij}=y_{i}\quad\forall%20i)

![formula](https://render.githubusercontent.com/render/math?math=$\qquad\\>\\>\\>\sum_{j=1}^{m}x_{j}=p)

![formula](https://render.githubusercontent.com/render/math?math=$\qquad\qquad\qquad\qquad\qquad\\>\\>x_j\ge%20z_{ij}\quad\forall{i}\forall{j}\\>\text{and}\\>A_{ij}\neq0)

![formula](https://render.githubusercontent.com/render/math?math=$\qquad\qquad\quad\\>x_j,y_i,z_{ij}\in[0,1])

</div>

<!-- - xj → Radar j na posi¸c˜ao j
- yi → Demanda i
- zij → Informa se a demanda i ´e atendida pelo radar j
- Aij → Informa qualidade do sinal do radar j para a demanda i

- Nu´mero de demandas m
- Nu´mero m´aximo de radares p (facultativo)
- Raio maximo de alcance do sinal dos radares r (facultativo)
- Nu´mero de pontos na dire¸c˜ao x
- Nu´mero de pontos na dire¸c˜ao y

We want to generalize the problem to solve a sudoku of any square dimension (9x9, 16x16, 25x25 ...). For that purpose, **n** represents the dimension of the puzzle, **x** are decision variables, **i** represents the columns, **j** represents the rows, **k** represents all possible digitis depending on the puzzle dimension, and **p** and **q** represents an auxiliar variable to iterate in all subgrids.

The first and the second constraints ensures that all columns and all rows will be filled must have only one of the available digits. The third constraint ensures that each cell in the grid will have only one digit. The last constraint ensures that all subgrid will have only one of the available digits. -->