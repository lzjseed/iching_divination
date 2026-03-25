# Add project specific ProGuard rules here.
-keepclassmembers class * {
    @android.webkit.JavascriptInterface <methods>;
}
-keep public class com.iching.divination.** { *; }
-keepattributes JavascriptInterface