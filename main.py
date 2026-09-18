__version__ = "3.0.0"

import os
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.utils import platform

if platform == "android":
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
else:
    run_on_ui_thread = lambda f: f


class RsengerApp(App):
    title = "Rsenger"

    def build(self):
        root = FloatLayout()
        self.root = root
        Window.clearcolor = (0.02, 0.024, 0.047, 1)

        logo = os.path.join(os.path.dirname(__file__), "assets", "rsenger_logo.png")
        if os.path.exists(logo):
            self.splash = Image(source=logo, size_hint=(None, None), size=(210, 210),
                                pos_hint={"center_x": .5, "center_y": .56}, allow_stretch=True,
                                keep_ratio=True)
            root.add_widget(self.splash)
        else:
            self.splash = Label(text="RSENGER", color=(1, 1, 1, 1), font_size="34sp", bold=True,
                                halign="center", valign="middle", size_hint=(1, 1))
            root.add_widget(self.splash)

        Clock.schedule_once(lambda *_: self.start_webview(), .20)
        return root

    @run_on_ui_thread
    def start_webview(self):
        if platform != "android":
            if hasattr(self.splash, "text"):
                self.splash.text = "Run this build on Android"
            return

        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        WebView = autoclass("android.webkit.WebView")
        WebSettings = autoclass("android.webkit.WebSettings")
        CookieManager = autoclass("android.webkit.CookieManager")
        View = autoclass("android.view.View")
        Color = autoclass("android.graphics.Color")
        WebChromeClient = autoclass("android.webkit.WebChromeClient")

        self.activity = PythonActivity.mActivity
        self.webview = WebView(self.activity)
        settings = self.webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setDatabaseEnabled(True)
        settings.setAllowFileAccess(True)
        settings.setAllowContentAccess(True)
        settings.setLoadsImagesAutomatically(True)
        settings.setJavaScriptCanOpenWindowsAutomatically(True)
        settings.setSupportMultipleWindows(False)
        settings.setBuiltInZoomControls(False)
        settings.setDisplayZoomControls(False)
        settings.setMediaPlaybackRequiresUserGesture(False)
        settings.setCacheMode(WebSettings.LOAD_DEFAULT)
        settings.setTextZoom(100)

        # A WebChromeClient is important for JS dialogs and modern WebView behaviour.
        self.webview.setWebChromeClient(WebChromeClient())
        CookieManager.getInstance().setAcceptCookie(True)
        CookieManager.getInstance().setAcceptThirdPartyCookies(self.webview, True)
        self.webview.setBackgroundColor(Color.rgb(5, 6, 12))
        self.webview.setOverScrollMode(View.OVER_SCROLL_NEVER)

        html_path = os.path.join(os.path.dirname(__file__), "index.html")
        self.webview.loadUrl("file://" + html_path)
        self.activity.setContentView(self.webview)
        Clock.schedule_once(self.hide_splash, 1.0)

    def hide_splash(self, *_):
        try:
            if self.splash and self.splash.parent:
                self.splash.parent.remove_widget(self.splash)
        except Exception:
            pass

    def on_request_close(self, *args):
        if platform == "android" and getattr(self, "webview", None):
            try:
                if self.webview.canGoBack():
                    self.webview.goBack()
                    return True
            except Exception:
                pass
        return False


if __name__ == "__main__":
    RsengerApp().run()
