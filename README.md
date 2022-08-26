# 九江慈善捐款自动化脚本
> 此脚本可直接获取多个1元捐款二维码，直接扫码可付款

# Linux/Mac Usage
>仅支持Linux与Mac系统, 自行安装chrome浏览器与同版本chromedrive, 具体直接搜素selenium chromedrive安装
> 
> 推荐使用conda环境 ***python>=3.7***

- **抓取master主支**
```bash
git clone https://github.com/ZIFENG278/jiujiang_denote.git
```
- 或者下载zip文件
```bash
wget https://github.com/ZIFENG278/jiujiang_denote/archive/refs/heads/master.zip
```
- **安装所需环境**
```bash
pip3 install -r requirements.txt
```
- **运行脚本**
```bash
python3 denote_jiujiang.py
```
- **在qr_code_save文件夹里扫码捐款**

