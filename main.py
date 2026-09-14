# Rsenger Android shell — Python/Kivy + native Android WebView
# Keeps the existing Firebase-powered Rsenger web app while packaging it as an Android app.

import os
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.utils import platform

if platform == 'android':
    from android.runnable import run_on_ui_thread
    from jnius import autoclass, cast
else:
    run_on_ui_thread = lambda f: f


class RsengerApp(App):
    title = 'Rsenger'

    def build(self):
        root = FloatLayout()
        self.root = root

        self.splash = Label(
            text='RSENGER',
            color=(1, 1, 1, 1),
            font_size='34sp',
            bold=True,
            halign='center',
            valign='middle',
        )
        root.add_widget(self.splash)

        Window.clearcolor = (0.02, 0.024, 0.047, 1)
        Clock.schedule_once(lambda *_: self.start_webview(), 0.15)
        return root

    @run_on_ui_thread
    def start_webview(self):
        if platform != 'android':
            self.splash.text = 'Run this build on Android'
            return

        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        WebView = autoclass('android.webkit.WebView')
        WebSettings = autoclass('android.webkit.WebSettings')
        CookieManager = autoclass('android.webkit.CookieManager')
        View = autoclass('android.view.View')
        Color = autoclass('android.graphics.Color')

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

        CookieManager.getInstance().setAcceptCookie(True)
        CookieManager.getInstance().setAcceptThirdPartyCookies(self.webview, True)

        self.webview.setBackgroundColor(Color.rgb(5, 6, 12))
        self.webview.setOverScrollMode(View.OVER_SCROLL_NEVER)
        self.webview.getSettings().setTextZoom(100)

        # Local HTML is bundled into the APK.
        html_path = os.path.join(self.user_data_dir, 'index.html')
        if not os.path.exists(html_path):
            # Buildozer copies bundled files into the application directory.
            html_path = os.path.join(os.path.dirname(__file__), 'index.html')

        self.webview.loadUrl('file://' + html_path)
        self.activity.setContentView(self.webview)

        Clock.schedule_once(self.hide_splash, 1.25)

    def hide_splash(self, *_):
        try:
            if self.splash and self.splash.parent:
                self.splash.parent.remove_widget(self.splash)
        except Exception:
            pass

    def on_request_close(self, *args):
        # Android back: navigate inside WebView before exiting the app.
        if platform == 'android' and getattr(self, 'webview', None):
            try:
                if self.webview.canGoBack():
                    self.webview.goBack()
                    return True
            except Exception:
                pass
        return False


if __name__ == '__main__':
    RsengerApp().run()
