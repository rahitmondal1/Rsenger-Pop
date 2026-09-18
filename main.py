__version__ = "3.0.1"

import os

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.utils import platform


# ============================================================
# ANDROID IMPORTS
# ============================================================

if platform == "android":
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
else:
    def run_on_ui_thread(function):
        return function


# ============================================================
# RSENGER APP
# ============================================================

class RsengerApp(App):

    title = "Rsenger"

    def build(self):

        # ----------------------------------------------------
        # Root layout
        # ----------------------------------------------------

        root = FloatLayout()
        self.root = root

        Window.clearcolor = (0.02, 0.024, 0.047, 1)

        # ----------------------------------------------------
        # Logo
        # ----------------------------------------------------

        base_dir = os.path.dirname(os.path.abspath(__file__))

        logo_path = os.path.join(
            base_dir,
            "assets",
            "rsenger_logo.png"
        )

        if os.path.exists(logo_path):

            self.splash = Image(
                source=logo_path,
                size_hint=(None, None),
                size=(210, 210),
                pos_hint={
                    "center_x": 0.5,
                    "center_y": 0.56
                },
                allow_stretch=True,
                keep_ratio=True
            )

        else:

            self.splash = Label(
                text="RSENGER",
                color=(1, 1, 1, 1),
                font_size="34sp",
                bold=True,
                halign="center",
                valign="middle",
                size_hint=(1, 1)
            )

        root.add_widget(self.splash)

        # ----------------------------------------------------
        # Start WebView after Kivy has started
        # ----------------------------------------------------

        Clock.schedule_once(
            self.start_webview,
            0.25
        )

        return root


    # ========================================================
    # CREATE AND START ANDROID WEBVIEW
    # ========================================================

    @run_on_ui_thread
    def start_webview(self, *_args):

        # ----------------------------------------------------
        # Desktop protection
        # ----------------------------------------------------

        if platform != "android":

            if hasattr(self.splash, "text"):
                self.splash.text = "Rsenger runs on Android"

            return


        # ----------------------------------------------------
        # Java / Android classes
        # ----------------------------------------------------

        PythonActivity = autoclass(
            "org.kivy.android.PythonActivity"
        )

        WebView = autoclass(
            "android.webkit.WebView"
        )

        WebViewClient = autoclass(
            "android.webkit.WebViewClient"
        )

        WebChromeClient = autoclass(
            "android.webkit.WebChromeClient"
        )

        CookieManager = autoclass(
            "android.webkit.CookieManager"
        )

        WebSettings = autoclass(
            "android.webkit.WebSettings"
        )

        View = autoclass(
            "android.view.View"
        )

        Color = autoclass(
            "android.graphics.Color"
        )

        File = autoclass(
            "java.io.File"
        )

        Uri = autoclass(
            "android.net.Uri"
        )


        # ----------------------------------------------------
        # Current Android Activity
        # ----------------------------------------------------

        self.activity = PythonActivity.mActivity


        # ----------------------------------------------------
        # Create WebView
        # ----------------------------------------------------

        self.webview = WebView(
            self.activity
        )


        # ====================================================
        # WEBVIEW SETTINGS
        # ====================================================

        settings = self.webview.getSettings()

        # JavaScript
        settings.setJavaScriptEnabled(True)

        # Firebase / local storage
        settings.setDomStorageEnabled(True)
        settings.setDatabaseEnabled(True)

        # Local files
        settings.setAllowFileAccess(True)
        settings.setAllowContentAccess(True)

        # Images
        settings.setLoadsImagesAutomatically(True)

        # JavaScript windows
        settings.setJavaScriptCanOpenWindowsAutomatically(True)

        # Keep everything inside one WebView
        settings.setSupportMultipleWindows(False)

        # Zoom
        settings.setBuiltInZoomControls(False)
        settings.setDisplayZoomControls(False)
        settings.setSupportZoom(False)

        # Media
        settings.setMediaPlaybackRequiresUserGesture(False)

        # Normal cache
        settings.setCacheMode(
            WebSettings.LOAD_DEFAULT
        )

        # Normal text size
        settings.setTextZoom(100)


        # ====================================================
        # WEBVIEW CLIENT
        # ====================================================

        self.webview.setWebViewClient(
            WebViewClient()
        )

        # JavaScript dialogs / console / popup behaviour
        self.webview.setWebChromeClient(
            WebChromeClient()
        )


        # ====================================================
        # COOKIES
        # ====================================================

        cookie_manager = CookieManager.getInstance()

        cookie_manager.setAcceptCookie(True)

        try:
            cookie_manager.setAcceptThirdPartyCookies(
                self.webview,
                True
            )
        except Exception:
            pass


        # ====================================================
        # VISUAL SETTINGS
        # ====================================================

        self.webview.setBackgroundColor(
            Color.rgb(5, 6, 12)
        )

        self.webview.setOverScrollMode(
            View.OVER_SCROLL_NEVER
        )


        # ====================================================
        # LOAD LOCAL INDEX.HTML
        # ====================================================

        html_path = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)
            ),
            "index.html"
        )


        if os.path.exists(html_path):

            try:

                # Android-safe file URI
                html_uri = Uri.fromFile(
                    File(html_path)
                )

                self.webview.loadUrl(
                    html_uri.toString()
                )

            except Exception:

                # Fallback
                self.webview.loadUrl(
                    "file://" + html_path
                )

        else:

            self.webview.loadDataWithBaseURL(
                None,
                """
                <html>
                <body style="
                    background:#05060c;
                    color:white;
                    font-family:sans-serif;
                    text-align:center;
                    padding-top:40%;
                ">
                    <h2>Rsenger</h2>
                    <p>index.html was not found.</p>
                </body>
                </html>
                """,
                "text/html",
                "UTF-8",
                None
            )


        # ====================================================
        # PUT WEBVIEW ON SCREEN
        # ====================================================

        self.activity.setContentView(
            self.webview
        )


        # Remove splash after WebView starts
        Clock.schedule_once(
            self.hide_splash,
            0.8
        )


    # ========================================================
    # HIDE SPLASH
    # ========================================================

    def hide_splash(self, *_args):

        try:

            if (
                self.splash is not None
                and self.splash.parent is not None
            ):
                self.splash.parent.remove_widget(
                    self.splash
                )

        except Exception:
            pass


    # ========================================================
    # ANDROID BACK BUTTON
    # ========================================================

    def on_request_close(self, *_args):

        if platform == "android":

            webview = getattr(
                self,
                "webview",
                None
            )

            if webview is not None:

                try:

                    if webview.canGoBack():

                        webview.goBack()

                        return True

                except Exception:
                    pass

        return False


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    RsengerApp().run()
