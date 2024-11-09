## 1. Maze Algorithms

补全`mazes.py`中的各个函数，跟着注释做就行。

也让gpt实现了一下代码，发现gpt写python是真厉害，就把我的代码写在注释里了，可以看看gpt是怎么简化代码以及python的妙用

#### Dijkstra 算法

emm，不熟悉python的数据结构，问了gpt应该是要用`heapq`模块，和课上的内容一样，这里实际上是广搜（Dijkstra的特例情况）

#### Shortest Path

一开始要先将所有格子标记为*non_path_marker*，不然之后显示会出问题

因为marks记录的是各个格子到起点的距离，所以从尾找到头会好找点

因为是回溯所以值小的cell肯定是回去的路

```python
for link in current.all_links():
    if self.marks[link] < self.marks[current]:
        current = link
```

gpt用lamda表达式取了最小值，也可以（~~重点是lamda表达式~~）

```python
current = min([neighbor for neighbor in current.all_links()], key = lambda cell: self.marks[cell])
```

#### Binary Tree

没什么好说的，随机取对象用`random.choice`

#### Sidewinder

#### Aldous Broder

照做就行

#### Wilson

gpt在每一次while循环重建一次未访问列表

```python
unvisited_cells = [cell for cell in grid.each_cell() if cell not in visited_cells]
```

运行起来非常慢

应该在开始记录所有未访问格子，后面逐渐移除

#### Recursive Backtracker

递归写起来很方便，但是不让用（~~都用python了考虑什么性能~~）

不过用栈也挺短的

## 2. Hybrid

混合**Aldous Broder**和**Wilson**算法

设定一个阈值，先使用**Aldous Broder**算法生成一部分迷宫，到达阈值后切换到**Wilson**，试了几个阈值(0.1, 0.25, 0.5, 0.75, 0.9)，感觉和**Wilson**速度区别不是很明显。
