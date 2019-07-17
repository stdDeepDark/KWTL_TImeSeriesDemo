## 框架说明

### 1、安装依赖
```
npm i
```

### 2、运行
```
npm run serve
```

### 3、依赖说明
- vuex: 全局变量管理
- vue-router: 路由
- echarts: 图表，v-charts依赖
- v-charts: 基于vue的echarts封装（官网 https://v-charts.js.org）
- axios: 用于ajax请求
- lodash: 基于js函数库
- mockjs: 用于模拟数据

### 4、嵌入代码方式
在框架上写代码：
在/src/pages/Page1.vue中
div.main直接写入代码或引入组件

调用已有链接地址：
在/src/pages/Page2.vue中
div.main的iframe标签中src写入已有url
