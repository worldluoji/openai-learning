# asyncio and coroutine
并发与异步编程是现代软件开发中的重要概念，特别是在处理大量I/O操作（如文件读写、网络请求）时，能够显著提升应用的性能。
Python的`asyncio`模块和协程（coroutine）为此提供了强大的支持。下面是对这一主题的一些基本介绍和示例：

### 协程（Coroutine）

协程是一种可以挂起和恢复执行的函数，它允许在执行过程中主动出让控制权，然后在适当的时候继续执行，而不需要外部调用者显式地控制。
在Python中，协程的使用可以追溯到生成器（generator）的引入，但现代意义上的协程是通过`async def`语法糖来定义的，这样的函数在调用时不立即执行，而是返回一个协程对象。
协程特别适合于处理I/O密集型任务，因为在等待I/O操作（如网络请求、磁盘读写）完成时，可以暂停当前协程，让出CPU给其他任务执行。

### asyncio模块

`asyncio`是Python的标准库之一，它提供了一套异步I/O框架，用于编写高性能的并发代码，尤其是在处理大量I/O操作的场景下。
`asyncio`基于协程、事件循环（Event Loop）和任务（Task）等概念构建，其中：

- **事件循环**是`asyncio`的核心，它负责调度和执行协程，管理异步操作，如监控I/O事件、定时器等，并在事件发生时恢复相应的协程执行。
- **任务（Task）**是`asyncio.Future`类的子类，代表了异步操作的封装，它允许跟踪协程的执行状态，方便地取消或获取结果。

### 二者关系

简而言之，`asyncio`模块是异步编程的基础设施，提供了运行协程所需的事件循环、任务管理和调度机制。
而协程则是编写异步代码的基本单位，它们定义了具体的异步逻辑。在`asyncio`框架下，通过定义协程函数（使用`async def`），
然后使用`asyncio.create_task()`或`asyncio.gather()`等方式将协程包装成任务并安排到事件循环中执行，实现了并发处理。

因此，`asyncio`和协程共同工作，使得开发者能够以简洁的代码实现高效的并发处理，尤其适合于处理I/O密集型任务。

### 异步代码编写示例

假设我们要并发地下载多个网页，使用`asyncio`和`aiohttp`库（一个异步HTTP客户端）可以这样实现：

首先，确保安装了`aiohttp`库：
```bash
pip install aiohttp
```

然后编写异步代码：
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        # 使用gather并发执行所有任务
        htmls = await asyncio.gather(*tasks)
        return htmls

urls = [
    'https://www.example.com',
    'https://www.python.org',
    'https://stackoverflow.com'
]

# 运行主异步函数
loop = asyncio.get_event_loop()
html_contents = loop.run_until_complete(main(urls))
loop.close()

for i, content in enumerate(html_contents):
    print(f"Content of {urls[i]}:")
    print(content[:100])  # 打印每个页面的前100个字符
```

在这个例子中，`fetch_url`是一个协程函数，负责异步获取单个网页的内容。
`main`函数创建了一个`aiohttp.ClientSession`实例（用于管理连接和会话），然后为每个URL创建一个任务（task），使用`asyncio.gather`函数并发执行这些任务。
当所有任务完成后，`main`函数返回所有网页的HTML内容。

通过这种方式，即使在单线程环境下，也能高效地同时处理多个I/O操作，大大提高了程序的响应速度和资源利用率。

<br>

## `asyncio.create_task()`和`asyncio.gather()`
`asyncio.create_task()`和`asyncio.gather()`在Python的异步编程中都扮演着重要的角色，但它们的用途和功能有所不同。

### asyncio.create_task()

1. **用途**：`asyncio.create_task()`用于启动一个协程（coroutine）作为一个独立的任务（Task），并将控制立即返回给调用者。这意味着调用者不会等待该任务完成，可以继续执行后续代码，使得多个任务可以并发运行。

2. **特点**：
   - 它返回一个`Task`对象，你可以用这个对象来检查任务的状态、获取结果或取消任务。
   - 从Python 3.7开始引入，之前的版本中通常使用`asyncio.ensure_future()`达到类似目的。
   - 不会阻塞当前协程的执行，非常适合于启动后台任务或并发执行多个任务。

### asyncio.gather()

1. **用途**：`asyncio.gather()`用于并发执行多个协程，并且可以等待所有协程完成。它可以接收一个或多个协程作为参数，并返回一个聚集了所有协程结果的未来（Future）对象。如果任何协程抛出了异常，`gather`也会立即传播这个异常，除非指定了`return_exceptions=True`参数。

2. **特点**：
   - 提供了一种方便的方式来并发执行多个任务，并且可以统一获取它们的结果或异常。
   - 可以通过传递一个任务列表给`gather`，它会等待所有任务完成或直到第一个任务抛出异常。
   - 如果你希望等待一组任务全部完成，并且需要处理它们的结果（成功或失败），`gather`是非常有用的。

### 区别总结

- **并发与等待**：`create_task()`专注于并发执行任务而不等待它们完成，立即返回以便继续执行后续代码；而`gather()`不仅并发执行任务，还会等待所有任务完成并返回结果或异常。
- **结果处理**：`create_task()`单独管理每个任务的结果或状态，而`gather()`则提供了一个集中处理所有传入任务结果的接口。
- **应用场景**：当你需要启动一系列独立任务并继续执行而不等待它们时，使用`create_task()`；当你需要等待一组任务全部完成并可能需要处理它们的集体结果时，使用`gather()`更为合适。


下面是一个使用`asyncio.create_task()`启动并发任务的简单例子。这个例子中，我们将创建几个异步任务来模拟从不同网站下载页面内容，每个任务都会打印下载完成的消息，但不会实际下载任何内容，仅为了演示异步并发的概念。

```python
import asyncio

async def download_page(url):
    # 模拟下载页面的异步操作，这里使用sleep代替真实下载以模拟延时
    await asyncio.sleep(1)  # 模拟下载耗时1秒
    print(f"Downloaded {url} successfully.")

async def main():
    # 定义要下载的页面URL列表
    urls = ["https://example1.com", "https://example2.com", "https://example3.com"]
    
    # 使用asyncio.create_task()启动每个下载任务
    tasks = [asyncio.create_task(download_page(url)) for url in urls]
    
    # 这里我们没有使用await asyncio.gather()等待所有任务完成，
    # 因为create_task()之后的任务已经是并发执行的。
    # 但为了保持示例简单，我们简单等待一段时间确保所有任务有机会完成
    await asyncio.sleep(2)  # 确保所有任务有足够时间执行
    
    # 实际应用中，如果需要等待所有任务完成并处理结果或异常，可以使用
    # await asyncio.gather(*tasks)

asyncio.run(main())
```

在这个例子中，`download_page`是一个协程函数，模拟了下载网页的操作。在`main`协程中，我们使用列表推导式和`asyncio.create_task()`为每个URL创建并启动一个任务。
注意，我们没有直接使用`asyncio.gather()`等待所有任务，而是简单地等待了足够长的时间来模拟所有任务完成。
在实际应用中，根据需求，你可能会选择使用`gather()`来更精确地控制和等待所有任务的完成。