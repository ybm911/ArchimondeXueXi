# ArchimondeXueXi 好好学习脚本

[![Author](https://img.shields.io/badge/Author-Elli0t-blue)](https://spacey.top)

> Archimonde（阿克蒙德） 名字由来：魔兽世界燃烧军团的两大高层干部恶魔之一，号称污染者，拥有无与伦比的破坏能力。

**提供放在服务器端自动运行**

[TOC]

## 快速开始（以江西共青团为例）

### Step0：获取 pid

江西共青团大学习 pid 网址为：

http://osscache.vol.jxmfkj.com/pub/vol/config/organization?pid=N0014

在返回的结果中选择自己的单位的 `id`，例如这里选择上饶师范学院团委：

<img src="https://cdn.jsdelivr.net/gh/ybm911/blog_picture/img/image-20220407105652709.png" alt="image-20220407105652709" style="zoom:50%;" />

将其替换在 `url` 的 `pid` 参数中：

http://osscache.vol.jxmfkj.com/pub/vol/config/organization?pid=N00140002

选址自己的分属团委：

<img src="https://cdn.jsdelivr.net/gh/ybm911/blog_picture/img/image-20220407105840400.png" alt="image-20220407105840400" style="zoom:50%;" />

同上，替换在 `url` 的 `pid` 参数中：

http://osscache.vol.jxmfkj.com/pub/vol/config/organization?pid=N001400021002

选择自己的班级：

<img src="https://cdn.jsdelivr.net/gh/ybm911/blog_picture/img/image-20220407105934050.png" alt="image-20220407105934050" style="zoom:50%;" />

保存自己的 `id` 进入下一步

### Step1：打卡

在脚本中修改输入参数 `nid`（就是我们上一步获取到的 `id`），并且修改 `cardNo`

```json
{
	"course": "7",
	"subOrg": null,
	"nid": "N0014000210021029",	// 替换为 id
	"cardNo": "21XXXX"	// 替换为自己的学号
}
```

* 每个班级学号不同，要遍历打卡的话，请自行修改代码

成果展示：

<img src="https://cdn.jsdelivr.net/gh/ybm911/blog_picture/img/%E6%88%AA%E5%B1%8F2022-04-07%2011.34.02.png" alt="截屏2022-04-07 11.34.02" style="zoom:67%;" />

### Step2：部署服务器自动运行

可以通过脚本设置定时任务（默认每周三上午9点5分自动运行）

```bash
sudo sh task.sh
```

## 重要提示

本脚本仅供学习交流使用，禁止使用脚本干扰正常青年大学习网上主题团课的学习

**写 README.md 不易，给个✨星星呗？**

## 问题和反馈

- 脚本较为简单，欢迎优化。如果你有意见或建议，请发送反馈或提交一个改进建议，或者欢迎提交 Pull request。
- 有问题需要提问？请先搜索 issues 上已有的留言。