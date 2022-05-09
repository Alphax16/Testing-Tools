import threading
import mouse
import keyboard


class ClicksNKeysEventsRecorder:
    def recorder(self):
        events = []
        mouse_events = []

        mouse.hook(mouse_events.append)
        events.append(mouse_events)
        keyboard.start_recording()


        keyboard.wait('esc')


        mouse.unhook(mouse_events.append)
        events.append(mouse_events)
        keyboard_events = keyboard.stop_recording()
        events.append(keyboard_events)

        print(keyboard_events)
        print(events)


        # k_thread = threading.Thread(target = lambda: keyboard.play(keyboard_events))
        # k_thread.start()
        #
        # m_thread = threading.Thread(target = lambda: mouse.play(mouse_events))
        # m_thread.start()
        #
        #
        # k_thread.join()
        # m_thread.join()

        return {'Events': events, 'Keys': keyboard_events, 'Clicks': mouse_events}

    def player(self, events):
        keys = events['Keys']
        k_thread = threading.Thread(target=lambda: keyboard.play(keys))
        k_thread.start()

        clicks = events['Clicks']
        m_thread = threading.Thread(target=lambda: mouse.play(clicks))
        m_thread.start()

        k_thread.join()
        m_thread.join()

        return events

    def recordNPlay(self):
        events = self.recorder()
        self.player(events)
        return events


def main():
    clicks_n_keys = ClicksNKeysEventsRecorder()
    clicks_n_keys.recordNPlay()


if __name__ == '__main__':
    main()


