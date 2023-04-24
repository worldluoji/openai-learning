# Data Integration
1. 数据集成定义
数据集成就是将多个数据源合并存放在一个数据存储中（如数据仓库），从而方便后续的数据挖掘工作。

2. 数据集成的两种架构：ELT 和 ETL

ETL 的过程为提取 (Extract)——转换 (Transform)——加载 (Load)，在数据源抽取后首先进行转换，然后将转换的结果写入目的地。

ELT 的过程则是提取 (Extract)——加载 (Load)——变换 (Transform)，在抽取后将结果先写入目的地，然后利用数据库的聚合分析能力或者外部计算框架，如 Spark 来完成转换的步骤。

ELT 和 ETL 相比，最大的区别是“重抽取和加载，轻转换”，从而可以用更轻量的方案搭建起一个数据集成平台。使用 ELT 方法，在提取完成之后，数据加载会立即开始。一方面更省时，另一方面 ELT 允许 BI 分析人员无限制地访问整个原始数据，为分析师提供了更大的灵活性，使之能更好地支持业务。

在 ELT 架构中，数据变换这个过程根据后续使用的情况，需要在 SQL 中进行，而不是在加载阶段进行。这样做的好处是你可以从数据源中提取数据，经过少量预处理后进行加载。这样的架构更简单，使分析人员更好地了解原始数据的变换过程。

参考资料：https://time.geekbang.org/column/article/76787