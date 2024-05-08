class Light:
    def turn_on(self):
        print("Light is turned on.")

    def turn_off(self):
        print("Light is turned off.")


class Curtain:
    def open(self):
        print("Curtain is opened.")

    def close(self):
        print("Curtain is closed.")


class SoundSystem:
    def play_music(self):
        print("Music is playing.")

    def stop_music(self):
        print("Music is stopped.")


# HomeAutomationFacade类，它作为上述所有子系统的外观，提供一个简单的接口给客户端使用：
class HomeAutomationFacade:
    def __init__(self):
        self.light = Light()
        self.curtain = Curtain()
        self.sound_system = SoundSystem()

    def watch_movie(self):
        """一键观看电影：关闭灯光，关闭窗帘，播放音乐"""
        self.light.turn_off()
        self.curtain.close()
        self.sound_system.play_music()

    def end_movie(self):
        """结束观影：打开灯光，打开窗帘，停止音乐"""
        self.light.turn_on()
        self.curtain.open()
        self.sound_system.stop_music()


'''
HomeAutomationFacade类作为一个外观，隐藏了家庭自动化系统内部的复杂性，为用户提供了一个简单直观的接口来控制多个子系统。
用户无需了解每个子系统的工作原理，就可以完成一系列操作，如开始观看电影和结束观影。这就是外观模式的应用实例。
'''
if __name__ == "__main__":
    home_automation = HomeAutomationFacade()
    
    print("Starting to watch a movie...")
    home_automation.watch_movie()  # 用户只需调用这个方法，就能完成一系列操作
    
    print("\nMovie ended...")
    home_automation.end_movie()  # 同样，一键结束观影操作