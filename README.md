# Android 易经占卜 APK 编译指南

## 📋 工程说明
这是一个纯原生WebView套壳的Android应用，所有占卜逻辑都在本地静态HTML中实现，完全离线运行，不需要任何网络权限，APK体积只有3MB左右。

## 🚀 编译步骤

### 1. 环境准备
- 下载安装 Android Studio 最新版：https://developer.android.com/studio
- 安装过程中选择安装 Android SDK 34 版本

### 2. 导入工程
1. 打开 Android Studio
2. 选择 "Open" 导入当前 `android-app` 目录
3. 等待 Gradle 自动同步依赖（第一次同步需要下载依赖，可能需要几分钟）

### 3. 生成APK
#### 方式1：测试版APK
菜单栏选择 `Build → Make Project`，编译完成后APK路径：
```
app/build/outputs/apk/debug/app-debug.apk
```
这个版本可以直接安装到手机测试使用。

#### 方式2：正式发布版APK
菜单栏选择 `Build → Generate Signed Bundle / APK`：
1. 选择 "APK"，点击Next
2. 选择你的签名密钥文件（如果没有可以新建一个）
3. 选择release构建类型，点击Finish
4. 正式版APK路径：
   ```
   app/build/outputs/apk/release/app-release.apk
   ```

### 4. 安装测试
- 将生成的APK文件发送到Android手机
- 手机开启"允许安装未知来源应用"权限
- 点击APK文件直接安装即可使用

## 📱 兼容性
- 支持 Android 7.0 (API 24) 及以上所有版本
- 自适应手机和平板各种屏幕尺寸
- 强制竖屏显示，符合手机使用习惯

## 🔧 自定义修改

### 1. 更新易经数据库 iching_data.js
如果需要更新易经数据，工程根目录提供了数据导出脚本 `createIchingData.py`：

#### 使用方法：
```bash
# 安装依赖（仅第一次需要）
pip install iching

# 运行脚本，自动导出最新数据到assets目录
python3 createIchingData.py
```
脚本会自动从 `iching` 库导出完整的易经数据库，生成 `iching_data.js` 并自动放到 `app/src/main/assets/` 目录下，不需要手动复制。

### 2. 修改应用名称
修改 `app/src/main/res/values/strings.xml` 中的 `app_name` 字段即可。

### 3. 修改应用图标
替换 `app/src/main/res/mipmap-*` 目录下的图标文件即可。

### 4. 更新占卜页面内容
直接修改 `app/src/main/assets/index.html` 即可，修改后重新编译APK生效。
