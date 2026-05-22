#!/usr/bin/env python3

"""CHRONO-ARCH v1.0.0 Upload - PyPI
A Computational Framework for Temporal Archaeology and Civilizational Dynamics
"""

import requests
import hashlib
import os
import glob
import sys

TOKEN = ""

print("=" * 60)
print("🏺 CHRONO-ARCH v1.0.0 Upload - PyPI")
print("=" * 60)
print("A Computational Framework for Temporal Archaeology")
print("and Civilizational Dynamics Using AI and Complex Systems Modeling")
print("=" * 60)

# قراءة README.md
try:
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    print(f"\n📄 README.md: {len(readme)} characters")
except FileNotFoundError:
    print("\n❌ README.md not found!")
    sys.exit(1)

# البحث عن ملفات التوزيع
wheel_files = glob.glob("dist/*.whl")
tar_files = glob.glob("dist/*.tar.gz")

if not wheel_files and not tar_files:
    print("\n❌ No distribution files found. Building package...")
    os.system("python -m build")
    
    wheel_files = glob.glob("dist/*.whl")
    tar_files = glob.glob("dist/*.tar.gz")

print(f"\n📦 Distribution files:")
for f in wheel_files + tar_files:
    print(f"   • {os.path.basename(f)}")

# رفع الملفات إلى PyPI
upload_success = False

for filepath in wheel_files + tar_files:
    filename = os.path.basename(filepath)
    print(f"\n📤 Uploading: {filename}")

    # تحديد نوع الملف
    if filename.endswith('.tar.gz'):
        filetype = 'sdist'
        pyversion = 'source'
    else:
        filetype = 'bdist_wheel'
        pyversion = 'py3'

    # حساب الهاشات
    with open(filepath, 'rb') as f:
        content = f.read()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()

    # بيانات الرفع لـ CHRONO-ARCH
    data = {
        ':action': 'file_upload',
        'metadata_version': '2.1',
        'name': 'chrono-arch',
        'version': '1.0.0',
        'filetype': filetype,
        'pyversion': pyversion,
        'md5_digest': md5_hash,
        'sha256_digest': sha256_hash,
        'description': readme,
        'description_content_type': 'text/markdown',
        'author': 'Samir Baladi',
        'author_email': 'gitdeeper@gmail.com',
        'license': 'MIT',
        'summary': 'CHRONO-ARCH: A Computational Framework for Temporal Archaeology and Civilizational Dynamics Using AI and Complex Systems Modeling',
        'home_page': 'https://chronoarch.netlify.app',
        'requires_python': '>=3.9',
        'keywords': 'archaeology, civilizational-dynamics, complex-systems, temporal-graph-networks, dynamical-systems, causal-inference, probabilistic-modeling, environmental-coupling, collapse-theory, archaeological-ai, phase-transitions, knowledge-diffusion, fokker-planck'
    }

    # رفع الملف
    try:
        with open(filepath, 'rb') as f:
            response = requests.post(
                'https://upload.pypi.org/legacy/',
                files={'content': (filename, f, 'application/octet-stream')},
                data=data,
                auth=('__token__', TOKEN),
                timeout=90,
                headers={'User-Agent': 'CHRONO-ARCH-Uploader/1.0'}
            )

        print(f"   Status: {response.status_code}")

        if response.status_code == 200:
            print("   ✅✅✅ SUCCESS!")
            upload_success = True
        else:
            print(f"   ❌ Error: {response.text[:300]}")
            
            # إذا كان الخطأ بسبب الوجود المسبق، حاول الرفع كإصدار جديد
            if "already exists" in response.text:
                print("   ⚠️ Version already exists. Use a new version number.")
                
    except Exception as e:
        print(f"   ❌ Exception: {str(e)}")

print("\n" + "=" * 60)
if upload_success:
    print("✅ CHRONO-ARCH v1.0.0 uploaded successfully!")
    print("🔗 https://pypi.org/project/chrono-arch/1.0.0/")
else:
    print("⚠️ Upload completed with some issues.")
    print("🔗 https://pypi.org/project/chrono-arch/")
print("=" * 60)

# عرض تعليمات التثبيت
print("\n📦 Install CHRONO-ARCH:")
print("   pip install chrono-arch")
print("")
print("📖 Documentation:")
print("   https://chronoarch.netlify.app")
