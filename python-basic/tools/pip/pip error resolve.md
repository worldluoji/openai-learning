# error resolve

1. ERROR: No module named 'pip'

```
python -m ensurepip
```
重新安装pip即可


2. pip install --upgrade pip 报错 ERROR: 
```
Could not install packages due to an EnvironmentError: [WinError 5] 拒绝访问。
....
Consider using the `--user` option or check the permissions.
```

先按提示加上--user
```
pip install --upgrade --user pip
```
如果还是没有成功，可能事镜像源的问题，要修改pip镜像源