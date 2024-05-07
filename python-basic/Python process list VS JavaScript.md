# Python process list VS JavaScript
以下是JavaScript和Python在数组/列表操作方面的一个对比表格：

| 操作       | JavaScript                           | Python                                     |
|------------|--------------------------------------|--------------------------------------------|
| 创建       | `let arr = [1, 2, 3];`<br>`let emptyArr = [];` | `lst = [1, 2, 3]`<br>`empty_lst = []`         |
| 访问元素   | `console.log(arr[0]);`                | `print(lst[0])`                             |
| 修改元素   | `arr[0] = 4;`                         | `lst[0] = 4`                                |
| 添加元素   | - `arr.push(4);`<br>- `arr.unshift(0);`<br>- `arr[arr.length] = 5;` | - `lst.append(4)`<br>- `lst.insert(0, 0)`<br>- `lst += [5]` |
| 删除元素   | - `arr.pop();`<br>- `arr.shift();`<br>- `delete arr[0];`<br>- `arr.splice(index, 1);` | - `lst.pop()`<br>- `lst.pop(0)`<br>- `lst.remove(value)`<br>- `del lst[index]` |
| 遍历       | - `for`循环<br>- `for...of`循环           | `for item in lst:`                          |
| 切片       | `let slicedArr = arr.slice(start, end);` | `sliced_lst = lst[start:end]`                 |
| 拼接       | - `let newArr = arr.concat(anotherArr);` | - `combined_lst = lst + another_lst`<br>- `lst.extend(another_lst)` |

此表格总结了两种语言在基本数组/列表操作上的主要命令和语法，帮助直观对比它们之间的异同。


## 解构
```python
l1 = [1,2,3]
l2 = [*l1, 4]
# l2 = [1,2,3,4]
```

```javascript
let l1 = [1,2,3]
let l2 = [...l1, 4]
// l2 = [1,2,3,4]
```