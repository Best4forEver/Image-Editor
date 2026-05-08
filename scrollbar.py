import tkinter as tk

class ScrollablePanel(tk.Frame):
    def __init__(self, parent, bg="#1A1A2E", width=220, **kwargs):
        super().__init__(parent, bg=bg, width=width, **kwargs)
        self.pack_propagate(False)   

        # ── Canvas + Scrollbar ─────────────────────
        self.canvas    = tk.Canvas(self, bg=bg,
                                   highlightthickness=0, width=width)
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL,
                                      command=self.canvas.yview)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # ── Inner Frame ────────────────────────────
        self.inner = tk.Frame(self.canvas, bg=bg)
        self.canvas.create_window((0, 0), window=self.inner, anchor=tk.NW)

        # ── Auto Update Scroll ─────────────────────
        self.inner.bind("<Configure>", self._update_scroll)

        # ── Mouse Wheel ────────────────────────────
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.inner.bind("<MouseWheel>",  self._on_mousewheel)

    def _update_scroll(self, e):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, e):
        self.canvas.yview_scroll(-int(e.delta / 60), "units")



