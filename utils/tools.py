class Tool():
    @staticmethod
    def clear(frames):
        for i in frames:
            print(i)
            frame = i.page().mainFrame()
            frame.evaluateJavaScript('reset();')
