# Graph Isomorphism SAT

- používá Glucose SAT solver

## zadání

zadání: [sat projekt](https://ktiml.mff.cuni.cz/~svancara/files/sat-projekt.pdf)
problém: [graph isomorphism wikipedia](https://en.wikipedia.org/wiki/Graph_isomorphism_problem)

## zakodování:

### vstup

počet vrcholů a počet hran pak seznam hran mezi vrcholy, takhle pro oba grafy hned za sebou

obecně:

```
n_{0} k_{0}
u_{0} v_{0}
...
u_{k_{0}-1} v_{k_{0}-1}
n_{1} k_{1}
u_{0} v_{0}
...
u_{k_{1}-1} v_{k_{1}-1}
```
příklad:

- pro příklad z wikipedie:
![graph isomorphism](./priklad_wikipedie.png)
[odkaz](https://en.wikipedia.org/wiki/File:Graph_isomorphisms.svg)

```
8 12
0 1
0 2
0 4
1 3
1 5
2 3
2 6
3 7
4 5
4 6
5 7
6 7
8 12
0 4
0 5
0 6
1 4
1 5
1 7
2 4
2 6
2 7
3 5
3 6
3 7
```
