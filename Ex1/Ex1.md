## 1. Refactor

重构**simple_drop.py**

毕竟项目比较简单，既然要让我们将**model**、**controller**分离，我直接就将文件分为了main、model、view、controller。

很显然，**model**中除了已经给出的`Platform`，还可以将代表玩家的`RedBox`提取出来

**controller**主要控制玩家的输入，后续应该还会负责处理deltaTime，但是因为原代码直接设置成了固定每秒30帧，这个也就没必要了

```python
# 每秒三十帧，位于main函数的while循环
pygame.time.Clock().tick(30)
```

**view**就是负责绘制了，`main`函数将屏幕的surface传递给`Drawer`后，后续所有绘制的调用都在这里进行了。

比如原本的`self.surface.fill((0, 0, 0))`现在需要调用`drawer.clear()`，这样更加统一

事实上，游戏主循环的理想形式是不做任何具体的逻辑处理，而只是负责各个模块的调用，例如

```python
def main():
    while controller.running:
        dt = controller.update()
        platforms.update(dt)
        player.update(dt)
        enemy.update(dt)
        ...
```

也许后续的作业和实验会用这种形式。

## 2. Pygame Exercise

模板有问题，先不做了

