package com.mhd.syprices;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.JavascriptInterface;
import android.webkit.ValueCallback;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class MainActivity extends Activity {
    private WebView web;

    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);
        web = new WebView(this);
        setContentView(web);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setDatabaseEnabled(true);
        s.setAllowFileAccess(true);
        s.setTextZoom(100);
        web.addJavascriptInterface(new Bridge(), "Native");
        web.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                if (url.startsWith("http")) {
                    openExternal(url);
                    return true;
                }
                return false;
            }
        });
        web.loadUrl("file:///android_asset/index.html");
    }

    private void openExternal(String url) {
        try {
            startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(url)));
        } catch (Exception ignored) {
        }
    }

    @Override
    public void onBackPressed() {
        web.evaluateJavascript("window.onBack ? String(window.onBack()) : 'false'", new ValueCallback<String>() {
            @Override
            public void onReceiveValue(String v) {
                if (v == null || !v.contains("true")) {
                    MainActivity.super.onBackPressed();
                }
            }
        });
    }

    private static String readAll(InputStream in) throws Exception {
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        byte[] buf = new byte[16384];
        int n;
        while ((n = in.read(buf)) > 0) out.write(buf, 0, n);
        in.close();
        return out.toString("UTF-8");
    }

    private File cacheFile() {
        return new File(getFilesDir(), "prices.json");
    }

    public class Bridge {
        @JavascriptInterface
        public String readAsset(String path) {
            try {
                return readAll(getAssets().open(path));
            } catch (Exception e) {
                return "";
            }
        }

        @JavascriptInterface
        public String readCache() {
            try {
                File f = cacheFile();
                if (!f.exists()) return "";
                return readAll(new FileInputStream(f));
            } catch (Exception e) {
                return "";
            }
        }

        @JavascriptInterface
        public void writeCache(String data) {
            try {
                FileOutputStream o = new FileOutputStream(cacheFile());
                o.write(data.getBytes("UTF-8"));
                o.close();
            } catch (Exception ignored) {
            }
        }

        @JavascriptInterface
        public void openUrl(final String url) {
            runOnUiThread(new Runnable() {
                public void run() {
                    openExternal(url);
                }
            });
        }

        @JavascriptInterface
        public void fetchAsync(final String url, final String callback) {
            new Thread(new Runnable() {
                public void run() {
                    String result = "";
                    try {
                        HttpURLConnection c = (HttpURLConnection) new URL(url).openConnection();
                        c.setConnectTimeout(15000);
                        c.setReadTimeout(20000);
                        c.setUseCaches(false);
                        c.setRequestProperty("Cache-Control", "no-cache");
                        if (c.getResponseCode() == 200) result = readAll(c.getInputStream());
                        c.disconnect();
                    } catch (Exception ignored) {
                    }
                    final String js = callback + "(" + JSONObject.quote(result) + ")";
                    web.post(new Runnable() {
                        public void run() {
                            web.evaluateJavascript(js, null);
                        }
                    });
                }
            }).start();
        }

        @JavascriptInterface
        public String version() {
            return "1.0";
        }
    }
}
