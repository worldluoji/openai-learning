
# 目标接口（Target Interface）
class PrintInterface:
    @staticmethod
    def print_data(data: str):
        raise NotImplementedError("This method should be implemented in subclasses.")



# 被适配者（Adaptee）
class IntegerValue:
    def display_int(self, value: int):
        print(f"Integer: {value}")
        
class FloatValue:
    def show_float(self, value: float):
        # .2f表示保留两位小数
        print(f"Float: {value:.2f}")



# 适配器（Adapter） NumberPrinterAdapter适配器类将这些不兼容的接口转换为我们期望的接口，使得客户端可以透明地使用不同类型的数据进行打印操作
class NumberPrinterAdapter(PrintInterface):
    def __init__(self, adaptee):
        self._adaptee = adaptee
    
    def print_data(self, data):
        if isinstance(data, int):
            self._adaptee.display_int(data)
        elif isinstance(data, float):
            self._adaptee.show_float(data)
        else:
            raise ValueError("Unsupported data type. Expected int or float.")

def main():
    integer_adapter = NumberPrinterAdapter(IntegerValue())
    float_adapter = NumberPrinterAdapter(FloatValue())
    
    integer_adapter.print_data(10)    # 应该被适配并正确打印
    float_adapter.print_data(3.14)   # 同样应该被适配并正确打印

if __name__ == "__main__":
    main()