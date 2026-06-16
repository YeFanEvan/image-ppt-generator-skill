# Image PPT Generator Skill

图片型高质感PPT生成 Skill，用于将客户方案、售前材料、汇报文档转化为蓝白科技风、政企风、数字化平台风的图片型PPT页面，并支持合并PDF或生成图片版PPT。

## 适用场景

这个 Skill 适合以下工作流：

- 根据方案文档生成PPT目录和逐页文案
- 参考已有PPT或截图统一视觉风格
- 生成蓝白科技风、政企风、数字化平台风页面图
- 先生成样张，再分批生成完整PPT页面
- 将多张PPT页面图片按顺序合并为PDF
- 将图片页面进一步转成图片版PPT

## 核心原则

先定内容，再定风格，再出样张，再批量生成，最后合并交付。

## 文件结构

```text
image-ppt-generator-skill/
├── README.md
├── SKILL.md
├── requirements.txt
└── scripts/
    └── merge_images_to_pdf.py
```

## 快速使用

合并图片为PDF：

```bash
python scripts/merge_images_to_pdf.py output.pdf 01_封面.png 02_目录.png 03_正文.png
```

## 注意事项

图片型PPT视觉效果好，但页面元素通常不可直接编辑。如用户要求可编辑PPT，需要重新用PPT组件化方式排版。

中文图片生成容易出现错字，必须重点检查公司名、项目名、客户名、地名、案例名和关键业务名词。
