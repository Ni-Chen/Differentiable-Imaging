#!/usr/bin/env bash

# 定义分支名称
BRANCH_NAME="main"

# 创建一个新的孤儿分支
git checkout --orphan temp-branch

# 添加所有文件到暂存区
git add .

# 提交暂存区的内容
git commit -m "clean history"

# 删除原分支
git branch -D $BRANCH_NAME

# 将 temp-branch 重命名为原分支
git branch -m $BRANCH_NAME

# 强制推送到远程仓库
git push -f origin $BRANCH_NAME

echo "clean history"