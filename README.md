# Differentiable Imaging

本仓库是 **DI（Differentiable Imaging）系列工作的总入口**，用于维护网站与资料索引。

## 项目定位

- 本仓库主要内容是网站页面、图片资源和站点维护脚本
- 用于集中展示论文、进展与相关链接

## 仓库内容

```text
.
|-- docs/                  # Jekyll 网站内容
|   |-- index.md
|   |-- _config.yml
|   |-- Gemfile
|   `-- img/
|-- script/                # 网站维护脚本（非算法代码）
|   |-- setting
|   |-- run
|   `-- clean.sh
|-- LICENSE
`-- README.md
```

## 在线内容

- Differentiable Imaging: A New Tool for Computational Optical Imaging (2023)  
  https://onlinelibrary.wiley.com/doi/full/10.1002/apxr.202200118
- Differentiable Imaging: Progress, Challenges, and Outlook (2025)  
  https://spj.science.org/doi/10.34133/adi.0117

## 本地预览网站

本仓库仅用于网站构建与展示，可通过 Jekyll 本地预览。

```bash
cd docs
bundle install
bundle exec jekyll serve
```

默认访问地址通常为：

```text
http://127.0.0.1:4000
```

## 脚本说明

- `script/setting`: 安装站点依赖
- `script/run`: 启动站点
- `script/clean.sh`: Git 历史压缩/重写脚本（包含 `git push -f`，请谨慎使用）

Windows PowerShell 运行 `.sh` 脚本需通过 Bash（如 Git Bash）调用。

## License

GNU GPL v2. See [LICENSE](LICENSE).
