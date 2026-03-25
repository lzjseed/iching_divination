#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
易经数据导出脚本
功能：从iching库导出完整的64卦数据库，生成前端可用的iching_data.js文件
自动保存到app/src/main/assets/目录，供Android APK打包使用
使用方法：python3 createIchingData.py
"""
import json
import os
import sys

# 尝试导入iching库
try:
    import iching
except ImportError:
    print("❌ 错误：未找到iching库，请先安装：pip install iching")
    sys.exit(1)

# 读取原始易经数据
base_path = os.path.dirname(iching.__file__)
data_path = os.path.join(base_path, 'package_data.dat')

if not os.path.exists(data_path):
    print(f"❌ 错误：未找到数据文件 {data_path}")
    sys.exit(1)

with open(data_path, encoding='utf-8') as f:
    data = json.load(f)

# 生成JS格式数据
output = "window.ichingData = " + json.dumps(data, ensure_ascii=False, indent=2) + ";"

# 输出路径
output_path = os.path.join(os.path.dirname(__file__), 'app', 'src', 'main', 'assets', 'iching_data.js')

# 保存文件
with open(output_path, "w", encoding="utf-8") as f:
    f.write(output)

print(f"✅ iching_data.js 生成完成！")
print(f"📁 输出路径：{output_path}")
print(f"📊 共加载 {len(data)} 卦数据")