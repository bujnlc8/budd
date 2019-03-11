[![Build Status](https://travis-ci.com/linghaihui/budd.svg?branch=master)](https://travis-ci.com/linghaihui/budd)

一个环境变量收集器。

项目名称来自魔兽世界的一个角色[巴德（Budd）](https://zh.wikipedia.org/wiki/%E9%AD%94%E5%85%BD%E7%B3%BB%E5%88%97%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8#%E9%9C%B8%E5%BE%B7%EF%BC%88Budd%EF%BC%89), 没有什么意思，就是觉得顺口。

支持以下用法:

1. 收集以`BAR_`开头的环境变量， 再对值调用`json.loads`，因此，环境变量的值需要符合json的格式。
```
import budd.json.bar as f

f.foo
f["foo"]

```

2. 收集以`BAR_`开头的环境变量，原样输出值。

```
import budd.raw.bar as f

f.foo
f["foo"]
```