# pip mirror source
配置Python使用镜像源通常是为了解决在国内访问Python Package Index (PyPI) 速度慢的问题。
虽然官方并没有提供专门的“官方镜像”，但你可以通过使用一些受信任的第三方镜像服务来加速包的下载过程。

在中国，最常用的镜像源之一是清华大学TUNA的镜像服务。以下是配置Python使用TUNA镜像源的步骤：

### 使用pip命令行临时配置

如果你只是想临时使用镜像源安装一个包，可以在安装命令中直接指定镜像源的URL：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PackageName
```

这里的`PackageName`是你想要安装的包的名称。

### 永久配置pip使用镜像源

为了永久改变pip的行为，你需要创建或修改pip的配置文件。这个文件可能是`pip.conf`（Linux/macOS）或`pip.ini`（Windows）。

#### 对于Linux/macOS：

1. 在用户家目录下创建或编辑`.pip/pip.conf`文件（如果文件或目录不存在，需要先创建）：

```bash
mkdir -p ~/.pip
echo "[global]" > ~/.pip/pip.conf
echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> ~/.pip/pip.conf
```

#### 对于Windows：

1. 在 `%HOME%` 目录下创建或编辑 `pip.ini` 文件（通常是 `C:\Users\<用户名>\pip\pip.ini`），如果该目录或文件不存在，请先创建：

```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### 注意事项

- 上述配置将全局更改pip的下载源，适用于所有的pip命令。
- 如果你使用的是虚拟环境（如venv或conda），并且希望只在特定环境中使用镜像源，可以在激活该环境后再按照上述方法在环境的特定目录下创建配置文件。
- 确保配置文件的格式正确，以免引发意外错误。
- 除了清华大学TUNA，还有其他镜像源可供选择，如阿里云、豆瓣等，只需将上述URL替换为相应镜像源的URL即可。

以上步骤可以帮助你有效利用镜像源加速Python包的下载过程。


<br>

## 恢复默认镜像源

如果你之前已经将Python的pip源从默认的PyPI源更改为了其他镜像源（如清华大学TUNA、阿里云、中科大等镜像），想要恢复回默认的PyPI源，你可以通过以下步骤操作：

### 对于Linux/macOS

1. **删除配置文件中的镜像源设置**：
   如果你之前是在`~/.pip/pip.conf`文件中添加了镜像源配置，可以通过编辑或删除此文件来恢复默认设置。打开终端，执行以下命令：

   ```bash
   rm ~/.pip/pip.conf
   ```

   这将删除配置文件，使pip使用默认的PyPI源。

### 对于Windows

1. **编辑或删除pip配置文件**：
   找到位于`%HOME%\pip\pip.ini`的配置文件（通常是 `C:\Users\<用户名>\pip\pip.ini`），打开并编辑这个文件，移除之前添加的`index-url`行，或者直接删除这个文件。

   如果你愿意手动编辑，打开文件后，移除类似于下面的行：

   ```ini
   [global]
   index-url = https://example-mirror.com/simple
   ```

   然后保存文件。或者，如果你选择删除文件，可以在文件资源管理器中找到并删除`pip.ini`。

### 验证更改

完成上述步骤后，你可以通过运行一个简单的pip命令来验证是否已成功恢复到默认源：

```bash
pip config get global.index-url
```

如果输出显示为`https://pypi.org/simple`，则表示你已成功恢复到了默认的PyPI源。

请注意，如果你在使用虚拟环境，确保是在正确的环境中执行这些操作，或者删除对应的虚拟环境内的pip配置文件。