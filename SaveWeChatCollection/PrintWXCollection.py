import pyautogui as pag
import time


# 测试功能
def mainDotest():
    pag.FAILSAFE = True
    width, height = pag.size()
    x, y = 0.5 * width, 0.5 * height
    pag.moveTo(x, y, duration=0.1)
    pag.scroll(-2)


# 主功能
def mainDo():
    # 防止失控：将鼠标移动到屏幕左上角会抛出错误
    pag.FAILSAFE = True
    # 默认操作位置为屏幕正中心
    width, height = pag.size()
    x, y = 0.5 * width, 0.5 * height
    # 激活窗口
    pag.moveTo(x, y-100, duration=1)
    pag.click()
    i = 1
    # 循环控制：i
    while i <= 50:
        pag.moveTo(x, y, duration=1)
        pag.scroll(-229)
        time.sleep(2)
        pag.click()
        # 按钮：浏览器打开
        pag.moveTo(268, 64, duration=1)
        pag.click()
        time.sleep(5)
        pag.moveTo(x, y, duration=1)
        pag.click()
        # 用打印保存
        pag.hotkey('ctrl', 'p')
        time.sleep(10)
        pag.moveTo(1380, 855, duration=1)
        pag.click()
        pag.moveTo(750, 550, duration=1)
        pag.click()
        # 右上角关闭
        pag.moveTo(1820, 20, duration=2)
        pag.click()
        time.sleep(1)
        pag.click()
        i += 1


if __name__ == '__main__':
    mainDo()
