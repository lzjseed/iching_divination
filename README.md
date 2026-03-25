# 易经占卜 Android 版
纯原生WebView套壳的Android占卜应用，正宗三枚铜钱起卦法，完整专业解卦内容，完全离线运行。

## ✨ 功能特点
- 🌰 正宗古法三枚铜钱起卦，自动识别变爻变卦
- 🎬 精美铜钱翻转动画，卦象实时绘制
- 📖 专业解卦内容，包含卦辞、爻辞、变卦完整解读
- 📱 完全离线运行，不需要任何网络权限，APK体积仅3MB左右
- 📱 支持Android 7.0+所有版本，自适应手机和平板

## 🚀 编译步骤

### 1. 环境准备
- 下载安装 Android Studio 最新版：https://developer.android.com/studio
- 安装时选择Android SDK 34版本

### 2. 导入工程
1. 打开Android Studio，选择"Open"导入当前目录
2. 等待Gradle自动同步依赖（第一次需要下载相关组件）

### 3. 生成APK
#### 测试版APK
菜单栏选择 `Build → Make Project`，编译完成后APK路径：
```
app/build/outputs/apk/debug/app-debug.apk
```

#### 正式发布版APK
菜单栏选择 `Build → Generate Signed Bundle / APK`，选择APK，按向导操作即可生成正式签名版APK。

## 🔧 自定义修改

### 更新易经数据库
```bash
# 安装依赖
pip install iching
# 执行脚本自动导出最新数据到assets目录
python3 createIchingData.py
```

### 修改应用名称
修改 `app/src/main/res/values/strings.xml` 中的 `app_name` 字段。

### 修改应用图标
替换 `app/src/main/res/mipmap/` 目录下的图标文件即可。

### 修改页面内容
直接编辑 `app/src/main/assets/index.html` 即可。

## 📦 性能说明
- APK体积：约3MB
- 启动速度：<1秒
- 内存占用：<50MB
- 完全离线，不需要任何权限
