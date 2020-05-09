<h1 align="center">
  Radar Positioning
</h1>

<p align="center">
  Project created to solve a radar positioning problem, part of Linear Programming course of <a src='http://www.ufjf.br/ufjf/'>Universidade Federal de Juiz de Fora</a>
</p>

<p align="center">
    <a href="#satellite-problem-presentation">Problem presentation</a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="#runner-how-to-run">How to run</a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="#pencil-dependencies">Dependencies</a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="#pencil2-what-is-linear-programming">Linear programming</a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="#triangular_ruler-radar-positioning-model">Linear model</a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="#book-resources-and-technologies-computer">Resources</a>&nbsp;&nbsp;
</p>

## :satellite: Problem presentation

We have a 2D region with signal demands to be met by a set of radars. We want to maximize the number of demands met and with better signal quality.

As seen in the image below, we have a solution for a region with 2500 points that radars can be positioned (black dots), 1000 demands to be met and a limit of 200 radars (blue circles). The red dots represents demands that could not be met and the green dots demands that were met.

<p align="center">
    <img src='https://res.cloudinary.com/lorransutter/image/upload/v1589061094/radarSolution.png'/>
</p>

There are two possible variations for this problem:

1. Fixed number of radars to cover demands.
2. No limit of radar to cover demands. In this case, in addition than maximize the number of demands met with better signal, we also minimize the number of radars needed to cover all demands.

## :pencil: Dependencies

Besides, of course, [Python](https://www.python.org/), gurobipy library must be installed too. Installation instructions in [Gurobi](https://www.gurobi.com/documentation/9.0/quickstart_mac/py_python_interface.html).

If you want to visualize the results as in the image above, you will need [PyOpenGL](http://pyopengl.sourceforge.net/).

## :runner: How to run

Open your terminal in the folder you want to clone the project

```sh
git clone https://github.com/LorranSutter/Radar-positioning.git
```

The script **Instance_generator.py** generates a random instance to be solved and the inputs are as follows:

- Int → Number of demands
- Int → Max number of radars (optional)
- Float → Max reach radius of radar signal (optional) [1-50]
- Int → Number of points in x direction
- Int → Number of points in y direction

```sh
python Instance_generator.py <list of inputs>
```

The script **Radar_max.py** is the main variation of the problem, with a fixed number of radars. There is only one input, which are the files in *Instances* folder.

```sh
python Radar_max.py Instances/<file>
```

The script **Radar_min.py** is the second variation of the problem, with no limit of radars. The input is the same as the above.

```sh
python Radar_min.py Instances/<file>
```

Finally, the script **Display_terrain.py** uses OpenGL to show the results of the previous scripts. Inputs needs two files, one from *InstancesPoints* folder and other from *Solutions* folder. Both must have the same suffixes, for example, instance_Points49_10_5 and instance49_10_5_out.sol

```sh
python Display_terrain.py InstancesPoints/<file> Solutions/<file>
```

## :pencil2: What is linear programming?

Linear programming is a technique used to solve optimization problems where the elements have a linear relationship.

Linear programs aims to maximize a **objective function** made of **decision variables** subject to **constraints** which ensures that all the elements have a linear relationship and all variables are non-negative.

## :triangular_ruler: Radar positioning model

For this problem, we want to maximize the number of demands met and with better signal quality. The meaning of the variables and parameters is as follows:

- xj → Radar j in the position j
- yi → Demand i
- zij → It says whether the demand i has been me by the radar j
- Aij → It says the signal quality of the radar j fot the demand i

- m → Number of demands
- n → Number of locations where the radars may be positioned
- p → Max number of radars

<div align="center">

![formula](https://render.githubusercontent.com/render/math?math=$\qquad\qquad\\>\\:\text{Max}\quad\sum_{i=1}^{m}y_i%2B\sum_{i=1}^{m}\sum_{j=1}^{n}A_{ij}z_{ij})

![formula](https://render.githubusercontent.com/render/math?math=$\text{Subject%20to}\quad\sum_{j=1}^{n}z_{ij}=y_{i}\quad\forall%20i)

![formula](https://render.githubusercontent.com/render/math?math=$\qquad\\>\\>\\>\sum_{j=1}^{m}x_{j}=p)

![formula](https://render.githubusercontent.com/render/math?math=$\qquad\qquad\qquad\qquad\qquad\\>\\>x_j\ge%20z_{ij}\quad\forall{i}\forall{j}\\>\text{and}\\>A_{ij}\neq0)

![formula](https://render.githubusercontent.com/render/math?math=$\qquad\qquad\quad\\>x_j,y_i,z_{ij}\in[0,1])

</div>

Each row of the model above is explained as follows:

1. Objective function that aims to maximize the sum of demands met and the signal quality on demand.
2. Number of demands met must be equals to number of demands.
3. Number of radars in position j must be equals to the max number of radars available.
4. Number of radars in position j must be grater or equals to the demands met by this radar in the position j.
5. All radar, demand and demand met must be 0 or 1.

<!-- We want to generalize the problem to solve a sudoku of any square dimension (9x9, 16x16, 25x25 ...). For that purpose, **n** represents the dimension of the puzzle, **x** are decision variables, **i** represents the columns, **j** represents the rows, **k** represents all possible digitis depending on the puzzle dimension, and **p** and **q** represents an auxiliar variable to iterate in all subgrids.

The first and the second constraints ensures that all columns and all rows will be filled must have only one of the available digits. The third constraint ensures that each cell in the grid will have only one digit. The last constraint ensures that all subgrid will have only one of the available digits. -->

## :book: Resources and technologies :computer:

- [Gurobi](https://www.gurobi.com/documentation/9.0/quickstart_mac/py_python_interface.html)
- [Python](https://www.python.org/)
- [PyOpenGL](http://pyopengl.sourceforge.net/)
