#!/bin/bash
# Builds the APK without Gradle: javac -> dx -> aapt -> zipalign -> apksigner
# Requires: apt install aapt apksigner zipalign dalvik-exchange android-sdk-platform-23
set -e
cd "$(dirname "$0")"
VER_CODE=${VER_CODE:-1}; VER_NAME=${VER_NAME:-1.0}
JAR=/usr/lib/android-sdk/platforms/android-23/android.jar
KS=${KEYSTORE:-$HOME/syprices.keystore}
rm -rf build && mkdir -p build/gen build/classes build/dex
cp ../data/prices.json assets/data/prices.json
aapt package -f -m -J build/gen -M AndroidManifest.xml -S res -I $JAR
javac --release 8 -nowarn -d build/classes -classpath $JAR -sourcepath src:build/gen $(find src build/gen -name '*.java') 2>&1 | grep -v "warning" || true
dalvik-exchange --dex --output=build/dex/classes.dex build/classes
aapt package -f -M AndroidManifest.xml -S res -A assets -I $JAR --min-sdk-version 23 --target-sdk-version 34 \
  --version-code $VER_CODE --version-name $VER_NAME -F build/unsigned.apk
(cd build/dex && aapt add ../unsigned.apk classes.dex >/dev/null)
zipalign -f 4 build/unsigned.apk build/aligned.apk
apksigner sign --ks "$KS" --ks-pass pass:${KS_PASS:-syprices2026} --key-pass pass:${KS_PASS:-syprices2026} --out "build/SY Build Prices.apk" build/aligned.apk
apksigner verify --print-certs "build/SY Build Prices.apk" | head -2
ls -la build/*.apk
