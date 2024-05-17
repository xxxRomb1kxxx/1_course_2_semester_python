import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, (ax1, ax2, ax_sum) = plt.subplots(3, 1, figsize=(10, 8))

x = np.linspace(0, 2 * np.pi, 1000)
amp1_init, freq1_init = 1, 1
amp2_init, freq2_init = 1, 1

wave1, = ax1.plot(x, amp1_init * np.sin(freq1_init * x))
wave2, = ax2.plot(x, amp2_init * np.sin(freq2_init * x))
wave_sum, = ax_sum.plot(x, amp1_init * np.sin(freq1_init * x) + amp2_init * np.sin(freq2_init * x))


ax1.set_title('Wave 1')
ax2.set_title('Wave 2')
ax_sum.set_title('Sum of Waves')


axamp1 = plt.axes([0.25, 0.02, 0.65, 0.03])
axfreq1 = plt.axes([0.25, 0.06, 0.65, 0.03])
axamp2 = plt.axes([0.25, 0.10, 0.65, 0.03])
axfreq2 = plt.axes([0.25, 0.14, 0.65, 0.03])

amp1_slider = Slider(axamp1, 'Amp 1', 0.1, 2.0, valinit=amp1_init)
freq1_slider = Slider(axfreq1, 'Freq 1', 0.1, 5.0, valinit=freq1_init)
amp2_slider = Slider(axamp2, 'Amp 2', 0.1, 2.0, valinit=amp2_init)
freq2_slider = Slider(axfreq2, 'Freq 2', 0.1, 5.0, valinit=freq2_init)

def update(val):
    amp1 = amp1_slider.val
    freq1 = freq1_slider.val
    amp2 = amp2_slider.val
    freq2 = freq2_slider.val
    wave1.set_ydata(amp1 * np.sin(freq1 * x))
    wave2.set_ydata(amp2 * np.sin(freq2 * x))
    wave_sum.set_ydata(amp1 * np.sin(freq1 * x) + amp2 * np.sin(freq2 * x))
    fig.canvas.draw_idle()

amp1_slider.on_changed(update)
freq1_slider.on_changed(update)
amp2_slider.on_changed(update)
freq2_slider.on_changed(update)

plt.show()
